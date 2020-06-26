from params import *
from utils import *

# [nonce][hash_list len][hash_value]
pow_table = {}



def cumulative_pow(params):
    nonce_int, nonce_bytes, hash_value, hash_offset, pow_bytes, prev_bytes, fingerprint, out_total, in_total = params

    # Pre-filter reduces starting entry no.
    pow_bytes = POW_H(nonce_bytes + hash_value).digest()
    if USE_PRE_FILTER:
        if lead_zeros(pow_bytes) < PRE_FILTER_POW_TARGET:
            return None

    # Do chained filtering second.
    if USE_CHAINED_POW:
        prev_bytes = pow_bytes = POW_H(prev_bytes + pow_bytes).digest()
        if hash_offset <= POW_SET_LEN - 2:
            prefix_no = lead_zeros(pow_bytes)
            if prefix_no < CHAINED_POW_TARGET:
                return None

            set_change_out_field = calc_set_growth(out_total, prefix_no, CHUNK_SIZE_BITS)
            set_change_out_field = at_least_one(set_change_out_field)
            if set_change_out_field * AVG_EDGE_CANDIDATES > MAX_SET_GROWTH:
                # Being triggered in our set cide but is this currently valid?
                return None
            else:
                out_total = set_change_out_field
                
                # Work out value for inside a field too for convenience.
                set_change_in_field = calc_set_growth(in_total, prefix_no, FIELD_SIZE_BITS)
                set_change_in_field = at_least_one(set_change_in_field)
                in_total = set_change_in_field


    # Apply indep filtering to reduce exponential set growth.
    best_nonce_info = [0, 0, MAX_SET_GROWTH, MAX_SET_GROWTH]
    if USE_INDEP_FILTER:
        if FIXED_INDEP_FILTER:
            if hash_offset == POW_SET_LEN - 1:
                pow_bytes = POW_H(nonce_bytes + fingerprint).digest() 
                prefix_no = lead_zeros(pow_bytes)

                # Store results if it makes sense.
                out_total = calc_set_growth(out_total, prefix_no, CHUNK_SIZE_BITS)
                in_total = calc_set_growth(in_total, prefix_no, FIELD_SIZE_BITS)
                best_nonce_info = [nonce_int, nonce_bytes, out_total, in_total]


    return [pow_bytes, prev_bytes, best_nonce_info, out_total, in_total]


def save_cumulative_results(edge_list, out_results, target_to_beat, hash_offset, last_offset, past_results, result_size=5):
    if hash_offset == last_offset:
        pow_bytes, prev_bytes, nonce_info, out_total, in_total = out_results
        target_to_beat = out_total
        nonce_info.append(edge_list)
        nonce_info.append(hash(b"".join(edge_list))) # Used for deterministic ordering.
        past_results.insert(0, nonce_info)

        # Sort by ?
        past_results = sorted(past_results, key=lambda k: (k[2], k[5]))
        if len(past_results) > result_size:
            past_results.pop()


    return target_to_beat, past_results

    

def shared_cumulative_pow_exec(params):
    global pow_table

    results, start, stop, is_last, hash_list = params
    word_list = []
    found = 0

    past_results = []
    result_size = 1000
    fingerprint = POW_H(b"".join(hash_list)).digest()
    target_to_beat = MAX_SET_GROWTH
    for nonce_int in range(start, stop):
        # Initial PoW.
        nonce_bytes = nonce_int.to_bytes((nonce_int.bit_length() + 7) // 8, byteorder="little")

        # Every word after the first.
        # Every element in a sense is also a PoW for another element.
        # So every element in a set save for the last gets filtered twice.
        prev_bytes = b"b"
        pow_bytes = b""
        out_total = 0
        in_total = 0
        last_offset = len(hash_list) - 1
        for hash_offset in range(0, len(hash_list)):
            hash_value = hash_list[hash_offset]
            out_results = cumulative_pow([nonce_int, nonce_bytes, hash_value, hash_offset, pow_bytes, prev_bytes, fingerprint, out_total, in_total])
            if out_results is None:
                break
            
            pow_bytes, prev_bytes, nonce_info, out_total, in_total = out_results

            # Save results if it makes sense.
            edge_list = hash_list[0:hash_offset + 1]
            target_to_beat, past_results = save_cumulative_results(edge_list, out_results, target_to_beat, hash_offset, last_offset, past_results, result_size)



    return past_results


def clusted_shared_pow_manager(sc, usable_cores, hash_list):
    results = []
    params_list = []
    max_nonce = (2 ** NONCE_BITS) - 1
    key_no = int(max_nonce / usable_cores)


    print("Usable cores = ")
    print(usable_cores)

    for i in range(0, usable_cores):
        start = i * key_no
        stop  = (i + 1) * key_no
        is_last = True if i == usable_cores - 1 else False
        if is_last:
            stop += int(max_nonce % usable_cores) + 1

        params_list.append([results, start, stop, is_last, hash_list])

    results = sc.parallelize(params_list, usable_cores).map(shared_cumulative_pow_exec).collect()
    unsorted_results = []
    for result in results:
        unsorted_results = unsorted_results + result

    sorted_results = sorted(unsorted_results, key=lambda k: k[2])
    
    return sorted_results


