from params import *
from utils import *
from golomb_sets import *


def brute_force_executor(params):
    word_index, word, gcs_table, fuzzy_chksum = params
    assert(len(fuzzy_chksum) == WORD_NO * CHKSUM_BITS)

    word_fuzzy_chksum_bit = fuzzy_chksum[word_index * CHKSUM_BITS:(word_index + 1) * CHKSUM_BITS]
    assert(len(word_fuzzy_chksum_bit) == CHKSUM_BITS)

    # Original code works with file streams.
    # Simulate it in memory with byte stream.
    fp = io.BytesIO(gcs_table)
    gcs = GCSQuery(fp)

    # Brute force a list of candidates for a hash in the compress table.
    # Then we're going to do a bunch of sheet to the offsets. Tru story.
    candidate_list = []
    bits = int((2 ** CHUNK_SIZE_BITS) - 1)
    i = 0
    while i <= bits:
        # Serialize int to bytes / bits.
        # We're brute forcing a bit stream by increasing numbers.
        # Not very efficent but this code isn't the lengthy part.
        test_word_bits = Bits(intVal = i)
        test_word_bits = byte_align(test_word_bits, CHUNK_SIZE_BITS)
        test_word_bytes = to_bytes(test_word_bits)
        
        # Hash word chunk of input data.
        test_hash_no = h1(test_word_bytes)
        test_bit = test_hash_no[:CHKSUM_BITS]
        assert(len(test_bit) == CHKSUM_BITS)

        # There's an N bit checksum. 
        if test_bit != word_fuzzy_chksum_bit:
            i += 1
            continue
        
        assert(len(test_word_bits) == CHUNK_SIZE_BITS)

        # Bloom filter: actual code to save candidate from gcs.        
        # Only save candidates found in bloom filter.
        word_bytes = word_format(test_word_bits, word_index)
        if gcs.query(word_bytes):
            candidate_list.append(test_word_bytes)
                
        i += 1
        

    return [word_index, candidate_list.index(word), len(candidate_list)]
        

def brute_force_controller(sc, word_no, words, usable_cores, gcs_table, fuzzy_chksum):
    # Forget about forward filter crap.
    # It's not used any more.
    # Chunk bits moved to globals.


    
    results = []
    remaining = word_no
    word_index = 0
    while remaining > 0:
        worker_no = min(usable_cores, remaining)
        
        # Build param lists for workers.
        params_list = []
        for i in range(0, worker_no):
            params = [word_index, to_bytes(words[word_index]), gcs_table, fuzzy_chksum]
            params_list.append(params)
            word_index += 1

        # Schedule workers to run across cores and wait for results.
        answers = sc.parallelize(params_list, usable_cores).map(brute_force_executor).collect()
        results = results + answers
        
        # Keep going until all done.
        remaining -= worker_no


    # Sort results by word index order.
    results = sorted(results, key=lambda x: x[0])

    # Build useful results.
    node_list   = [ ]
    candidate_no_list = [ ]
    for result in results:
        node_list.append(result[1])
        candidate_no_list.append(result[2])
        

    return [node_list, candidate_no_list]



