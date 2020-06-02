from params import *
from utils import *
from shared_pow import *
from magic_filter import *
from compress import *

old_nonce_results = [[1365061047, b'\xb7-]Q', 0.25, 0.015625]]


# secrets.token_bytes out
rand_bit_str = "0111001111000111101010000010111101001101001101100000001110110001001011011110110100011110000111010010001001100011100000011001001100110000010010111001110101110010000100011111100011001001111011010110101011110110010100010010100100010101101110010010111001111001100100100000011000101111001101001110100111000011100010111101110101000001110111000001001111101000111110010100100101100011000011000100011010011100011100110001010001100010000000000010110000100111111100000111000001100010111001000101111001100000001101100110100111100101001101001011110110111001100001000011111111010010010000110010000000111111010111101010101111100101110011111101100010100001000010011011101011010011001100100111010001110110000000011011001110100000010010001010111100010011011101101110000100110110001010110001110111100100010010101001001001101100110111100111101101110000100101011001001100001011100000001110101011000010001000001001000101111011101100010000000000010011010000111010111111000110111101100001101010011011001101011000001101111100111000110000110010000111101101111111000100001000111000100001100001111110110011111010000011011001101101011111010110111010111111111100001000111111100100100100000000001011101110111001100001001110110000110111010001001001010101001001000100101001011011000000011001001100100010000011000001011100100010110101010100011011101110111000001011010011101000000100001000001111111001010100100110010100101100011110011110101000100100010110001111010000110111010010111111001000111100101010111000001100000010111111100001111110110000010111001001010100101000100010010011010100001011111011001101001101000000001011110101011000100111010011010111100101001110100100101000110111011100000010011010100001011010001101100101101101101010100110001000111100011000100100110111011110000101001101111001011000001100111111110111101010100111000111001101011101010000110010010010100101100100000000101100100100010001010010011100110001110101010110010000101110110010011000110110100001101011110011100111011110000100011000001011001011101110101000011011101111000000101011100011111010000101001110001010010101110001110110011110111000110001010110000111000101011011101001110110111011001000111111010110010010111011101011111110000010000010000010111010111100001110101101110010000011111010001101000011011100010000110011101110011001011001110111010011011001001011000101001110000010011001011001101101111101011100000111011100111110101101001010111100111101001110011001001111001101001011110011000100110011101000000011111001001000111111011101111110001101100011110110100001101000010010111111100011011101001100100011100010110011110111011111001111111110001001001011100000110110001101100100111111010101000011111101101111011101101111011010101100011000000101010110111000001000010110100010110011010100000101010100010100011100010110001011011101011001110101110011110111101111111001001010001001000111000011000010100000000011110101011011101000001010011111100000011100101101110101011100000101000100100011101011101011010000001010111110010010001100010101100110010101000001001101101101111111101011001001101010001001111010011010011111101000110011111001101111110000010101011111010110000101110010100110010101010101101001100001101100111110111101110011100101001100111000010110110100010011001111001111010100010101010011001000000110111001111001010001100100010000111100010101111111110011011010001011010001010100000001110000100101011110110001100101000001101100111010000000100000000111111010010010110000100010111001100101001100001010000111010101100001001010110100000110000011011111011100010111100010001100011100010010011011011100000101000111001010010110101110111001110010010100001110111000101100000010001010111001001100000100010111000110011110100000000101110101111110001111110111100011010101001110110111010101011101011101000000010110000010111000010111011111101001010110101100010100010101111100101101001011011110010100011110010010001010001110001001011110000010111001010101011010000001001011001100000111010101011000100100011110111000101000111101111100010000111110110101010101011001101001010010011111001000110101110101000001000010100101011011101101001100000110100000010101010101111010010011111011101010100110000001100111110101101010101111101101010010101011100011100100110101101111011110111001011011110000100011011101011010111100111010010111110101011011001001001011110111001000011100001000111011101000101100110110011011010110011111111001101100101001001110100000110110110000101111011100100010001100100011110010111110011110010011111011001111000101001110001001001100111010001110110111001101010101100101000010000101101101001001100001111001101100111111100011111000110110111110100110110010110001100110100101101010011101110000010011001000100001001011001101111100101101100000110000000111000011111101100110010101011010011011011111101111010101111000111111110111000100001000110110011011011111001111000001010111110101111111001101101011011010100111101010000110000011010101011011100100000110101111010111000001100000010001000001001110100110010010000001011000101001011100101001010110011001110110101001000101101010001101110101110110101101000001001000000100010101101001010001001011011011011110101100010101001010100110000110100101000010001100001011010101000010101100110100101111111100000011001111001010100011001110010001110111011000011111100011101000100110100000011100101110100101010011001100111000011011001111011000011110101111110110110100110110110111100100010110011101010000000100000100011101000101110100100000111111101001101111100011000011110100010000110111010110110110000000100011100011110110001010000101010000110000010001010100010010101111011010111100111100110000001100001111101100111110111101110000001001100100000111000101100100011011101011011101100011001100111110011001000101010011110111000000100101101101010011111111010110010101010110100100000011000000001010010101100010010011111111010001100100110101100000110011010001111001100100001110101100101011100100101110101101110010001010000100100100000001101011001111000110100100011101001100101100001011011000110000101101101110010110010011101011011001011000111110000111100111100111010101010001000110100010000111110011010111010110100010101010111111100000111110001101001011110011100000000111111011011110010000110110110011111110001010100110001110111011100011000011110011000110111000100111011010101010111101001100000110100000100001101111001101001100011101000110001101110110110010100010000110011011010011010100000101100111100111110110110110000001001001010100100010000100000100100011011011110000011001101001000100010000101000101111010001000001010101100111011101001100001101010100111000000110101101000010011010001001001011100110001010001000101001111000001001011010101000001101001101110011011100000000111100000011110100110010010111011001000101001001110110011000100110101000001001010000001110011001100001101001011111111100111111000110101010001010111011101111011000100101100001000000100100000011101110000100110100010001000111111111110111110010001011101101101101100010011010001110111001001101010011001111000010010010100101110010011101011010000110110111011001111010000010010111010011110110111100001111100100010111101100100000111100100000100111111100111111100010101011100011001101000001001011001111010110011001010101000010101100010000011001110111100000111101110000011001011010110100001001100001010000110000010110101100110000000010110100001111101011111101011101011001011000010101100100010111000001101000011010001010101110110011010001100000101100100101111000011101111001100101100011010110011110100110011011100000100010100111101110110100110001010100011101100011100010010101101000110010100011101000000110001101111110001110001010110110011010100000001100011110100000100100010111100100001100001000010011101001000000111101010010001111010011000100100110110101111010101010100101001110010001110110001101011100101101101111111000100000100000110001100010101001100011011000000010000011100000101011101011010101100011111110011010110001101000001110010111110011000000000110111001011011011010110100010100111000100010100011101101001101000000100010100110100101011110000110010011001001111110101101111110011111100000010001111100010110101110100110000011011100010011111000011101001000110010011001111110100101011110101111000010010010110001010010101001000101100100110100010010001010011101110010011100"




assert(len(rand_bit_str) % CHUNK_SIZE_BITS == 0)



test_rand_bv = Bits(bitstring=rand_bit_str)

assert(len(test_rand_bv) % CHUNK_SIZE_BITS == 0)




#TEST_BUF = hex_down()

TEST_WORDS = buf_to_chunks(test_rand_bv)

#print(choose_best_nonce(old_nonce_results, TEST_WORDS[:POW_SET_LEN * 2]))

#exit()


TEST_GCS_TABLE = add_words_to_filter(TEST_WORDS)

print(len(TEST_GCS_TABLE))

print(WORD_NO)

print(EDGE_NO)

exit()

test_sc = get_sc()


"""
gcs_table, accurate_chksum, fuzzy_chksum, node_list, candidate_no_list = compress(test_sc, test_rand_bv, CLUSTER_CORE_NO)

print(candidate_no_list)

print()
print()

print(node_list)

exit()


print(AVG_BLOOM_POSITIVES)
print(AVG_EDGE_CANDIDATES)

exit()
"""


candidate_no_list = [74, 64, 59, 63, 55, 63, 71, 57, 64, 60, 70, 77, 68, 52, 71, 56, 63, 73, 72, 61, 65, 71, 58, 73, 72, 54, 62, 57, 70, 66, 61, 70, 73, 68, 83, 59, 58, 73, 70, 64, 68, 65, 69, 74, 70, 54, 68, 61, 65, 66, 56, 69, 68, 65, 56, 62, 58, 60, 64, 56, 58, 53, 68, 67, 73, 57, 64, 66, 63, 76, 72, 61, 82, 62, 53, 52, 78, 68, 63, 68, 65, 63, 57, 74, 56, 69, 79, 75, 68, 60, 74, 76, 71, 60, 70, 69, 74, 50, 68, 70, 61, 62, 73, 56, 62, 63, 64, 75, 78, 60, 61, 76, 73, 65, 68, 69, 61, 60, 69, 76, 64, 81, 59, 72, 72, 75, 63, 51, 85, 61, 59, 64, 71, 66, 72, 63, 57, 71, 75, 64, 65, 65, 60, 57, 75, 61, 79, 46, 67, 69, 67, 55, 58, 67, 75, 65, 51, 57, 66, 59, 50, 64, 57, 63, 74, 53, 51, 63, 60, 66, 64, 60, 58, 77, 77, 63, 63, 54, 73, 71, 68, 61, 83, 70, 71, 75, 79, 76, 72, 68, 71, 68, 58, 75, 64, 57, 57, 64, 82, 65, 60, 45, 73, 68, 63, 61, 75, 56, 62, 66, 72, 72, 77, 73, 77, 66, 54, 60, 70, 71, 69, 62, 69, 71, 50, 57, 63, 68, 60, 67, 66, 76, 56, 68, 63, 65, 75, 72, 70, 71, 58, 76, 71, 73, 71, 58, 63, 72, 77, 84, 61, 61, 66, 60, 67, 62, 65, 72, 64, 55, 69, 59, 66, 80, 63, 67, 67, 59, 73, 71, 70, 68, 65, 55, 63, 68, 59, 58, 59, 64, 66, 72, 72, 63, 69, 63, 66, 66, 58, 60, 63, 60, 84, 73, 72, 64, 58, 69, 63, 66, 61, 75, 65, 62, 60, 61, 79, 58, 55, 70, 74, 74, 64, 62, 68, 69, 61, 64, 51, 68, 62, 76, 72, 64, 68, 65, 67, 60, 67, 60, 61, 60, 70, 65, 62, 72, 85, 59, 50, 68, 65, 58, 61, 60, 54, 56, 54, 59, 61, 51, 71, 67, 70, 71, 55, 72, 61, 65, 64, 60, 59, 61, 48, 61, 66, 63, 71, 63, 65, 80, 66, 82, 73, 68, 54, 75, 68, 61, 56, 67, 82, 56, 68, 73, 62, 72, 48, 53, 56, 65, 57, 59, 59, 62, 64, 78, 66, 61, 72, 55, 56, 60, 67, 60, 65, 62, 47, 52, 63, 68, 57, 69, 69, 72, 53, 72, 62, 64, 76, 50, 68, 65, 70, 66, 75, 68, 67, 72, 63, 64, 70, 55, 68, 67, 80, 75, 59, 65, 62, 79, 63, 73, 61, 75, 66, 61, 67, 71, 68, 64, 58, 63, 82, 66, 60, 73, 57, 62, 60, 63, 59, 67, 65, 61, 54, 60, 61, 69, 61, 68, 83, 63, 72, 63, 69, 57, 67, 66, 80, 64, 62, 46]

node_list = [24, 20, 17, 6, 46, 55, 38, 46, 17, 52, 63, 24, 26, 6, 18, 40, 9, 62, 13, 7, 15, 14, 42, 22, 2, 0, 29, 30, 19, 3, 25, 24, 38, 46, 46, 58, 17, 10, 27, 40, 27, 25, 10, 39, 8, 21, 2, 13, 29, 11, 9, 23, 2, 30, 0, 47, 55, 13, 4, 4, 31, 9, 37, 29, 64, 52, 63, 65, 0, 30, 46, 8, 49, 49, 8, 27, 51, 30, 48, 10, 57, 10, 38, 39, 5, 66, 51, 2, 35, 51, 34, 52, 15, 5, 11, 65, 27, 42, 34, 55, 42, 28, 32, 20, 14, 52, 48, 8, 33, 21, 22, 70, 14, 12, 54, 63, 12, 20, 46, 33, 59, 45, 47, 5, 66, 31, 24, 20, 2, 26, 32, 13, 56, 30, 59, 41, 33, 16, 60, 63, 62, 11, 16, 26, 11, 60, 17, 10, 49, 34, 10, 52, 10, 27, 21, 30, 45, 19, 25, 9, 44, 26, 23, 51, 66, 33, 39, 1, 44, 65, 39, 4, 53, 1, 10, 16, 12, 41, 37, 17, 20, 29, 31, 27, 30, 50, 15, 58, 18, 46, 59, 20, 10, 46, 33, 46, 11, 15, 67, 0, 13, 23, 5, 47, 15, 60, 47, 5, 1, 23, 37, 28, 0, 36, 62, 1, 47, 2, 60, 50, 36, 60, 29, 49, 6, 20, 34, 48, 19, 17, 23, 17, 16, 6, 19, 29, 63, 40, 63, 56, 23, 64, 1, 59, 22, 28, 56, 60, 39, 40, 20, 29, 46, 17, 27, 58, 15, 58, 42, 11, 36, 37, 40, 25, 50, 7, 10, 48, 71, 55, 9, 24, 22, 31, 11, 1, 48, 44, 45, 37, 4, 31, 7, 62, 31, 2, 19, 50, 5, 4, 20, 22, 28, 61, 40, 42, 9, 53, 50, 26, 17, 6, 18, 23, 0, 13, 10, 57, 29, 20, 57, 26, 59, 42, 35, 36, 8, 37, 34, 6, 55, 0, 66, 43, 8, 33, 63, 4, 51, 8, 18, 28, 14, 27, 49, 54, 30, 9, 6, 9, 23, 8, 31, 26, 34, 2, 0, 51, 54, 18, 52, 11, 29, 68, 24, 4, 26, 16, 13, 25, 28, 37, 46, 5, 50, 51, 47, 21, 33, 41, 34, 27, 51, 10, 51, 42, 28, 22, 24, 33, 26, 45, 2, 0, 9, 27, 8, 5, 1, 27, 40, 41, 6, 11, 2, 60, 37, 58, 11, 34, 16, 27, 15, 59, 9, 50, 38, 24, 6, 66, 47, 3, 65, 69, 39, 1, 61, 51, 21, 40, 14, 51, 65, 49, 36, 8, 2, 37, 29, 10, 60, 11, 12, 26, 38, 56, 38, 3, 60, 55, 33, 28, 2, 55, 30, 23, 36, 6, 64, 49, 11, 45, 53, 59, 7, 4, 3, 9, 4, 49, 57, 14, 31, 12, 16, 25, 57, 6, 19, 45, 66, 48, 11, 45, 19, 17, 64, 26, 54, 8, 14, 41]

assert(len(candidate_no_list) == WORD_NO)
assert(len(node_list) == WORD_NO)

edge_hashes = [b'\xca\xa5\x1e\x0c\xdf\x1a\xda\xa5o;\xf5<}\xcc\x90\xb3\xffSf\xe9', b'\xf6\xff\x90&\xdb\x1f\xe1\xa3}\xc8\x8a\x9dr\x9c\xa1\x03\x07\x1b\x17f', b'\xd0\xa1\xaa&f\x9b\xc5l\x8a\xd4\xdd\xbe\xbb\xdb\xabe]\x9d\x11\xe7', b'\x17\xb38\xca\xee\xb9\xbe@\xe6\n\xe0|\x8e\xfa\xae{6\xe1O\x80', b'\x1d\xbd\x03\xd0\x91\x1c\xd03r\xc4\xac\xb6y\x00\xf0PW_\x01_', b'\xe6\xcc?\x91\xe6weI\x86\xf6\x87\xf1p=\xf1\x0e\xdf<\xfa\xce', b'\xc3\xcf%uESv\xa0X\xbf\xa4\xb9k\x8b\xe1p\x83\xc4\xad\xf3', b'N\xc5fc\x94\xe7\xbb\x9f\x9e!\xb2\xce\xea\x87/\xdc\xeduPe', b'2\x11\xa2\xaa\x0f\t\xab}Dm\x83L;\xaa\x8b\x01\xe4c\xd11', b'\xc6`\xd6\xb3_4\xaam \xfc\xf8\xab\xff\xb4\xcb\x05\x91\x1d\xfb8', b'li\xbc\xf3\x88\x01\xf52\x8f\xba\xcd\x10\x0f\x1f\x88\x0c\x1f\xd5\xccz', b'o\xfb\x8b\x14\xab^(T\xa3\x8eC\x13\xa6LH(:D\x8a^', b'"p\x87E=\x01\xff\x8e\xbcQvZ\x04\x81#\xb4\x88S\x0cj', b'\xd5\xf2x%\x93\xc0DG\xc8a\xe5\x7fK\x00#\xdc]\x95\xb1.', b'\xf4\x1c\xd7\x13\xf6VZVc\xe8\x08\x12\xa0\x9f\xc5\x19\xbb\x9c^\xf0', b',9R\x9a\x0c8t\x1a\x9a9\xeb\xe9\xfd\xa7 \x16\xb4cH\xdd', b'\x89\xd4\xba\xca\x98\x17\x86/T\xb4\xf6\xbd\xb626u\xca>\\c', b'\x94\xda:^!\xbe*"\x02\x18"\x9bwUHd\xe6\xd9\x17\xb0', b'\x15p8)-\xece\xe6\x03-\xa2\x82\x9e\x82\x91\xac%\xab\xb0\xae', b',K|a\x95W_w\t\x9aP\xb3\x9f\x92\xab\x17b\x8eA\xa1', b'q>j\xf6\x0fr:\xbeX\x87\xdcr.TL,\x99\x12\xda\xc9', b'*\x9a\n\x9cS\xc7\xb6\xa5\xce\xf1\xeaC`\x13\xb8z\xd6@\xf1y', b'I3\xa8\x0c=\xef4}\x9e\x0e\x86\xa7\r}\x0fK\x98^_J', b'\xb9\xe1\x8aTS\nJ\x9f-\xa1Jb;k\xddZ \x86NQ', b'\xd2#\x8f\x08 )\xe4\xa6UU\xcbn5\x15\xa5k\x9f\x98\xde\x92', b'\xf8\xc0\xb1\xf1\xf6\xeb\xd0\xc4\xa8\x89W\x1f\x12r6\xf4\xca\xb4\xb9\xe1', b'\x8e\x06u\x8f\x03\x1c\xfd\x1e1p\xad\x01\x1d~\xee[\xbd\xa9\x12\xf5', b'L\xe7JF;\x03{\x08r\x023\xa5*\xd1\xe0\x0b\xbc,\xc4u', b'\xad_&\x92\x8dm#\x0b\xff\x14\xb7>Y\xaf\x94\xc4\xc2\xbb\xd2\xbc', b'&\x10\xbb\xf1\x82\xfc\xb1\x1c\x1b\x9e#\xde\xabz\x07\xfa^\x8e\xe4\xf7', b'\xa2A\xa7N_\xa6\xb387\xb5\xcaN\xf9\xe3y\x1eb2.B', b'r\xc9\x90\xa0V\xfb\xad\x03\x96T\xb1\xe4\xbfm\x9a\x8e\x9a\x15\xc8\r', b'\xacH%I\\\x8eK\xe6\xc8\xae\x93\xabU\xe3\xa5\xaf\xd0\xee\xb2\xe0', b'\xaf6\xf08\xb8\x0746\x83\xc1\xf4\xac\xb50\x0e\xad\xfe\xb8s\xf6', b'\x98H\xe0\x8c\n`{\xfd\xab\xc4E8\x9b\xf0\xafQQ#\xe8(', b'\xd8M\xc2/N\xd1|\xd1\xcao*!G\x9a\x85\x002R\n]', b'y\xdd\xfb\xb6\x08\xaf\x93\x94P\x82\r\x9bc%\xa2\xde\xee\xba^\xbe', b'\x8a\x90\x82\x88\x0fV\xbfE\xd0}E\x94\xebSB\x84\xea\xb8\xb6\x18', b'\x9b=\x8c\x99\xdd\xd7\xec\xcf\xe94\nt\xa2\xae\xf9\x00\xc0\x05S\xca', b'\x8a\xfa\xb2\xd65\xad\x0c\xa2\xd9\xe2\x8c@\xde\xc2\xd4^\x19\xa9\x8fC', b'2\x80\xe6\xb5\xdb\xfc\xb7a\xee\xac\xcc\x00\x9e\xabu\xf7F\xd8\xb5\xcb', b'\xe6\xb13\xc2\x14F\xe8\xb8\xfb\x8aQ\xdb\xf0^Z\x8a\xf3\xa1<L', b'\x02\xb6W\xc0\x01\xca\xe0\xdd@A\x00\x0f\x12\x98O\x02\x93%\x1b\x18', b'\x86\xf7\xe0\xb7(\x05\xa2\xedc.>W\x1f\x16\xd0\xc5\xbb\xec\xec\xb7', b'\xa6\x84\xee\x13\x8c\x03[\x0b\xdc\x0e\x0e\xee\x94\xaaf\xbd\x82\x8b\xf9\xe7', b'\xb1\xc9X\xe3\xf4_\x1f\xea\xbe\xc4\xfa\xe2\x85@o\xc1\xb8\xee\x95P', b"\t'u\xb3&mH\xe5\xe7 x\n.\xa0\x0c\xc2Q\x89\xab\xec", b'\xcbw\xc7\x8awH\x8f\x13\xb2mh\xc0\x86;\xcc\xbbk\x846+', b'\x8dn^Kf\x9f\xbd"\xad6\x91_\x0e\xc3\xaaB-Yn\x82', b'ecX\xe2\x1c\xb0\xc6[gGa\x91U\x02\xeb\x1f5\x0f2h', b'\xca\xb7\xaf\xe3\x1d\x8f\x13I\x13d\xc4\xa4}\xd7\x10\x9dK\xfb\xaf\xec', b'\x13X\xf0\xbe\xa5\xd5\xabe\x7fic\xae\xcd\x05\xe4\xb9\xe4\x1aBi', b'#\x98\xdaiF\xae\xf0*){\xd7J\xf9\xa4\x92\x88\xd1(OY', b'JQ\xd7\x8c\x9f`\xbb\x12\xac\xe3\xbf]\x14\x1eb\xacUj\x95f', b"0\x95,\x1c\xc8\xe2\xac\xfc\xa7h'P\xdc\xcf\xcb\x863\x1d\xf2K", b"\xa7\n\xaf'G\x9d\xff\xca\xd6z\x94\x11z\x95Uo\xc8\x89BG", b'\x90\xe3:\xff%\xc0\x05\x91\xaeK\xc9\xfdT\x1e\x0e\x16\ni\xe0H', b'\x04W\x02ve\x1bc\ti\xb1\x0cAY\xd1\xa4\xb5+)9\x82', b'P\xa4\x8d\xd4;\xeb\xeftU\xfa\x0c\x1a\x03C\xdd\xe3\xa7\xdcp\xd8', b')e\xd6\x06Q\x18\xf5!\x9d\x12H\x91\x0e\x02\x11\x03O\xc5\xa8\x88', b'\x07\x93>!\xc8\rDy9\x8d\xf0\x95l\x15\xef\x88\xc1\x19\xd3Q', b'\xf4)UN\xb1_\xae[\xc8\xd2\xe2\xb5q\xfb\xdb[Z\x91\xe6"', b'\x97\x18\xa6f{C\x986\xcf\x99\x01b\xa0\x7f\xbea\x03W\xba\xd9', b'x\xe0\xd3\xf2\xd2\x94\x93[|\xa8\xe8\x83\xce\xb4jc0\xbe.\x8f', b'\xf1\x12\x98\x0ck\x8c\xc0\x01\x804\x8d\xd4\xa3\xffV\x02\x80\x94\xf3A', b'\xe1\xd4\xd8\xe8\t\x81\x88\xbb[\x19S$\x19o\xb0YLTR\xa2', b'e\xbb\x1c!\x9c\x0e\x88\xfa\x8a\xe4_X\xc2\x8d\xd7\x17\x05\x03\xa57', b'\x18.U\x1f:\x89\xab\xf9\x1c\xd2A\xa6\xcb\x90\xc7\xd1\xa3L\x11\xe7', b'\xe4u\xe0f\xf1\xf5\xd5\xd7\xaf"r\xfa7\xb8\xd4d\xf7\xcdF^', b'\xb1D4\xda\xb7\xd6\x8e\xfa\xdaM*\xe7\xf0\x87\x07VD\xff;w', b'\xa0:"\x17\xa3\xdb\xfc\xb4\x98W\x08\xe9r\xd1c\x82d\xc5\xb4\xfa', b'\xb1G\x18\xce\xcf/\xe0V\x1d\xd1\x87\xfd7Y\x80\xcdSO\xfe+', b'\xebI\x9f\nBz\xda\xf3K\xb5\xf6D\x85*I\x10g\xcdf\xb6', b'>4H\t\xf93\xdbGZ\xbb\x13\xf0\xb8\xb4G\x81\xb7\xfd\xfe\xdb', b'\xf4a~\xf4\xec\xac8H\x8d\xc3^\x8d\x00U\xcc\x80\xb8<\xa3\xb5', b'\xd3X\xf1\xfc\x95.\xe2A\xaf\xd5H\x88I\x9b\xf8\xbd\xdej\xd4\x08', b'\xce\xf0\xae\xab\x08\xb3\x1b\x8e\xccZ4\xd0\xb1\x84;\xfb\x84\xab\xf9\x83', b"\xa8\x8b\xe6\xb7\xb8\xa9\xb1>\xbd\xcf\xcfx\x97(\xea'b\x82\xbfM", b'm\x02\x05o\xdf-\x7f\xc8c\x17\x02\xf6\xdby.]\x02\xb6]\x7f', b'\xa9\x05\xceB\xf5n\xf7\xfe`\\\xab\x01\xb7{\x03\xa1\xda\x05\xb4\xe3', b'\x7f\xf3\xc6dEc\xb9Q\x9d\xe2\xf1\xb9\x17"\xa7p~\xf8\xac\x82', b'j\xed\xe7"\x9f\xfc\x8c\t\xec\x08V\xfa\xa2\x9a\x88O%g\xc4\xbe', b'\tq_\xd2kqd\x0fl\xbe\xd1XD\x03\xa9\x8e\xbd\x92&\x02', b'\xed~\xb3\xff@G\x97\xa8ca\x16d`\x8d\xc2A\xcfK\xdd\xeb', b'\xf2k\x0e\x8dj\xe5%jll5-\x8d\x1c\x9f\xf8\x8c\xba\x8d\xb5', b'7D\xe9\x909wD\xe7\xd3\x94\xe4U\xd4\x0c\x85%\xf5\xe1)\xce', b'\xc8gY!\xb9\x8f\xb3\xb1$\xe8\\<\xfe\n\xe5\xa1\x12P\t\xf7', b"\xb9\xb0\x04S|@/\x88x\xba#BW\x01i'\xf1\xb6\x1aA", b"\xcc\x87\t\x97O\xd7#\xd89\x0bS\xd1P\xf9\xed\xa5'\xbeRa", b"\xe9\r\xff\xa5\x0f\x16\xd0\xbd\xed\xe4\xb7\x7f\n\x84\xaac\xe0\xb4\xd3'", b'\xa4\xb8\x88\x9e\xd7k\x9c$\xe4\xb4\x04\r\x87\x9arC"\xbb\xa1\xa9', b'\x0b\xc6W\xfbU\xc4\xab\xa6\xdc\xeeB\x06\x90\xe1i\xc8RM;\x04', b'\xfd\xd6\xb4\x8d\x18\xbb\x1b\x114\x05\xfeF\xa7\xd3\xae\x83\xb6\x83\xc3\x8e', b'\x9e\xcf\xad\xa2:8\x8aWOQ&\x14\xc4A\x94\xc5Y\xacz|', b'#<\x83\x14\xa3\x16\x12\x83D$l9\xbf\xf5\xaf\xd3\xe3\x83n\xf3', b'\xdb\x08\xbe\xb5j)\xe6O,\x9c\xf0#\x98/<j\t\x9b6:', b'\xb9\xd9\xe9\xe6C\x87\x88\xc8\x15\xd6\x1d\xba{\xb41+\xffk\xcc\x1b', b'$\x01;.a\x97$\xf5Ko\xaf>\x82\xe4\xe6\x149\xab\x97v', b'\xdc\\\xc8\xeb\x85W\xa9\xcc\xa0\xc7\x07\xbd\xa3;\xe8\x8a\xb9:\x8b\xb5', b'F|\xa1>>\xda\xe9j\xed\xc0v\x8cuh\x08\xf6l\x13>\xc3', b'\xb2\xe8y\xfd+\x9dj\x00?\x9c7\x9a\x15\x10\xce\x04Q\x1e\xb3\x91', b'_\x98\xaf\xdc!\xf7S\xe9\xa9\xd4\xf0\t|\x8aH_T\xbe\x82\xd4', b'\xa5\x19\x89bl\x0e#\x8c\xd3p\xca\x9a\xfdK\x1a\x86w!\xc1l', b'\x15\xc7\x0f\xc5\xaeuq\xce\x8a\xe3\x07\xd8\x19{\x8aI0\xa3;\xd1', b'Z\xe4k/ILoa\\\x80\x05\x102\x95h\n\xdf\x84\x94a', b'Q\x7f\x82\xcb\x9e\xac\xd5\x91b\xf5\x96\xe3\xd9M\xaf\xaaDF\x08\xa2', b'\xec1\xc5c\x84r\x98\x98jr"\x1eG`\xa25J\xce\xfb\xac', b'T\xa3[\x9c\xc6\xff\x11\xba\xb8\xdc\xc8\xe5\x90\xdc\xd7\xd5\x91\xf9\x90\xe4', b'\r\xc4\xc3\xf1\xf5\xeb0\xd5L\x05\xd0\xdd@=e\x9dj%\t,', b'\x87-\xb3\xb8a\x96\x95\xec\xe3\x83\xff\xb29\xc8N]\xae\x10ts', b'\xb5\xfc}\x7f\xfcv\xd3\t\x08\x92\xc9~\xe3\x17\xff}p_k"', b'%\x7f\x0e\x92ky%\xbc\xc7{u$\xd1m\xd0\xc6n"Q\xe2', b'\xb9\xe5\xd3P\x05\x96\x15\x02P\x96\xbe,\xd07fq\xba\xa0\x95a', b'x6n\xd9\xea\xdd>\xb0ZX\xf4TC\xc9\x05O^\xf8D[', b'\xee\n\x86\xaf\xc8*$\xf1\x08\xab\xc3\x8de\xc1\x02l\x08\x0f[\xab', b'R\x8e\th\x0b\xca!\xe6\xe2a\xa5\x85,\xa9\xed\xa74\xe1I\x05', b'"\x16KM\x0c!\x9d\x01\xa1t\xf2\xf4\xfd\xbc\x0b\xbd\x93a\xd1\x07', b'@\xc5\xeeg\xc0N\xb7\x18P\xb4\xf8\xa9\xce\x98\xd7\x98e> 6', b'%H\x0c\xc3\x12u\xa4#\xbd\xd6\xf8\xf7\xba#\xc6_>\x06\x156', b"\xd5.\xd8\xdf\x11\xbf\x8c'\x0f\x13A\xec\x0e\xd6\x8b}\xc5\rmr", b'\x1c\x1d7\r\xf7-p\x11\xef\xad\x00&W)Z\xc6k\x13\xae&', b']xxLz\xf7W\xbb\x88\x89\xee\xd4e\x15W\xe5\xafr?\xa5', b'\xb7\xa3OT<\x18=\x16W#\xd2\xdd\xbd\xd0\x1c\x98\xcd\x91\xc1\x95', b'XV\x8d\xf8\xff8^D\xc5k\x9c\x08:\x90\x84\xaeE\xb0,w', b'\xf4\x893\x0e\x8e\xf8\x83U\xa16<N\tp\xb7\\%\xaa\x95\x16', b'j\x1d\xado\x91&W\x12Q\xa4t)\x07\\B~\xda\xa4\x85\xff', b'\x82\x04\r\xd3\xed5\x18\xeb\xcb\xdc\x036\xa2Wr\xf2\x7f\x12\t\x1d', b'\xb3I=\xc2\xd4,\x89/\xf7Sz\x04\xee\x1bB]\xb7V5\xba', b'\x1a\xe9\xb9\xefh\xb6\x18\x7f\\\xa9\x14\x01\x11\xf9-\x0b\xc1\x0cj\xc7', b'\xd4\xea\r\x8e\x08\x06w\xbf\xa2:\xd1y\xa1$\x14\x7f\x94\x13oc', b'\x1e\xcc\xe7\xbflN\xb3\x08\x1a\xcdo\xb2\xbckY\xb61%\xdcG', b'\xd1$\xads.\xf9>\xa0\xd1\xce\xf9\xa3s\xc1\x1c\xd9:\xe7\xf1\xcf', b'6/\xb1\x04\xe3}\xc2\xc4\xb3\xc6\x98X\xc54\xd0\x83\x02\xa0\xfd\xe8', b'Q\xf9uP\xe8\x92\x1a\x1d\xcd\xa4\x0f\xf5u^\x87n\xf3\xecR^', b'6\xe1h\x9f\x9d\xd8O\xa9\x1d\xef\x8eq\x16\xd6_R\xdc\xe9\xf7T', b"rJ|o\xa2\xd5N~\xf2\x84B\xd0^\xbf0*,'\xb7\x9d", b'\rE\xbb\xe3\x87\x07\xbeo\x05\xe0\x91)lX\xf2\x84\xbc\xd7L\xf2', b'\x8a\xb4i\xcf\x06\xaf(%c\x9e\xbe\x93O\x02-\xfd\x88\xa6\xc39', b'g\x8d\x98w_%\x9f\xe8 \xaa\xb8\xc6\xc2\xd3\xb3V]\xb2T\xba', b'\xdf\x98\xd2U\xe1\xdbN\xedB\x89$\xc6k\xecqR\x1f\x12|x', b'\xb8!\x1d\xe2\xd7\xe2D\xa1\x14\xc7\xf0q\x10\x86\xaf\x10&&u\xce', b'\xe8#^w(8\xa1\x1c\xbe\xb6a=d\xab\x81\xb1\xf5\xb4\xc5\x92', b'\xb6\x86%x\x1ai_\n\xe0\x16\x83J\xe8\x81\x0e\x91Cr\xf3\xe9', b'\x05\xae5P\xbfg\xa3\x84\xecc\x11I\x00`\xe2\x95\x11\xe39\xf4', b'\xeew\xd4\x9b\xdd\xfe\x8e_\x96\x07\xb7\xda*H\xc8\xc2I\x06R\xfc', b'0\x9a\xcd\xef\xaeP\xfd\x03L\xbd\xf0\xa27G=z\x8c.\xcc1', b'EX\xe3\xe7\xb7\x81*\xa3\x12\xef\xfbBr|=\xbd\x98\xed\xaf\xea', b'\x1b\x0c\xc7F\xb8S\x7fQ\x0c\x1b\x00%\x8a/\x08\x8a\xdd\xdfeL', b'&d\x1cr\x91\x15\x92\xcf\xf3\xb7\xab\xf2M\xfe\x0c\xd4\xdc&\xebm', b'\x00^<\xe2\x8c<er\xb6\x02\xd2\x84\xcaH\xe2\x14.7\xfe\xd6', b'[\x93\x9d\x03\xf25\xad\x06W\x12\x15Y\xa6\x00%\xb4\xdeB\xba\xa0', b'\x9b\xe7Q\x93\xc2\x13\xee\x0cT\xb6\x84\x0e\x0c\xa4\xbd!\xb4\x051\xd0', b'\x12\x96\xbb\x15\x9b\xad\xf9\xa4\x85\xee\x80\xce\r\x1d\x18O\xe47~>', b'\xf4Iz\x82\n\xac2\x15o#[\xf9\xe22E\xaar\xec}[', b"\x89\x17\x80\xdf'\xfd-h\xf7\x88\x8e\xfe\xeeC\xd7^\xbb\x9a\xc8\xea", b'\xe8\xc0\xbd\x8aM\x8ctN<\xd1\xbc\xb6J\xdf)iz\x9a\x1f ', b'x{\x98dS\x8bL\xbf\x03vX\xfeU\xb9\xba\xc7\xea\x17\xebp', b'B\xf7\x83\xa6\x0fx~[\xa3\xbfK\x14\xde_dZ\xdc\xfb\xb0\x9f', b'\xdb\xe6Z\xd9&Qi\x1a|\x1cY/\x80\x91L\x1bk\x8c\x7f-', b'\x1a\x0f\xd8%\x9e& \x1c\xa3\x82L\n\x14\x13\xb69\x05\x07\x90\xd9', b'33\xafT\xfe\x90\xe3\xfd\x9es\x06\xd1\x9b\xd20\x8e\xd9\x90~\x10', b'\xd05\xfcw\xd04?00`\x1c\xbd\xbdb<\xe9\xf9\xe0\xaf\x06', b'\xf4\xb3eq\x04\xb4@t\xcd\xa7\x0e/\xb85\x8c|\xb9\x12\x86\x90', b'\xa2\xd8\xddeY\x1d\xdf\xdd\n\xf4O\x1b^p\xad(\xa8\x0cl\xb8', b'\xb1\xb8\xb1\x12\xc6_/;@JGA\xf8\x02\x004}\xd4\xe6%', b'!)\xbeNM\xf3\xcf\xe4\x14\xce\x13G\xef@\x82+\xc2\xd0k\xd0', b"\xb9\x8c\xae\xc9Z\xf2\x035\xb0q\xc0'(\x0f\x98\x07\xe9m\xdeN", b'\xe3\xc1\x12\x0b\xcb\x963\xdf#\x03\xb1dj\x06~\xac\xe5\x15\xc4\x9f', b'\x06\xcaQ\xd2K]\xee:\xc1\xea\xac\x91\xbc2\xb4\x14\xf1\xc8A\xfa', b'\xef\xb3\xa27:\xb7\xf4\x1e\t;7\xf7z\xbb\x02\xf7\r\xd5Z:', b'v\xea\x10\x01 %f}\xb1/\x02g\xc7jih\xa5+U\xad', b'\x10\x00d\x95\x03\xda\x94z4\x87\xe3Y\x0b\xbc\x7f\xa9\x08\x10\x99\xbf', b"'[\xb6=\x91\xf8od\x8f/\x0f}\\\x1d\x12-\x14}\x87\xbc", b'~JS\xf8Hgz\xe9L\x87\x86\xa1|\xe1i\xa8\x04\xb7E\xdc', b'\xf2\xc6o\xb9\x16\xfd_\xfc\xdb\xe7Yn\x05f\x11\xc1\xff\xabQ\xd7', b"rz\xdc'\xf8\xe8\x9f\xbeG\xbf%\x90\x89\xd7\xb2\xe7\xa5jx\xc9", b"\xac\n\xf0\x9a6D'<\x08R\xf78\xb5\x7fTQ\xee\xadae", b'p,\x1b\xdc\x10\x80\x03Gc\x13\x1e\xf5\xb6\x83\xce\x8c\x8e\x95\xdcA', b'q/|\xdc\x181\xd8\x12\x86\xd7p`\x8do\xb0\xdb\xc2\x08\xac\x94', b'\xfb\x1b(\x12\ry\xed_\xf5\xa1\xf0\xfd\xc4j\x97"!\xbc\xa4\x15', b"f\x00e\xbeF12\xe8\xfe\x17T\x06p_t{w'\x10\x03", b"\x83\xf6\x88(\xa8\xb5\xf0\x98\x8aa'y)\n\x94\xab\xa2\xfd\x022", b'~\x81%\xc8\x13=J\x9c\x8c\xb1\x8c\x1f\xad\xde[E\x06&\xa6\x8d', b'S\xf1G\xc8\x81d\xca`L\xf5R\x89\x19\xbc\x0b\xdb]\xc9\r[', b'\xbf}\t\x81\xa1 Ce\xc3\x824K\x89%\x93\x96\xdc$\xbb\x8a', b'\xe00\x18rE\xa5\xd3v\xbd\xfeQ\xcf\xb5@\xf4N\xac\xe2\xcd\xe3', b'\xee\xaa]\x88:(\x0c5\x1b\xa6\xbf6\x94\x03\xc3\x03\xee\t{B', b'\xa3B\x83A\x8e\x99\xc1;\xe2\t\xe2ca\xa6>{\x84V\x99E', b'G\xc2~\x0c\x83\xd4L\x9a\xb4\x067\x10\xa6\xc0\xf1\xff\x0ci;\xa8', b'}\xc3\xb5\xa3-\xb5\xcc\x99\x92/\x9c\xa16\x1eX\x13\x10@\xe6\xbd', b'\x1a\x10b\xff\xfd\x974\xbf\x87\xb7j$xM\xd8\xfbj\xbdb^', b'lb\x93F\xdcFVBB\xe9R\x89|)7\x8a\xafT\x91|', b'\xb6\xd7\x11\x80\xc4\xb6\\\xbd\xbeY\xe9Cpy\xbd\x92\xcf\x92\x0bG', b'\xd71\xf8\xdbq0[\x0efj\x1d;\x9b+T\n\x9a\x0e\xf8\x1e', b'H\xc7\x11\xaer>\x8c\x94\xa0\x0f\xc5|?\xfc]Y%\xd6\xd3\x81', b'\xb0z\x9b\xbf(\xbeA\x86\xab\xcd\xbct\xba\xcaX\xf1lz\xb0R', b'\xf7\xa4\xfde\x00\x1a\xe1Y\x84\x9a\x8c\xf9\xcd<\xa7\xc9M@\xfb ', b'\xb6\xcaj\xe0\xc9bWl\x9b$\x14M\x87e\xfe\x87/=\xc4\x92', b':\xffz\xc1q\xde\xac)=^\x8auXJ\xd9<\x94A(H', b'\xc7\xc0?-G?$\xb8\x8c\x03v\x86z\x06\xb8\xaf$h\xa6 ', b'\xd4y\x9d\x048\x0c\x9c\xea\xc0\x8f\x04q\xaa\x10\xe3#\x03\xdc>\xc5', b'\x16\xda\xfeX\xb9g\x02+\x9a%u\xfbN\xc1\xf0\x7f&\xa8\xf0\xf1', b'\x1c\xa9\x04\x1c\xf3c%\x08\xac\xab\xb2\xd3~E\x82\xac\x05\x01\xe4\xf3', b'\x11l\x0bg\x95s"1\x1e\xcb\x95y~\xc7\x9f\xbb@\xca\x1d3', b'\x10|\x0e\x88\xd9\xed\xd4\x12\xa9\x1f\xe7\x87\x03\xad\x04\x88;\x85\xc1Z', b'\x1b\x12\xf3\x07y\xce\x15\xd5\xf3}1[\xf2\x07\xe8\xe2\xfb\xa9\x11c', b'\x7f\xc2\xa3j\x1d\xe2.\xc0\xe7\xdc\xca4\xfb\xa94\x88\xcf\x88\xd2\x88', b'\xf1\x1d\xb2G\x8a\x8a\xc58\x8f\n\xadP\x8f\x95\xe4n\xa9}\xef\xf0', b'5\xc9\x97\x97Q\xf5\x99J\n\xac<B5\xb5\xfc\r*\xcf\x03L', b'\xd1\xef\x89\x83s\xbdp\x817P\x8b\x06\x84&Ykk#\xa9F', b'\xc2\x1f\xaeq\xacP\n\xe6\xc4\xd2\xd0\xf6Z\xc2\xeb7\x8c\xc8[\x0e', b'\xbd\x9e\xff#\xbcw\x9aI$\x83*\xbd\xea\x18\x04\xcc[\x1a\xebq', b'\xae\x189\xb3\xf4\xa8\x86\xf0\x7f\xcfwS8\xe2\xd6\x10>\x1e:\x8f', b'\\C\xa1GV\x9c8\x8a\\\xf7tQw\xcf~\r\xd6Q\x86\x9b', b'\xcd\x1d\xd1\xd5\xebmi\x80\x07\x8dV\x13\xca\xbf\xffu\xad\xfe;\x07', b'\xb5\x85J\xc8rao\x8c\xf3\x893\xe5?\x1b\x94(8\x1f!\x00', b'\xaf\xfeuRYs\x1d\xbb\x081T\xfb\t\xbc\xfc\xf4jG\xc4\x84', b'\x99\x1aL\x0f4\xcd\x0b`\xd6\xcf\x9e\xe3\xea\xde\xc2[\xba4wa', b'\x13\xc1\x1b?\xa7\x82u\t\x0e\x8d\xc1\x15w\xd5\xf4\xb4\x97#\xb7\xe5', b'\xa8\xba\x83@\xb0Fq\xe4M\xcd\x97~\xf7\xa0\x1b\xe5\x88\xf6\xabW', b'\t7\x19\xfc\xda\xb1\xf7+4\xd4\xf4\x84\xbf\xe2\xc9\xfd\x16\xe0\x14K', b'8N\xcf3\xe9\x88\xf9\xd6\x18\xa62\xbb\xa9\t\xe1pV\x06{7', b'\xb5Gr\x18\x071\x95\xac\xa3NAP6f\xe1\xec\xcb\xb2(G', b'\xf7\x0b\x8b\x9cZ\x9c\xd7\xfe,WI0\xc7\x14l|2\x98\x8c\xb4', b'\xc8\x13q\x03\n\xbbB\x05\xd3\xff\x84O|\xcc\\\xdc\x1bM\xc05', b'\xa6 Wn\x8b\x960\x0ehFV\x1d\x84KO\xc8|\x8e\xf8\xbc', b'\xdf\x11\x8aU\xb5\xaaP\xb8,\x8a\xb2\xae]1)=~\x10\xbe\xb1', b'?\xefxC\xa90c]\x1f \xdb\x95\xc2F\x1b\x1d\xdbH\xcfv', b'\x84B\xd6AG\xc0-\x0cQ\x87\xc9\x94\xe0\xd4\xf3\xd2\xf6K\x01\xdc', b'\x91\x86\xc6\x85\xd6\xdfI\xfa\x82\t\x8c\xe9\x9f\x93\x81\xaa\x99R3a', b'\xf1\xb2\x82\xf9_\xf8P\x1b\xd1Y6\x82\xa4\n\x15t3W\xf4\xfc', b'W\xa2\xf8\xd1\xd3}\xf0\x17\xe5\xf4a\xbcg\xde\xd6\xfe_\xaf\x16X', b'\x9e\xfb9\xef\xf5\xa2&|\xeb\x98B\xbdg\xb0\xd8\xeb\xc6\x89~\xb3', b'l\xeb\x9e\xc6\xecM%h\x84\xc2\xff\xf4\xa5@~\xbdj\xc0D\x9a', b'\x95i,YR\xa6\x02Y.\x9d\x91#"\xcf\\\xd0q7\xc0Q', b'l\xe1\xbf\xe7\x90C\xeca\x83\xce\xca\x00\xc2HR\xa55Us\x82', b'\xf8|O\x1b\xd7)\x8b\xab\xb6*\x1dx.\x1c\xa9\xe4\x94\xbeMH', b'fVl\x01\x98\x1f^N?\x88\xbeU\xeds\x87\x93a\xa1B;', b'd`s\xbf~\xed\x00\x9e.\xd4[\xd3\xaa\xa2\n\xd7\xcf\xd6;l', b'\x08zF[\xfa\xc5\xe2\xda\x02\xc06"\x0c\xf6J\x1d\x8f`q\x1a', b'|Bg\x97\xc6\xa0G\xb12\xee\x14mI{\xe6\xff\\U\xcc9']


words = buf_to_chunks(test_rand_bv)


"""
best_nonce, use_field = choose_best_nonce(old_nonce_results, words[:8])

print(best_nonce)
print(use_field)

exit()


print(SET_NO)
print(EDGE_NO)
print(WORD_NO)

exit()

"""

"""
nonce_list = []
fieldless_list = []
set_last_hash = b"init"
edge_hashes = []
for set_offset in range(0, SET_NO):
    set_nodes = node_list[(set_offset * POW_SET_LEN) * 2:((set_offset + 1) * POW_SET_LEN) * 2]
    set_edge_hashes = compute_edge_hash_list(set_nodes, set_offset, set_last_hash)
    assert(len(set_edge_hashes) <= POW_SET_LEN)

    edge_hashes = edge_hashes + set_edge_hashes

    set_last_hash = set_edge_hashes[-1]

    
    results = clusted_shared_pow_manager(test_sc, CLUSTER_CORE_NO, set_edge_hashes)

    print(results)
    
    set_word_list = words[(set_offset * POW_SET_LEN) * 2:((set_offset + 1) * POW_SET_LEN) * 2]
    assert(len(set_word_list) <= POW_SET_LEN * 2)
    best_nonce = results[0]

    print(set_offset)
    print(best_nonce)
    print()

    nonce_list.append(best_nonce)



#print(nonce_list)

print(edge_hashes)
"""





nonces = [[1044355555, b'\xe3\x99?>', 8.0, 0.5, 8, 6], [2899788880, b'PD\xd7\xac', 8.0, 0.5, 1, 0], [784060060, b'\x9c\xce\xbb.', 8.0, 0.5, 2, 1], [4192945908, b'\xf4F\xeb\xf9', 8.0, 0.5, 6, 1], [1645709622, b'6\x89\x17b', 8.0, 0.5, 4, 6], [1187207087, b'\xafW\xc3F', 8.0, 0.5, 4, 0], [2973343122, b'\x92\x9d9\xb1', 8.0, 0.5, 4, 1], [163170762, b'\xca\xc9\xb9\t', 8.0, 0.5, 3, 4], [693856640, b'\x80i[)', 8.0, 0.5, 4, 0], [870588066, b'\xa2\x1e\xe43', 8.0, 0.5, 3, 2], [4286417330, b'\xb2\x89}\xff', 8.0, 0.5, 6, 1], [1713078412, b'\x8c\x80\x1bf', 8.0, 0.5, 5, 0], [166142981, b'\x05$\xe7\t', 8.0, 0.5, 3, 0], [2838046601, b"\x89')\xa9", 8.0, 0.5, 8, 0], [780633642, b'*\x86\x87.', 8.0, 0.5, 2, 0], [521664485, b'\xe5\xf7\x17\x1f', 8.0, 0.5, 1, 4], [660652026, b"\xfa\xbf`'", 8.0, 0.5, 1, 0], [192460537, b'\xf9\xb6x\x0b', 8.0, 0.5, 6, 0], [1400970051, b'C\x1b\x81S', 8.0, 0.5, 4, 1], [1279413774, b'\x0eNBL', 8.0, 0.5, 3, 0], [1724860836, b'\xa4I\xcff', 8.0, 0.5, 5, 0], [2866862507, b'\xab\xd9\xe0\xaa', 8.0, 0.5, 3, 1], [2700024884, b'4\x1c\xef\xa0', 8.0, 0.5, 3, 1], [1291457918, b'~\x15\xfaL', 8.0, 0.5, 4, 0], [807320515, b'\xc3\xbb\x1e0', 8.0, 0.5, 7, 0], [1350344109, b'\xad\x9d|P', 8.0, 0.5, 2, 1], [3615730463, b'\x1f\xab\x83\xd7', 8.0, 0.5, 3, 1], [2012579342, b'\x0e\x86\xf5w', 8.0, 0.5, 3, 0], [1117543052, b'\x8cZ\x9cB', 8.0, 0.5, 5, 2], [2299783669, b'\xf5\xe9\x13\x89', 8.0, 0.5, 2, 0], [2360042970, b'\xdae\xab\x8c', 8.0, 0.5, 3, 0], [760268037, b'\x05\xc5P-', 8.0, 0.5, 2, 1], [2170048726, b'\xd6PX\x81', 8.0, 0.5, 5, 1], [1132088118, b'6KzC', 8.0, 0.5, 4, 3], [2159860720, b'\xf0\xdb\xbc\x80', 8.0, 0.5, 4, 4], [3503515179, b'+f\xd3\xd0', 8.0, 0.5, 6, 1], [19520575, b'?\xdc)\x01', 8.0, 0.5, 5, 0], [317185419, b'\x8b\xdd\xe7\x12', 8.0, 0.5, 4, 3], [875624483, b'#\xf804', 8.0, 0.5, 8, 0], [1425500133, b'\xe5g\xf7T', 8.0, 0.5, 6, 0], [552226050, b'\x02M\xea ', 8.0, 0.5, 1, 2], [2040731647, b'\xff\x17\xa3y', 8.0, 0.5, 8, 0], [356727306, b'\n:C\x15', 8.0, 0.5, 3, 0], [3271742456, b'\xf8\xd3\x02\xc3', 8.0, 0.5, 4, 1], [4247053968, b'\x90\xe6$\xfd', 8.0, 0.5, 5, 1], [4284523913, b'\x89\xa5`\xff', 8.0, 0.5, 4, 0], [644296069, b'\x85-g&', 8.0, 0.5, 2, 0], [3064810406, b'\xa6K\xad\xb6', 8.0, 0.5, 4, 0], [3396669693, b'\xfd\x10u\xca', 8.0, 0.5, 5, 0], [1392663096, b'8Z\x02S', 8.0, 0.5, 4, 0], [1379849433, b'\xd9\xd4>R', 8.0, 0.5, 5, 3], [430794326, b'Vf\xad\x19', 8.0, 0.5, 7, 1], [1553139711, b'\xff\x07\x93\\', 8.0, 0.5, 3, 1], [993152558, b'.N2;', 8.0, 0.5, 4, 0], [3751928366, b'.\xe2\xa1\xdf', 8.0, 0.5, 5, 1], [245500751, b'O\x0b\xa2\x0e', 8.0, 0.5, 5, 1], [1632462609, b'\x11gMa', 8.0, 0.5, 1, 1], [2765410577, b'\x11\xd1\xd4\xa4', 8.0, 0.5, 4, 0], [2649784729, b'\x99\x81\xf0\x9d', 8.0, 0.5, 4, 3], [1192146922, b'\xea\xb7\x0eG', 8.0, 0.5, 4, 0], None]







"""
for nonce in nonces_extended:
    set_no = 0
    start_offset = set_no * POW_SET_LEN
    stop_offset = start_offset + POW_SET_LEN
    print(min_prefixes(nonce[1], edge_hashes[start_offset:stop_offset]))
    input("enter to con")
    print()

exit()
"""

# 1. On [1] check that [0] + [1] a = prefix total >= 4
# 2. On [2] check that prefix + a is >= 12
# exact prefix combination would be a decent filter but how to store it compactly

# (45 * (5626 ** 2)) / 12



random.seed(12345)

def generate_rand_edge_lists(list_no, member_no_list, edge_hashes):
    max_edge_bits = (2 ** (20 * 8)) - 1
    edge_lists = []
    for edge_offset in range(0, len(edge_hashes)):
        edge_list = []

        member_no_a = member_no_list[(edge_offset * 2)]
        member_no_b = member_no_list[(edge_offset * 2) + 1]
        member_no = member_no_a * member_no_b
        for member_offset in range(0, member_no):
            # Since hashes are suppose to be random just generate max bits
            as_int = random.randrange(0, max_edge_bits + 1)
            as_bytes = as_int.to_bytes((as_int.bit_length() + 7) // 8, byteorder="little")
            edge_list.append(as_bytes)

        # Now insert the real edge randomly.
        insert_offset = random.randrange(0, member_no)
        edge_list[insert_offset] = edge_hashes[edge_offset]

        # Record the list of edges.
        edge_lists.append(edge_list)

    # ... and return them.
    return edge_lists



# Generate the edges in memory instead of all at once. pop what you dont need.
def reduce_set_edges_exec(params):
    start, stop, cand_no_list, col_division, set_offset, nonce, prev_edge_out, prefix_filter, type_offset = params
    nonce_bytes = nonce.to_bytes((nonce.bit_length() + 7) // 8, byteorder="little")

    # Make edge generators.
    edge_makers = []
    # todo fix zero indexing -- add last hash out and more info fore return
    def closure(cand_a_no, cand_b_no, edge_offset, edge_no, start_no, stop_no, do_print=0):
        def edge_gen():
            no = 0
            node_a = 0
            while node_a < cand_a_no:
                node_b = 0
                while node_b < cand_b_no:
                    if start_no is not None:
                        if no < start_no:
                            no += 1
                            node_b += 1
                            continue

                    if do_print:
                        print([node_a, node_b])

                    # Get edge hash and chain together from previous set if start edge.
                    edge_offset_overall = (set_offset * POW_SET_LEN) + edge_offset
                    h_out = compute_edge_hash(edge_offset_overall, node_a, node_b)
                    if edge_offset == 0:
                        h_out = hashlib.sha1(prev_edge_out + h_out).digest()


                    yield h_out

                    node_b += 1
                    no += 1
                    if stop_no is not None:
                        if no >= stop_no:
                            return

                node_a += 1

        return edge_gen


    edge_no = int(len(cand_no_list) / 2)
    assert(edge_no)
    for i in range(0, edge_no):
        cand_a_no = cand_no_list[(i * 2)]
        cand_b_no = cand_no_list[(i * 2) + 1]

        #print(cand_a_no)
        #print(cand_b_no)

        edge_start = None
        edge_stop = None
        do_print = 0
        if i == 0:
            edge_start = start
            edge_stop = stop
            do_print = 0

        edge_makers += [closure(cand_a_no, cand_b_no, i, edge_no, edge_start, edge_stop, do_print)]


    result_size = 10000
    results = []
    hash_list = []
    target_to_beat = MAX_SET_GROWTH
    for edge_zero in edge_makers[0]():
        out_total = 0
        in_total = 0
        prev_bytes = b"b"
        pow_bytes = b""
        fingerprint = b""
        edge_list = [edge_zero]
        if edge_no == 1:
            fingerprint = sha1(b"".join(edge_list)).digest()

        #print(edge_zero)

        out_zero = cumulative_pow([nonce, nonce_bytes, edge_zero, 0, pow_bytes, prev_bytes, fingerprint, out_total, in_total])
        #print(out_zero)
        
        if out_zero is None:
            print("a")
            continue
        else:
            target_to_beat, results = save_cumulative_results(edge_list, out_zero, target_to_beat, 0, edge_no - 1, results, result_size)


        for edge_one in edge_makers[1]():
            edge_list = [edge_zero, edge_one]
            if edge_no == 2:
                fingerprint = sha1(b"".join(edge_list)).digest()

            out_one = cumulative_pow([nonce, nonce_bytes, edge_one, 1, out_zero[0], out_zero[1], fingerprint, out_zero[3], out_zero[4]])
            if out_one is None:
                print("b")
                continue
            else:
                target_to_beat, results = save_cumulative_results(edge_list, out_one, target_to_beat, 1, edge_no - 1, results, result_size)

            edge_one_prefix = lead_zeros(out_one[0])

            if edge_one_prefix != prefix_filter[0]:
                continue


            #if edge_one_prefix < 4:
            #   continue


            for edge_two in edge_makers[2]():
                edge_list = [edge_zero, edge_one, edge_two]
                if edge_no == 3:
                    fingerprint = sha1(b"".join(edge_list)).digest()

                out_two = cumulative_pow([nonce, nonce_bytes, edge_two, 2, out_one[0], out_one[1], fingerprint, out_one[3], out_one[4]])
                #print(out_two)
                #exit()
                if out_two is None:
                    print("c")
                    continue
                else:
                    target_to_beat, results = save_cumulative_results(edge_list, out_two, target_to_beat, 2, edge_no - 1, results, result_size)

                edge_two_prefix = lead_zeros(out_two[0])


                if edge_two_prefix != prefix_filter[1]:
                    continue

                """
                if edge_one_prefix + edge_two_prefix < 4:
                    continue
                """


                for edge_three in edge_makers[3]():
                    edge_list = [edge_zero, edge_one, edge_two, edge_three]

                    #print(edge_three)
                    if edge_no == 4:
                        fingerprint = sha1(b"".join(edge_list)).digest()

                    out_three = cumulative_pow([nonce, nonce_bytes, edge_three, 3, out_two[0], out_two[1], fingerprint, out_two[3], out_two[4]])


                    if out_three is None:
                        print("d")
                        continue
                    else:
                        #dif = str(out_three[3]).replace(".", "")
                        #out_three[3] = int(dif[:3])
                        if out_three[3] != 8.0:
                            continue

                        target_to_beat, results = save_cumulative_results(edge_list, out_three, target_to_beat, 3, edge_no - 1, results, result_size)


    return results
    


def reduce_set_edges_controller(sc, usable_cores, candidate_no_list, node_list, nonce_list, edge_hashes, outliers):
    params_lists = []
    prev_edge_out = b"init"
    for set_offset in range(0, SET_NO):
        # Skip outliers but record it.
        if set_offset in outliers:
            print("Skipping outlier ", set_offset)
            continue

        set_cand_no_list = candidate_no_list[set_offset * (POW_SET_LEN * 2):(set_offset + 1) * (POW_SET_LEN * 2)]
        col_zero_max = set_cand_no_list[0] * set_cand_no_list[1]

        col_division = int(col_zero_max / usable_cores)
        nonce = nonce_list[set_offset][0]

        prefix_filter = [nonce_list[set_offset][4], nonce_list[set_offset][5]]
        type_offset = 8.0

        # We don't assume even divisibility.
        # Every part of the range is fully allocated.
        col_division_last = col_zero_max - (col_division * (usable_cores - 1))

        # Set prev_edge_out.
        set_edge_hashes = edge_hashes[(set_offset * POW_SET_LEN):(set_offset * POW_SET_LEN) + POW_SET_LEN]
        if set_offset > 0:
            # Prev edge out is the last edge hash of the previous set.
            prev_edge_out = edge_hashes[((set_offset - 1) * POW_SET_LEN) + 3]

        results = []
        for i in range(0, usable_cores):
            # Range is from start to stop - 1. It doesn't include stop.
            start = i * col_division
            stop = start + col_division

            # Allocate last core anything left over.
            if i == usable_cores - 1:
                # If nothing is coming next we want to include stop in the range.
                stop = start + col_division_last + 1

            # Save worker params.
            params = [start, stop, set_cand_no_list, col_division, set_offset, nonce, prev_edge_out, prefix_filter, type_offset]
            params_lists.append(params)

            # Collect results (on same machine for testing.)
            #results += reduce_set_edges_exec(params)


        results = sc.parallelize(params_lists, usable_cores).map(reduce_set_edges_exec).collect()
        unsorted_results = []
        for result in results:
            unsorted_results = unsorted_results + result


        # nonce_info: nonce_int, nonce_bytes, out_total, in_total, edge_list, id
        sorted_results = sorted(unsorted_results, key=lambda k: (k[2], k[5]))

        # Record offset of correct set hashes by comparing to fixed set hashes.
        # offsets are wrong for loops
        sorted_offset = 0
        found_set_edge_hashes = 0
        for result in sorted_results:
            found_edges = result[4]
            if found_edges == set_edge_hashes:
                found_set_edge_hashes = 1
                break

            sorted_offset += 1

        if not found_set_edge_hashes:
            print("Did not find offset ", set_offset)
        else:
            print("Found set offset ", set_offset)
            print(sorted_offset)
        print("result len = ", len(sorted_results))
        print()








set_zero_edge_cand_lists = generate_rand_edge_lists(1, candidate_no_list[0:POW_SET_LEN * 2], edge_hashes[0:POW_SET_LEN])

reduce_set_edges_controller(test_sc, CLUSTER_CORE_NO, candidate_no_list, node_list, nonces, edge_hashes, [26, 60])





"""
4096.0
4096.0

16777216.0
16777216.0

68719476736.0
68719476736.0

281474976710656.0
274877906944.0

274877906944.0

"""


