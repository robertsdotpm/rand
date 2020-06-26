from params import *
import hashlib

def sort_duplicates(my_list):
    my_list.sort()
    my_list = list(my_list for my_list,_ in itertools.groupby(my_list))
    
    return my_list


def byte_align(bv, bv_len=0):
    if bv_len:
        if len(bv) < bv_len:
            dif = bv_len - len(bv)
            
            # Pad from the left.
            bv = Bits(bitlist=[0] * dif) + bv
            
        return bv
    else:    
        bv_len = len(bv)
        if bv_len % 8:
            bound = bv_len % 8
        else:
            return bv
        
        bv = Bits(bitlist=[0,0,0,0,0,0,0,0][:8 - bound]) + bv

        return bv


def to_bytes(bv):
    if type(bv) == bytes:
        return bv
    
    bv_len = len(bv)
    buf = b""
    offset = 0
    while bv_len > 0:
        if bv_len >= 8:
            buf += bytes([int(bv[offset * 8:(offset + 1) * 8])])
            bv_len -= 8
        else:
            partial_byte = bv[offset * 8:]
            partial_byte = byte_align(partial_byte)
            buf += bytes([int(partial_byte)])
            bv_len = 0
            break
            
        offset += 1
        
    return buf


def bitsof(bt, nbits):
    # Directly convert enough bytes to an int to ensure you have at least as many bits
    # as needed, but no more
    neededbytes = (nbits+7)//8
    if neededbytes > len(bt):
        raise ValueError("Require {} bytes, received {}".format(neededbytes, len(bt)))
    i = int.from_bytes(bt[:neededbytes], 'big')
    # If there were a non-byte aligned number of bits requested,
    # shift off the excess from the right (which came from the last byte processed)
    if nbits % 8:
        i >>= 8 - nbits % 8
    return i

    
def h1(buf):
    return Bits(rawbytes=xxhash.xxh32(to_bytes(buf)).digest())
    

def mk_chksum_bit(word, bit_no=1):
    word_hash = h1(word)
    

    return word_hash[:CHKSUM_BITS]

    
class build_mk_forward_filter:
    def __init__(self, hash_func):
        self.hash_func = hash_func
        self.prev_hash = None
        self.prev_word = None
        self.i = 0
        
    def internal_hash(self, prev_hash, prev_word, word, replace=0, bit_no=1):
        if type(prev_word) == type(None):
            self.prev_word = word
            return [Bits(bitlist = [0] * bit_no), 0]
            
        if type(prev_hash) == type(None):
            unknown = self.hash_func(to_bytes(prev_word) + to_bytes(word))
        else:
            if word == prev_word:
                return [Bits(rawbytes=prev_hash)[:bit_no], self.prev_hash]
        
            unknown = self.hash_func(prev_hash + to_bytes(word))
            
        if replace:
            self.prev_word = word
            

        hash_bytes = to_bytes(unknown)
        if replace:
            self.prev_hash = hash_bytes

        
        #bound = min(bit_no, len(unknown))
        return [unknown[:bit_no], hash_bytes]
    
    def mk_forward_filter(self, word, i=0, replace=1, bit_no=1):
        if type(self.prev_word) == type(None):
            self.prev_word = word
            self.i = i
            unknown = self.hash_func(to_bytes(word))
            self.prev_hash = to_bytes(unknown)
            return unknown[:bit_no]
            
        return self.internal_hash(self.prev_hash, self.prev_word, word, replace, bit_no)[0]


def mk_chksum(words, bit_fun, direction="forwards", bit_no=None):
    # Process words.
    # Reverse interate or not
    word_list = words
    
    # Process word list.
    chksum = Bits(size=0)
    for word in word_list:
        chksum_bits = bit_fun(word, bit_no=bit_no)
        if bit_no != None:
            assert(len(chksum_bits) == bit_no)

        chksum = chksum + chksum_bits

    # Mark final bit with 1 to indicate "end".
    #chksum += Bits(bitlist=[1])
    #chksum = byte_align(chksum)

    
    return chksum

    
def buf_to_chunks(buf):
    # Cut buf up into words
    buf_len = len(buf) 
    words = []
    for i in range(0, int(buf_len / CHUNK_SIZE_BITS) or 1):
        if buf_len - ((i + 1) * CHUNK_SIZE_BITS) >= CHUNK_SIZE_BITS:
            word = buf[i * CHUNK_SIZE_BITS: (i + 1) * CHUNK_SIZE_BITS]
            
            assert(len(word) == CHUNK_SIZE_BITS)
            words.append(word)
        else:
            word = buf[i * CHUNK_SIZE_BITS:]
            
            assert(len(word) == CHUNK_SIZE_BITS)
            words.append(word)

    assert(len(words) % 2 == 0)
            
    return words
    

def print_formed_chains(x, skip_print=0):
    out = []
    for pair_offset in range(0, len(x)):
        for pairs_offset in range(0, len(x[pair_offset])):
            for pairs_chain_offset in range(0, len(x[pair_offset][pairs_offset])):
                chain = []
                for match_offset in range(0, len(x[pair_offset][pairs_offset][pairs_chain_offset])):
                    match = x[pair_offset][pairs_offset][pairs_chain_offset][match_offset]
                    if type(match) != list and match is not None:
                        chain.append(int(match))

                if len(chain):
                    out.append(chain)


    out.sort()
    out = list(out for out,_ in itertools.groupby(out))
    skip_print or print(out)
    
    return str(out)

    
def print_longest_chains(x, skip_print=0):
    out = []
    for match_list in x:
        out_list = []
        for match in match_list:
            if match is None:
                continue
            if type(match) == list:
                for sub_match in match:
                    out_list.append(int(sub_match))
            else:
                out_list.append(int(match))
            
        if len(out_list):
            out.append(out_list)

    out.sort()
    out = list(out for out,_ in itertools.groupby(out))
    skip_print or print(out)
    
    return str(out)


def print_node_list(x, skip_print=0):
    out = []
    for node in x:
        out.append(str(int(node)))
        
    skip_print or print(out)
    
    return str(out)
            
    #print(x)
    
    """
    #y = str(x)
    y = y.replace(">", '"')
    y = y.replace("<", '"')
    y = y.replace("None", '0')
    y = y.replace("BitVector.BitVector.BitVector object at", "")
    print(y)
    """


# candidate_lists
def print_candidate_list_as_grid(candidate_lists, skip_print=0):
    buf = ""
    spacing = " " * 4
    for row_offset in range(0, 1000):
        rows_written = 0
        for col_offset in range(0, len(candidate_lists)):
            col = candidate_lists[col_offset]
            
            if row_offset < len(col):
                rows_written = 1
                value = str(col[row_offset])
                padding = " " * (CHUNK_SIZE_BITS - len(value))
                buf += str(col[row_offset]) + padding + spacing
            else:
                buf += spacing + (" " * CHUNK_SIZE_BITS)
                    
        # Start a new row.        
        buf += "\r\n"
                
        if not rows_written:
            break
            
    skip_print or print(buf)
    
    return str(buf)
    

def print_match_chains(match_chains, skip_print=0):
    out = []
    for link_offset in range(0, len(match_chains)):
        out.append([])
        match_pair_list = match_chains[link_offset]
        for match_pair_offset in range(0, len(match_pair_list)):
            pair = match_pair_list[match_pair_offset]
            node_a = str(int(pair[0]))
            node_b = str(int(pair[1]))
            out[link_offset].append([node_a, node_b])
            
    skip_print or print(out)
    
    return str(out)


def node_list_to_match_list(node_list):
    match_list = []
    assert((len(node_list) % 2) == 0)
    
    bound = int(len(node_list) / 2)
    for i in range(0, bound):
        node_a = node_list[i * 2]
        node_b = node_list[(i * 2) + 1]
        pair = [node_a, node_b]
        
        
        match_list.append([pair])
        
    assert(len(match_list) == int(len(node_list) / 2))
    return match_list
    

# Build a list of offsets for a word in the candidate sets.
# Returns node_list and candidate_no_list.
def candidates_to_nodes(word_list, candidates_list, candidates_no_list):
    assert((len(word_list) % 2) == 0)
    
    node_list = []
    for i in range(0, len(candidates_list)):
        candidate_list = candidates_list[i]
        is_found = 0
        for j in range(0, len(candidate_list)):
            candidate = candidates_list[j]
            if candidate == word_list[i]:
                node_list.append(j)
                is_found = 1
            
        if not is_found:
            raise Exception("Could not find word in candidate list.")

    return node_list


# Generate candidates.
def generate_rand_node_list(word_no, cand_low, cand_high, cand_no=0):
    node_list = []
    candidate_no_list = []
    candidate_no = cand_no or random.randrange(cand_low, cand_high)
    for i in range(0, word_no):
        if not FIXED_CAND_NO:
            candidate_no = cand_no or random.randrange(cand_low, cand_high)
            
        # Node is an offset in a list of candidates.
        node = random.randrange(0, candidate_no)
        assert(node < candidate_no)
        node = Bits(intVal=node)
        
        node_list.append(node)
        candidate_no_list.append(candidate_no)
        
    assert(len(node_list) == word_no)
    assert(len(candidate_no_list) == word_no)
    return [node_list, candidate_no_list]
    

def generate_rand_candidate_lists(candidate_no_list, chunk_size_bits):
    # List of candidates.
    max_bits = (2 ** chunk_size_bits) - 1
    cand_lists = []
    for candidate_no in candidate_no_list:
        candidates = [max_bits * 2]
        for i in range(0, candidate_no):
            cand = candidates[0]
            while cand in candidates:
                cand = random.randrange(0, max_bits)
                
            candidates.append(cand)
            
        # Convert to bits.
        for i in range(0, candidate_no):
            candidates[i] = Bits(intVal=candidates[i])
            
        cand_lists.append(candidates[1:])
        assert(len(cand_lists[-1]) == candidate_no)
        
    assert(len(cand_lists) == len(candidate_no_list))
    return cand_lists
    

# Generate false candidates per set.
def insert_false_matches_into_match_list(match_list, candidate_no_list, cand_high, fake_no):
    # Otherwise there isn't a high enough amount of entropy to generate unique sets.
    assert((cand_high * cand_high) ** 2 >= fake_no)
    
    # Generate list of random nodes.
    rand_nodes_a = []
    rand_nodes_b = []
    for rand_nodes in [rand_nodes_a, rand_nodes_b]:
        for i in range(0, cand_high):
            if i == cand_high - 1:
                break
    
            rand_node = random.randrange(0, i + 1)
            rand_nodes.append(Bits(intVal=rand_node))
    
    # Populate a given list with the required no of fake nos.
    for matches_offset in range(0, len(match_list)):
        node_a_cand_no = candidate_no_list[matches_offset * 2]
        node_b_cand_no = candidate_no_list[(matches_offset * 2) + 1]
        matches_list = match_list[matches_offset]
        valid_match = matches_list[0]
        
        matches_list = []
        while len(matches_list) != fake_no:
            cur_len = len(matches_list)

            
            assert(node_a_cand_no)
            assert(node_b_cand_no)
            
            node_a_offset = (cur_len + node_b_cand_no) % (node_a_cand_no - 1)
            node_a = rand_nodes_a[node_a_offset]
            assert(node_a_offset < node_a_cand_no)
            
            node_b_offset = (cur_len + node_a_cand_no) % (node_b_cand_no - 1)
            node_b = rand_nodes_b[node_b_offset]
            assert(node_b_offset < node_b_cand_no)
            
            fake_pair = [node_a, node_b]
            matches_list.append(fake_pair)
            
        # Insert valid match randomly back into set.
        match_list[matches_offset] = matches_list
        insert_offset = random.randrange(0, fake_no)
        matches_list[insert_offset] = valid_match
        assert(int(valid_match[0]) < node_a_cand_no)
        assert(int(valid_match[1]) < node_b_cand_no)
        
        assert(len(match_list[matches_offset]) == fake_no)
        assert(valid_match in match_list[matches_offset])
        
    assert(len(match_list[0]) == fake_no)
    return match_list
    
    
# Formed chain [match 0 pair offset][possible sub chains ...]
# formed_chain_lists = [ [None] for i in range(len(match_chains[0])) ]
def return_longest_chains_from_formed_chains_list(formed_chains_list):
    chains = []
    len_to_beat = 0
    x = formed_chains_list
    for pair_offset in range(0, len(x)):
        for pairs_offset in range(0, len(x[pair_offset])):
            for child_chain_offset in range(0, len(x[pair_offset][pairs_offset])):
                chain = x[pair_offset][pairs_offset][child_chain_offset]
                if (len(chain) % 2) != 0:
                    continue
                
                if len(chain) > len_to_beat:
                    len_to_beat = len(chain)
                    chains = []
                    
                if len(chain) == len_to_beat:
                    chains.append(chain)

    chains.sort()
    chains = list(chains for chains,_ in itertools.groupby(chains))
    return chains


def is_node_list_in_match_list(node_list, match_list):
    for i in range(0, len(match_list)):
        col_i_edges = match_list[i]
        is_found = 0
        for j in range(0, len(col_i_edges)):
            col_i_edge = col_i_edges[j]
            col_i_edge = [  int(col_i_edge[0]), int(col_i_edge[1])  ]
            node_edge  = [  int(node_list[i * 2]), int(node_list[(i * 2) + 1])    ]
            
            if col_i_edge == node_edge:
                is_found = 1
                break
                
        if not is_found:
            return 0
            
    return 1
            

def get_most_valid_chain_offset(chains_list, node_list):
    for i in range(0, len(chains_list)):
        chain = chains_list[i]
        didnt_match = len(chain)
        
        for j in range(0, min(len(chain), len(node_list)) ):
            found_node    = chain[j]
            expected_node = node_list[j]
            
            if found_node == expected_node:
                didnt_match -= 1
                
        if not didnt_match:
            return i
            
    raise Exception("Unable to find single instance of a valid chain in chains list.")


def process_candidates(parent_no, hash_chains, child_match, forward_filter_no, boundary_count, gcs, success_func):
    # Generate
    candidate_total = 0
    for [prev_child_match_offset, test_hasher] in hash_chains:
        candidate_total += 1
        
        # Do hash test.
        prev_child_match = test_hasher.prev_word
        assert(len(prev_child_match) == CHUNK_SIZE_BITS)
        assert(len(child_match) == CHUNK_SIZE_BITS)
        # Check hash result
        hash_result_no, hash_result = test_hasher.internal_hash(test_hasher.prev_hash, to_bytes(prev_child_match), to_bytes(child_match), bit_no=FORWARD_FILTER_BITS)
        assert(len(hash_result_no) == FORWARD_FILTER_BITS)
        
        if hash_result_no != forward_filter_no:
            continue
        
        if boundary_count == WORD_HASH_BOUNDARY and WORD_HASH_BOUNDARY:
            if parent_no == 0:
                boundary_hash = xxhash.xxh32( to_bytes(child_match) ).digest()
            else:
                boundary_hash = xxhash.xxh32(to_bytes(prev_child_match) + to_bytes(child_match)).digest()
            if not gcs.query(boundary_hash):
                continue
                
        success_func(hash_result, prev_child_match_offset)

    return candidate_total


# TODO: outdated now.
def cipher_filter_str_to_cipher_list(cipher_filter):
    filter_list = []
    filter_no = len(cipher_filter) / MAX_CIPHER_EDGE_BITS
    
    for i in range(1, filter_no + 1):
        bound = min(i * MAX_CIPHER_EDGE_BITS, len(cipher_filter))
        
        # Truncate high order padded zero bits.
        filter = int(cipher_filter[(i - 1) * MAX_CIPHER_EDGE_BITS:bound])
        
        # Save filter.
        filter_list.append(Bits(intVal=filter))

    return filter_list


def cand_lists_to_match_list(candidate_lists, candidate_list_no):
    assert(len(candidate_lists) % 2 == 0)

    match_list = []
    for edge_offset in range(0, int(len(candidate_lists) / 2)):
        start_offset = edge_offset * 2
        stop_offset = start_offset + 2
        cand_list_a, cand_list_b = candidate_lists[start_offset:stop_offset]
        
        edge_list = []
        for cand_a in cand_list_a:
            for cand_b in cand_list_b:
                edge = [ cand_a, cand_b ]
                edge_list.append(edge)

        match_list.append(edge_list)

    return match_list


def compute_edge_hash(edge_offset, node_a, node_b):
    # Node a h part.
    offset_a = edge_offset * 2
    txt_a = b"[%d] %d" % (offset_a, node_a)

    # Node b h part
    offset_b = offset_a + 1
    txt_b = b"[%d] %d" % (offset_b, node_b)

    # H input is node a, node b = edge.
    h_input = b"%s; %s;" % (txt_a, txt_b)
    h_out = POW_H(h_input).digest()

    return h_out


# Hash list passed to shared PoW function.
def compute_edge_hash_list(node_list, set_offset, out_edge_hash):
    hash_list = []
    pair_no = int(len(node_list) / 2)
    for i in range(0, pair_no):
        node_a = node_list[i * 2]
        node_b = node_list[(i * 2) + 1]

        edge_offset = (set_offset * POW_SET_LEN) + i
        h_out = compute_edge_hash(edge_offset, node_a, node_b)
        if i == 0:
            # Link together the output of the previous set to form a chain.
            h_out = POW_H(out_edge_hash + h_out).digest()
            
        hash_list.append(h_out)

    return hash_list


def bitvec_list_to_int_list(vec_list):
    int_list = []
    for vec in vec_list:
        int_list.append(int(vec))

    return int_list


def count_chains_at_pairs_offset(formed_chains, pairs_offset):
    total = 0
    for pair_offset in range(0, len(formed_chains)):
        child_chains = formed_chains[pair_offset]
        total += len(child_chains[pairs_offset])

    return total




def compute_bytes_saved(gcs_table_len):
    # Calculate bytes saved.
    nonce_bytes = math.ceil(SET_NO * (NONCE_BITS / 8))
    bit_filter_bytes = math.ceil((CHKSUM_BITS * WORD_NO) / 8)
    chksum_bytes = math.ceil(ACCURATE_CHKSUM_BITS / 8)
    used_bytes  = gcs_table_len + bit_filter_bytes
    used_bytes += nonce_bytes + chksum_bytes
    bytes_saved = BUF_SIZE - used_bytes

    return bytes_saved


def calc_set_growth(set_total, prefix_no, chunk_size_bits):
    chained_p = (1.0 / (2 ** prefix_no))

    bloom_positives = (2 ** chunk_size_bits) * (1.0 / PROB)
    bloom_positives = bloom_positives * (1.0 / (2 ** CHKSUM_BITS)) 
    edge_candidates = bloom_positives ** 2

    set_change = (set_total * edge_candidates) * chained_p

    return set_change


# Indep can be random, fixed, or guided. Forget guided for now.
# todo: Convert to actual probabilities.
# I may need to change my new math based on the new chaining code.
# chksum bits needs to be applied to edges inside set
# chksum bits needs to be applied to every word to work -- currently that is too large to store without taking up all data
# Final chained filter should not be applied if not using fixed indep
at_least_one = lambda i: 1.0 if i < 1 else i
def compute_max_chains(chunk_size_bits=CHUNK_SIZE_BITS, chaining_version=1, output=0):
    # Filter individual words
    bloom_positive_no = (2 ** chunk_size_bits) * (1.0 / PROB) # 340.4  todo: inside i loop
    bloom_positive_no = bloom_positive_no * (1.0 / (2 ** CHKSUM_BITS)) 

    # Total number of edge candidates.
    cand_no = bloom_positive_no ** 2 # 
    total = 0
    prev_set_col_no = 1
    set_no = 1 # Comment out to run full test.
    for j in range(0, set_no):
        #print("Set no = %d" % (j + 1))
        indep_target = random.randrange(0, POW_SET_LEN)
        for i in range(0, POW_SET_LEN):
            col_no = cand_no

            # Apply pre-filtering if enabled.
            # Can be applied independently.
            if USE_PRE_FILTER:
                col_no = cand_no * (1.0 / (2 ** PRE_FILTER_POW_TARGET))
                col_no = at_least_one(col_no)

            # Apply chained filtering if enabled.
            # Not independent so previous results are applied.
            if USE_CHAINED_POW:
                # Exponential function here to destroy.
                chained_p = (1.0 / (2 ** CHAINED_POW_TARGET))
                if chaining_version == 2:
                    chained_p /= (POW_SET_LEN - j)

                """
                if USE_INDEP_FILTER:
                    if FIXED_INDEP_FILTER:
                        if i == POW_SET_LEN - 1:
                            chained_p = 1
                """
                
                col_no = (prev_set_col_no * col_no) * chained_p
            else:
                col_no = (prev_set_col_no * col_no)
            col_no = at_least_one(col_no)

            if output:
                print(col_no)

            # Apply indep filtering if enabled.
            # Occurs once per set based on mode.
            if USE_INDEP_FILTER:
                # Random mode.
                if FIXED_INDEP_FILTER == 0:
                    # Apply random indep filter.
                    if i == indep_target:
                        # POW_SET_LEN because POW_SET_LEN times chance of false positve.
                        col_no = col_no * ((1.0 / (2 ** INDEP_POW_TARGET)) * POW_SET_LEN)

                # Fixed mode.
                if FIXED_INDEP_FILTER:
                    # Apply filter.
                    if i == POW_SET_LEN - 1:
                        col_no = col_no * (1.0 / (2 ** INDEP_POW_TARGET))

            col_no = at_least_one(col_no)
            prev_set_col_no = col_no
            if output:
                print(col_no)
                print()


    total = prev_set_col_no
    return total
                    

def rand_bv(buf=0):
    # Data seems to need to be a multiple of the data chunk sizes
    # Generate random data.
    buf = buf or secrets.token_bytes(BUF_SIZE)

    # Ensure rand data buf is word aligned right.
    bv = Bits(rawbytes=buf)
    if len(bv) % CHUNK_SIZE_BITS:
        dif = CHUNK_SIZE_BITS - (len(bv) % CHUNK_SIZE_BITS)
        bv = bv + Bits(bitlist=[0] * dif)
        
    assert((len(bv) % CHUNK_SIZE_BITS) == 0)

    # Make sure word count ends up even too.
    word_no = math.ceil((BUF_SIZE * 8) / CHUNK_SIZE_BITS)
    if word_no % 2:
        bv = bv + Bits(bitlist=[0] * CHUNK_SIZE_BITS)

    # Should be set size aligned really

    # Update buf based on changes.
    #as_hex = bv.get_bitvector_in_hex().encode("ascii")
    #buf = hex_down(as_hex)

    return bv


def get_run_time(core_no):
    total = 0

    # Brute force candidate tables.
    total += (WORD_NO / core_no) * 120 # Two mins to brute force 17 bits per core.

    # Calculate shared PoW for edge_hash lists.
    total += 0


def lead_zeros(buf, buf_len=POW_H_LEN):
    total_bits = buf_len * 8
    format_str = "{:0" + str(total_bits) + "b}"
    as_int = int.from_bytes(buf, byteorder='big')
    try:
        as_str = format_str.format(as_int)
        return as_str.index("1")
    except:
        return total_bits


def print_bytes(buf):
    as_hex = binascii.hexlify(buf).decode("utf-8")
    as_bin = str(Bits(rawbytes=buf))
    zero_prefix = lead_zeros(buf)

    print("\n %s\n%s\nprefix = %d (0 is success)\n" %
        (as_hex, as_bin, zero_prefix)
    )

def pow_view(nonce_bytes, hash_list):
    prev_bytes = b"b"
    fingerprint = POW_H(hash_list[0] + hash_list[1] + hash_list[2] + hash_list[3]).digest()
    i = 1
    for hash_value in hash_list:
        print("Hash no = ")
        print(i)

        # Pre-filter reduces starting entry no.
        pow_bytes = POW_H(nonce_bytes + hash_value).digest()
        if USE_PRE_FILTER:
            print("Pre filter = ")
            print_bytes(pow_bytes)

        # Do chained filtering second.
        if USE_CHAINED_POW:
            prev_bytes = pow_bytes = POW_H(prev_bytes + pow_bytes).digest()
            print("Chained pow = ")
            print_bytes(pow_bytes)

        # Apply indep filtering to reduce exponential set growth.
        if USE_INDEP_FILTER:
            if FIXED_INDEP_FILTER:
                if i == len(hash_list):
                    pow_bytes = POW_H(nonce_bytes + fingerprint).digest() 

                    print("Fixed indep = ")
                    print_bytes(pow_bytes)
            else:
                print("Fixed indep = ")
                print_bytes(pow_bytes)

        i += 1


def get_sc():
    spark_config = (SparkConf().set("spark.cores.max", str(CLUSTER_CORE_NO)))
    sc = SparkContext(SPARK_URI, conf=spark_config) 
    sc.setLogLevel('OFF')

    py_files = ["checksum.py", "experiment.py", "golomb_sets.py", "brute_force.py", "compress.py",
        "decompress.py", "params.py", "shared_pow.py",
        "utils.py"]

    for py_file in py_files:
        sc.addPyFile(py_file)

    return sc


# Index starts at 0.
def word_format(word, word_index):
    assert(len(word) == CHUNK_SIZE_BITS)

    no_prefix = b""
    if USE_NO_PREFIX:
        no_prefix = b"word %d " % (word_index)

    word_bytes = no_prefix + to_bytes(word)

    return word_bytes
    

def is_word_in_field(nonce_hash, word_int):
    max_field_int = int((2 ** FIELD_SIZE_BITS) - 1)
    assert(max_field_int < MAX_WORD_INT)

    # Nonces tend to cluster around higher numbers.
    # Make distribution more uniform.
    rand_int = int.from_bytes(nonce_hash, byteorder='big')

    # Place field randomly in CHUNK_SIZE_BITS space.
    field_offset = rand_int % MAX_WORD_INT

    # Wrap the word inside the shrunken field.
    field_word_int = word_int % max_field_int

    # Determine if the above field word intersects our randomly placed field.
    lower_bound = field_offset
    upper_bound = (field_offset + max_field_int) % MAX_WORD_INT

    if field_word_int >= lower_bound and field_word_int <= upper_bound:
        return 1

    # Otherwise field word doesn't intersect random field.
    return 0


def choose_best_nonce(set_nonce_results, set_word_list):
    # Go over the 100s of nonces returned from the cluster and choose the best.
    # The nonce set is already sorted with the best first.
    # But we're also checking for field compatability here.
    use_field = False
    best_nonce_result = None
    for nonce_result in set_nonce_results:
        nonce_int, nonce_bytes, set_total_out_field, set_total_in_field = nonce_result
        nonce_hash = POW_H(nonce_bytes).digest()
        valid_words = 0

        # Add up number of intersecting words.
        for word in set_word_list:
            word_int = int(word)
            if is_word_in_field(nonce_hash, word_int):
                valid_words += 1
            else:
                break

        # All words for nonce intersect field.
        if valid_words == (POW_SET_LEN * 2):
            best_out_no = set_nonce_results[0][2]
            if set_total_in_field < best_out_no:
                best_nonce_result = nonce_result
                use_field = True
                break


    # Unable to find a valid nonce that intersects the field with good set reduction.
    # Use the best nonce available instead.
    if best_nonce_result is None:
        best_nonce_result = set_nonce_results[0]


    return [best_nonce_result, use_field]


def min_prefixes(nonce_bytes, hash_list):
    max_zeros = POW_H_LEN * 8
    min_prefixes = [[max_zeros, max_zeros] for i in range(0, POW_SET_LEN)]
    prev_bytes = b"b"
    fingerprint = POW_H(b"".join(hash_list)).digest()
    hash_offset = 0
    for hash_value in hash_list:
        # Do chained filtering second.
        pow_bytes = POW_H(nonce_bytes + hash_value).digest()
        if USE_CHAINED_POW:
            prev_bytes = pow_bytes = POW_H(prev_bytes + pow_bytes).digest()
            prefix = lead_zeros(pow_bytes)
            if prefix < min_prefixes[hash_offset][0]:
                min_prefixes[hash_offset][0] = prefix

        # Apply indep filtering to reduce exponential set growth.
        if USE_INDEP_FILTER:
            if FIXED_INDEP_FILTER:
                if hash_offset == len(hash_list) - 1:
                    pow_bytes = POW_H(nonce_bytes + fingerprint).digest()
                    prefix = lead_zeros(pow_bytes)
                    if prefix < min_prefixes[hash_offset][1]:
                        min_prefixes[hash_offset][1] = prefix

        hash_offset += 1

    return min_prefixes




