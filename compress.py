from params import *
from utils import *
from golomb_sets import *
from brute_force import *



def add_words_to_filter(words):
    # Build and write regular GCS compressed bloom filter.
    gcs = GCSBuilder(len(words), PROB)
    word_no = 0
    for w in words:
        word_bytes = word_format(w, word_no)
        gcs.add(word_bytes)
        word_no += 1

    table_path = "table.gcs"
    try:
        os.remove(table_path)
    except:
        pass
        
    # Save GCS to file.
    with open(table_path, "wb") as f:
        gcs.finalize(f)
        fsize = f.tell()
        
    # Read table into buffer.
    gcs_table = b""
    with open(table_path, "rb") as f:
        gcs_table = f.read()

    # Test words can be read back from bloom filter.
    fp = io.BytesIO(gcs_table)
    gcs = GCSQuery(fp)
    word_no = 0
    for w in words:
        word_bytes = word_format(w, word_no)
        assert(gcs.query(word_bytes))
        word_no += 1

    return gcs_table


def compress(sc, buf, usable_cores):
    buf_len = len(buf) 
    words = buf_to_chunks(buf)
    gcs_table = add_words_to_filter(words)

    # Main N byte checksum.
    fuzzy_chksum = mk_chksum(words, mk_chksum_bit, bit_no=CHKSUM_BITS)
    assert(len(fuzzy_chksum) == len(words) * CHKSUM_BITS)


    

    print("fuzzy chksum = ", fuzzy_chksum)
    

        
    print("Words no = ", len(words))
    
    # Todo -- change this to full buf at the end.
    print("Buf[:16] as hex ", binascii.hexlify(to_bytes(buf[:(CHUNK_SIZE_BITS * 8)])))
    
    accurate_chksum = Bits(rawbytes=sha256(to_bytes(buf)).digest())[:ACCURATE_CHKSUM_BITS]

    node_list, candidate_no_list = brute_force_controller(sc, len(words), words, usable_cores, gcs_table, fuzzy_chksum)
    
        
    return [gcs_table, accurate_chksum, fuzzy_chksum, node_list, candidate_no_list]
    


