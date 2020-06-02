from params import *

nonce_infos = [[1365061047, b'\xb7-]Q', 0.25, 0.015625], [1848219630, b'\xee\x97)n', 1.0, 0.0625], [242312691, b'\xf3eq\x0e', 0.5, 0.03125], [1309172843, b'kd\x08N', 0.5, 0.03125], [2949320465, b'\x11\x0f\xcb\xaf', 0.5, 0.03125], [11150583, b'\xf7$\xaa', 0.5, 0.03125], [3151049747, b'\x134\xd1\xbb', 0.0625, 0.00390625], [3976628613, b'\x85\x89\x06\xed', 0.5, 0.03125], [1032981196, b'\xcc\n\x92=', 1.0, 0.0625], [3015840604, b'\\\x13\xc2\xb3', 0.0625, 0.00390625], [585426497, b'A\xe6\xe4"', 0.25, 0.015625], [420764144, b'\xf0Y\x14\x19', 0.25, 0.015625], [1273382307, b'\xa3E\xe6K', 0.015625, 0.0009765625], [2365945643, b'+w\x05\x8d', 0.25, 0.015625], [1111984661, b'\x15\x8aGB', 0.125, 0.0078125], [1047052377, b'Y\xc0h>', 0.015625, 0.0009765625], [4191467485, b'\xdd\xb7\xd4\xf9', 0.0625, 0.00390625], [1719323171, b'#\xcazf', 0.0625, 0.00390625], [3899714000, b'\xd0\xe9p\xe8', 0.25, 0.015625], [1913901649, b'Q\xd2\x13r', 0.5, 0.03125], [1186982517, b'u\xea\xbfF', 0.25, 0.015625], [1882476678, b'\x86P4p', 1.0, 0.0625], [481113485, b'\x8d5\xad\x1c', 0.125, 0.0078125], [2816100731, b'{I\xda\xa7', 0.25, 0.015625], [1537317555, b'\xb3\x9a\xa1[', 1.0, 0.0625], [1299837149, b'\xdd\xf0yM', 0.125, 0.0078125], [2762009377, b'!\xeb\xa0\xa4', 0.25, 0.015625], [2901774569, b'\xe9\x90\xf5\xac', 0.5, 0.03125], [2172238615, b'\x17\xbby\x81', 0.5, 0.03125], [1581705709, b'\xed\xe9F^', 0.25, 0.015625], [2735855535, b'\xaf\xd7\x11\xa3', 1.0, 0.0625], [3746140393, b'\xe9\x90I\xdf', 0.5, 0.03125], [1309937681, b'\x11\x10\x14N', 2.0, 0.125], [1897525246, b'\xfe\xef\x19q', 1.0, 0.0625], [892924881, b'\xd1\xf385', 0.25, 0.015625], [1761038878, b'\x1eR\xf7h', 0.015625, 0.0009765625], [2066478753, b'\xa1\xf6+{', 0.25, 0.015625], [3805252633, b'\x19\x8c\xcf\xe2', 16.0, 1.0], [4121126792, b'\x88g\xa3\xf5', 0.125, 0.0078125], [1858820445, b']Y\xcbn', 1.0, 0.0625], [1801940571, b'[ngk', 0.00390625, 0.000244140625], [2687263008, b' a,\xa0', 0.5, 0.03125], [1360452954, b'Z\xdd\x16Q', 0.00390625, 0.000244140625], [240966423, b'\x17\xdb\\\x0e', 0.25, 0.015625], [586250089, b'iw\xf1"', 0.03125, 0.001953125], [448827198, b'>\x8f\xc0\x1a', 0.5, 0.03125], [3781675228, b'\xdc\xc8g\xe1', 0.5, 0.03125], [3702769046, b'\x96\xc5\xb3\xdc', 1.0, 0.0625], [3448396012, b'\xecX\x8a\xcd', 0.5, 0.03125], [267902009, b'9\xdc\xf7\x0f', 0.5, 0.03125], [1519358636, b'\xac\x92\x8fZ', 0.0625, 0.00390625], [97237764, b'\x04\xbb\xcb\x05', 0.0625, 0.00390625], [2527612037, b'\x85L\xa8\x96', 0.015625, 0.0009765625], [198549278, b'\x1e\x9f\xd5\x0b', 0.5, 0.03125], [4231129012, b'\xb4\xe71\xfc', 0.5, 0.03125], [72971396, b'\x84tY\x04', 0.25, 0.015625], [685441177, b'\x99\x00\xdb(', 0.5, 0.03125], [3285101028, b'\xe4\xa9\xce\xc3', 0.00390625, 0.000244140625], [792855110, b'F\x02B/', 0.5, 0.03125], [144957323, b'\x8b\xdf\xa3\x08', 0.25, 0.015625], [149922104, b'8\xa1\xef\x08', 1.9073486328125e-06, 1.1920928955078125e-07]]


#pow_view(nonce_infos[0][1], hash_list)

assert(len(nonce_infos) == SET_NO)


# record offset.
total = 0
results = []
i = 0
for nonce_info in nonce_infos:
    nonce_int, nonce_bytes, out_no, field_no = nonce_info
    nonce_info.append(i)

    bit_no = nonce_int.bit_length()
    remaining = 32 - bit_no
    if remaining < 4:
        total += 1

    i += 1

# Sort from largest nonce first.
nonce_infos = sorted(nonce_infos, key=lambda k: k[0], reverse=True)

# Quotient bit size
d = nonce_infos[-1][0]
q = int(nonce_infos[0][0] / d)
q_bits = q.bit_length()

# Find remainder bit size.
r_bits = 0
for nonce_info in nonce_infos:
    r = nonce_info[0] % q
    if r.bit_length() > r_bits:
        r_bits = r.bit_length()

print(q_bits)
print(r_bits)
print(32 - (q_bits + r_bits))

print(d)
print(d.bit_length()) # 4 bytes for divisor.

# 9 bits for quotient
# 9 bits for remainder

# ensure all chosen nonces are > min bit threshold to allow for compression



#print(total)


#sorted(unsorted_results, key=lambda k: k[2])
#print(nonce_infos)

nonce_info2 = []

for nonce_info in nonce_info2:
    nonce_int, nonce_bytes, x, y = nonce_info
    print(nonce_int)
    if 32 - nonce_int.bit_length() >= 4:
        print(nonce_info)
        break










