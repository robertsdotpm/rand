from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from pyspark import SparkConf, SparkContext
import sys, math
from hashlib import md5, sha256, sha1
import struct
from array import array
import codecs
import sys
import io
import binascii
from binascii import crc32
import xxhash
import copy
import warnings
from BitVector import BitVector as Bits
import random
import pprint
import json
import re
import os
import secrets
from multiprocessing import Pool
import pysnooper
import multiprocessing
import itertools
import time
import argparse
import uuid
from blake3 import blake3, KEY_LEN, OUT_LEN
from checksum import *

hex_down = binascii.unhexlify
hex_up = binascii.hexlify


class blake_mock:
    def __init__(self, buf):
        self.b = blake3(buf)
    
    def digest(self, length=0):
        return self.b.digest()

    def update(self, buf):
        self.b.update(buf)



class fletcher_mock:
    def __init__(self, buf):
        self.b = Fletcher64()
        self.update(buf)
    
    def digest(self, length=0):
        return self.b.digest()

    def update(self, buf):
        self.b.update(buf)


class xxhash_mock:
    def __init__(self, buf):
        self.b = xxhash.xxh32(buf)
    
    def digest(self, length=0):
        return self.b.digest()

    def update(self, buf):
        self.b.update(buf)

# Add offset adjustment to next compressed nonce so that removing it leaves a valid nonce range


POW_H = fletcher_mock

# In bytes.
BUF_SIZE = 1024 
PROB = 1024  # needs to be binary power
WORD_HASH_BOUNDARY = 0 # Every N words do a hash to the bloom filter.
CHKSUM_BITS = 1 
CHUNK_SIZE_BITS = 17 # 17 Not feasible to brute force larger values.
ACCURATE_CHKSUM_BITS = 32
ONLY_ADD_EVERY_N_WORD = 1
TEST_WORD_NO = 2
USE_RAND = 1
MAX_CIPHER_EDGE_BITS = 4
FIXED_CAND_NO = 0
USE_NO_PREFIX = 1
CORE_EXECUTOR_MAX = 5 
CLUSTER_CORE_NO = 64 # When running on a cluster.
CPU_CORE_NO = CLUSTER_CORE_NO # When running on singgle machine.

POW_SET_LEN = 4 # Set of edges -- not individual nodes.
NONCE_BITS = 32

USE_CHAINED_POW = 1 # 1
USE_PRE_FILTER = 0 # 1 
USE_INDEP_FILTER = 1 # 1
FIXED_INDEP_FILTER = 1  # 1 seems better for now. 

CHAINED_POW_TARGET = 0 # 6
INDEP_POW_TARGET = 10 # 14 seems better for now
PRE_FILTER_POW_TARGET = 1 # 1

TYPE_LIST = [2.0, 1.0, 0.5, 0.25]




"""
This is for the pre-filter
We use this as a heuristic to avoid having to check more than this number of entries. If prior prefixes don't reduce the set under this then we assume that it can't be a valid result. In reality the output size will be <= 1.
"""
MAX_SET_GROWTH = 1000000000 * 10 # 10 bil

SPARK_URI = "spark://192.168.75.22:7077"


# ------------------------------- STOP EDITING --------------------------------
# Don't touch bellow here.
# Useful computations.
MAX_WORD_INT = int((2 ** CHUNK_SIZE_BITS) - 1)
WORD_NO = math.ceil((BUF_SIZE * 8.0) / CHUNK_SIZE_BITS)
WORD_NO += WORD_NO % 2 # 484 (partial end)
EDGE_NO = math.ceil(WORD_NO / 2.0) # 241
SET_NO = math.ceil(EDGE_NO / POW_SET_LEN) # 61 (partial end)
AVG_BLOOM_POSITIVES = (2 ** CHUNK_SIZE_BITS) * (1.0 / PROB)
AVG_BLOOM_POSITIVES = AVG_BLOOM_POSITIVES * (1.0 / (2 ** CHKSUM_BITS)) 
AVG_EDGE_CANDIDATES = AVG_BLOOM_POSITIVES ** 2
FIELD_SIZE_BITS = CHUNK_SIZE_BITS - 2

# Length of the PoW hash function output in bytes.
POW_H_LEN = len(POW_H(b"test").digest())

# data structures: 
# cand_list = list of --unknown-- brute forced words from bloom query
# node_list = list of --correct-- offsets into cand list
# match_list = list of --correct-- offset
#      --pairs-- into cand set [[a, b], ...]
# edge = H of a pair [a, b] used for ciphers


"""
Todo:




Failures:

p=64, b=3, f=4, c=16, n=1 failed
p=128, b=3, f=4, c=17, n=1 failed
p=1024, b=3, f=0, c=17, n=1 failed

p=32, b=2, f=6, c=17, n=1 failed
p=32, b=2, f=6, c=17, n=1 failed
p=32, b=2, f=5, c=17, n=1 633600 failed

p=768, b=3, f=0, c=17, n=1, chk=0 failed

512 works, 256, 65 works
p=1024, b=6, f=1, c=16, n=1  <---- closest yet. significant is the higher than usual b. and c = 16 failed
p=1024, b=4 ... c=17,  failed
p=1024, b=5, f=1, c=16 ,  failed
p=1024, b=4, f=0, c=16 ,  failed
p=128, b=2, f=2, c=16 failed  <----- very close
p=128, b=1, f=2, c=17 failed
p=128, b=1, f=3, c=17, n=3failed
p=64, b=1, f=0, c=16, n=1 failed
p=8, b=1, f=7, c=16, n=1 failed
p=16, b=1, f=4, c=16, n=1 failed
p=128, b=2, f=5, c=16, n=3  failed

// Prefixes could be compressed -- permutations n = 5, r = 3, = 32 or 5 bits -- discard 1,2,8.
// that leaves 8 bits for offsets. Do offset calculations then see if those can be compressed. possibly it might fit
// fixing one of the prefixes in the code would require only 20 (r = 2) or 5 bits -- additional bit left for offsets:
    // 2 bits for Q, 7 bits for R. q = 100.
    max value possible would be 428 for the offset
"""
