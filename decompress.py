from params import *
from utils import *


# Not finished -- ignore.
def decompress(accurate_chksum, candidate_lists, candidate_list_no, nonce_list):
    # Generates every possible combination of edges
    # Lengthy = 22,000 hashes * 122
    match_list = cand_lists_to_match_list(candidate_lists, candidate_list_no)

    # Use special nonce list to cut probable path through match pairs.
    formed_chain_lists, checkpoint_list = compute_formed_chains(match_list, candidate_lists, candidate_no_list, nonce_list)

    # Throw away all chains from the results except the longest.
    longest_chains = return_longest_chains_from_formed_chains_list(formed_chain_lists)
    
    # Only keep the chain that yields a targeted checksum.
    data = b""
    accurate_chksum = to_bytes(accurate_chksum)
    for chain in largest_chains:
        if sha256(to_bytes(chain)).digest()[:4] == accurate_chksum:
            data = chain
            print("DATA RECONSTRUCTED: \a\a")
            break
            
    print("Done first.")

    return data

    
    
