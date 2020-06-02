from params import *
from utils import *

# Taken from https://giovanni.bajo.it/post/47119962313/golomb-coded-sets-smaller-than-bloom-filters
# Modified to work in memory for speed

def bitwriter(f):
    """
    Coroutine to write bits into a file-like.
    Use .send((N, V)) to write the N least-significant
    bits of V into the file.
    Remember to call .close() to flush the internal
    state when done.
    """
    v = 0
    n = 0
    try:
        while 1:
            (n2,v2) = yield None
            v <<= n2
            v |= v2 & ((1<<n2)-1)
            n += n2
            while n >= 8:
                b = (v >> (n-8)) & 255
                f.write(bytes([b]))
                n -= 8
            v &= 255
    except GeneratorExit:
        if n != 0:
            v = (v << (8-n)) & 255
            f.write(bytes([v]))
        raise


# ////
def bitreader(f):
    """
    Coroutine to read bits from a file-like.
    Use .send(N) to read N bits from the file.
    """
    accum = 0
    n = 0
    v = None
    while 1:
        n2 = yield v
        while n <= n2:
            accum <<= 8
            try:
                accum |= ord(f.read(1))
            except TypeError:
                # ord(None) => eof
                return
            n += 8
        v = (accum >> (n-n2)) & ((1<<n2)-1)
        n -= n2
        accum &= (1<<n)-1


def golomb_enc(f, P):
    """
    Coroutine to encode Golomb/Rice-encoded values into
    a file-like f, with parameter P.
    Use .send(V) to encode the value V into the file.
    This is an optimal encoding if values are geometrically
    distributed with P.
    """
    logp = int(math.log(P,2))
    f = bitwriter(f); f.__next__();
    while 1:
        v = yield None
        q,r = v//P, v%P
        f.send((q+1, (1<<(q+1))-2))
        f.send((logp, r))   


def golomb_dec(f, P):
    """
    Coroutine to decode Golomb/Rice-encoded values
    from a file-like f, with parameter P.
    Use .next() (or iterate over it) to read the values.
    """
    logp = int(math.log(P,2))
    f = bitreader(f); f.__next__()
    while 1:
        try:
            v = 0
            while f.send(1):
                v += P
            v += f.send(logp)
        except StopIteration:
            return
        yield v


# def gcs_hash(w, (N,P)):
def gcs_hash(w, params):
    """
    Hash value for a GCS with N elements and 1/P probability
    of false positives.
    We just need a hash that generates uniformally-distributed
    values for best results, so any crypto hash is fine. We
    default to MD5.
    """
    N, P = params
    if type(w) == str:
        w = w.encode("ascii")
    
    

    h = md5(w).hexdigest()
    h = int(h[24:32], 16)
    return h % (N*P)

    
    #h = hash(w)
    
    #h = int.from_bytes(sha1(w).digest(), byteorder="little")
    
    #h = crc32(w)
    
    x = (N * P)
    #h = xxhash.xxh32(w).intdigest()
    
    h = int.from_bytes(to_bytes(h1(w)), byteorder="little")
    return h % x


class GCSBuilder:
    def __init__(self, N, P):
        self.N = N
        self.P = P
        self.values = array("L")
        self.values.append(0)
        
    def add(self, v):
        self.values.append(gcs_hash(v, (self.N,self.P)))

    def finalize(self, f):
        values = sorted(self.values)
        f.write(struct.pack("!LL", self.N, self.P))
        f = golomb_enc(f, self.P)
        f.__next__()
        for i in range(len(values)-1):
            d = values[i+1] - values[i]
            if d == 0:
                continue
            f.send(d)
        f.close()


class GCSQuery:
    def __init__(self, f):
        self.f = f
        self.N, self.P = struct.unpack("!LL", self.f.read(8))

    def _rewind(self):
        self.f.seek(8)

    def query(self, w):
        h = gcs_hash(w, (self.N,self.P))
        N = 0
        self._rewind()
        for d in golomb_dec(self.f, self.P):
            N += d
            if h == N:
                return True
            if h < N:
                # early-exit since values are sorted
                return False
        return False
        


