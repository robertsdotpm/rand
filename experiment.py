from params import *
from utils import *
from shared_pow import *
from compress import *


if __name__ == '__main__':


    hash_list = [b'\xa2\xd3\xaf\x04\x8d\x98\xb6\xf1e\t|\xb9\x94K8C\x02\xa5\xe9p', b'9c\xb3\x84g4\xc6\xf4G\x89\x1e\xaa2E\nqaS\xc46', b'\x84J\x940jXr\x00$9\xe7s\xa8\xa2 `cV\xf4\x17', b'\xbb0\x11y\xf0X\x8a\xb0\xc6EqV\\s\xf2m\xc3\x98\x85x']
    nonce_bytes = b'c\xf5\xc26'
    #pow_view(nonce_bytes, hash_list)
    

    #exit()

    core_no = 112
    #sc = pyspark.SparkContext("spark://192.168.75.22:7077", "test") \




    

    x = b"test"


    rand_bv = rand_bv()
    words = buf_to_chunks(rand_bv)
    gcs_table = add_words_to_filter(words)


    

    print(compute_max_chains(output=1))
    print()

    print(compute_bytes_saved(len(gcs_table)))

    # Calculate time for completation based on core and clock speed.

    exit()


    # todo calc output size


    #print(math.ceil((CHKSUM_BITS * 242) / 8))

    #print(saved)

    #exit()

    """

    searching 4 bytes with 112 cores = 48 mins


    cul pow = 68719476753
        ^ possibly 2 lots of 35 prefix

    we 

[b'\xa2\xd3\xaf\x04\x8d\x98\xb6\xf1e\t|\xb9\x94K8C\x02\xa5\xe9p', b'9c\xb3\x84g4\xc6\xf4G\x89\x1e\xaa2E\nqaS\xc46', b'\x84J\x940jXr\x00$9\xe7s\xa8\xa2 `cV\xf4\x17', b'\xbb0\x11y\xf0X\x8a\xb0\xc6EqV\\s\xf2m\xc3\x98\x85x']


    11:50 - 


    c=1(5), pf=1(2), idf=1(12,r) == 262144.0  # Lowest that works so far.
    c=1(6), pf=1(1), idf=1(15,r) == 32768.0  # Lowest that works so far.

    c=1(6), pf=1(1), idf=1(14,f) == 16384.0 -- works
                                    chksum bits = 2 --
                                64


    c=1(6), pf=1(1), idf=1(14,f, chksum -- 3
        -- set len to 5 == 9:09 -- 

    c=1(6), pf=1(1), idf=1(15,f) -- 7:55 -- hung


    c=1(5), pf=1(2), idf=1(15,r) ==  hung

    c=1(5), pf=0(0), idf=1(10,r) == 10:28 -- 10:43 with chaining v2 
        1048576.0
        repeat with bug fix to pow: hung

    c=1(5), pf=1(2), idf=1(10,r) == 10:48 with chaining v2  -- hung
        
    c=1(5), pf=1(1), idf=1(10,r) == 10:48 with chaining v2 -- quit

    c=1(7), pf=0, idf=1(10,r) == 11:27 with chaining v2  -- hung


    total culmative pow across all 5 hashes see how high you get. 
    
    save offset into prob set using set finger print after reduction stage 1
    then do 20 on it? 262144 * (1.0 / (2 ** 20))
        extra filter leaves 2 bytes remaining

    
    not confirmed:
    c=1(5), pf=1(2), idf=1(12,f) == 65536.0 
    c=1(5), pf=1(2), idf=1(12,r) == 16384.0 
    c=1(6), pf=1(2), idf=1(12,f) == 4096.0


    # if this works its probable the whole thing does
    c=1(10), pf=1(2), idf=1(8,f) == 256  -- 7:18 -- hung

    c=1(3), pf=1(2), idf=1(25,r) == 2048.0 -- 9:10 -- 


    h_in = binascii.unhexlify(b"05b9d3a05b98c985e40b88b575d4129c724e9a27")
    nonce_bytes = 
    print(bitsof(x, 4))

    exit()
    """
    


    # Experiment variables.
    #usable_cores = multiprocessing.cpu_count() # Use all CPU cores available.
    hash_no = POW_SET_LEN * 2
    cand_no = 16384

    # Correct offsets.
    node_list, candidate_no_list = generate_rand_node_list(hash_no, 0, 0, cand_no)
    match_list = node_list_to_match_list(node_list)

    # Some false matches including valid offsets mixed randomly.
    insert_false_matches_into_match_list(match_list,
        candidate_no_list, cand_no, cand_no - 1)

    # Check recovery is actually possible.
    assert(is_node_list_in_match_list(node_list, match_list))

    print("here 1")

    # Is hash list actually high entropy?

    # Generate shared PoW on one machine.
    hash_list = compute_edge_hash_list(node_list, 0, b"x")[:POW_SET_LEN]
    assert(len(hash_list) == POW_SET_LEN)

    print("here 2")
    print(hash_list)

    print()

    #nonce_int, nonce_bytes, cul_pow = cpu_shared_pow_manager(usable_cores, hash_list)
    sc = get_sc()
    results = clusted_shared_pow_manager(sc, core_no, hash_list)

    best_nonce, use_field = choose_best_nonce(results, words[:POW_SET_LEN * 2])

    print(best_nonce)
    print(use_field)

    print(results)
    
    nonce_int, nonce_bytes, cul_pow = results[0]

    nonce_list = [nonce_int]

    print("cul pow")
    print(cul_pow)
    print()

    print(nonce_list)
    print("\a")

    # After this point success is assumed.
    pow_view(nonce_bytes, hash_list)



    exit()

    # Attempt recovery using sPoW.
    formed_chains = compute_formed_chains(match_list, nonce_list)

    print("End formed chains")

    longest_chains = return_longest_chains_from_formed_chains_list(formed_chains)
    print_longest_chains(longest_chains)

    print("ending prog")

"""
t=5, sl=4 s

t=6, sl=4  1:35 -- 1:37
t=6, s1=4  1:38 -- 1:39  3937367516
t=7, s1=4  1:39 -- failed / hung
t=7, 1:56 failed
t=6, sl=5  2:11 -- failed / hung

6, 4, indep, 10:55 -- hung
6, 4, dep, 10:53 -- hung
5, 4, dep 10:59 -- instant
6, 4, dep, 10:53 -- 11:02
6, 4, dep, 11:02 -- 11:05 

5, 4, indep 11:12 -- hung
14, 4, indep, no chained 11:24 -- instantly

5, 4, indep 4(10), 1:25 -- hung
5, 4, indep 4(5), 1:31 -- hung
5, 4, indep 4(4), 1:33 -- hung
5, 4, indep 4(2), 1:37 -- 1:49 success (3 would work too) 8?
5, 4, indep 4(4), 1:49 -- hung

5, 4, indep 4(2), single indep 15 2:28 -- hung
5, 4, indep 4(2), 4 indep 8 -- 9 minutes
5, 4, indep 4(2), 4 indep 10 3:29 -- hung


5, 4, indep 4(2), 4 '' /\ not fixed indep 15 -- 8:02 -- failed -- exhausted!
5, 4, indep 4(2), 4 '' /\ not fixed indep 12 -- 8:50 -- 9:27 success!

5, 4, indep 4(2), 4 '' /\ fixed indep 10 -- 9:28 -- failed exhausted

5, 4, indep 4(3), 4 '' /\ not fixed indep 12 -- 10:05  hung



5, 4, pre filter 0, 1 fixed indep 10 -- 4:10 pm -- hung
    finger print

5, 4, pre filter 0, 1 fixed indep 10 -- 6:21 pm -- 6:48
5, 4, pre filter 0, 1 fixed indep 15 -- 6:50 pm -- 7:38 failure exhausted nonce space!


5, 4, pre filter 0, 4 not fixed indep 10 -- success
5, 4, pre filter 0, 4 not fixed indep 15 -- 5:28 -- 6:11 works consistently but takes a fuck load of time

5, 4, pre filter 0, 4 not fixed indep 20 -- 10:35 -- failure exhausted




sl = 4
p = 1 / (2 ** t)
  = 1 / (2 ** 6)
  = 1 / 64
  = 0.015625
  
edge_no = 20000
pass_one = edge_no * p
         = 312.5
pass_two = 4.8

Next col will be 325 * 20000 = 6500000 = we need a cluster
(1 + 1 + 4 + 312)
(1 + 1 + 4 + fix this)

1.0 / (2 ** 14)
00006103515625

20000 * 0.00006103515625

- 15 to be safe

"""