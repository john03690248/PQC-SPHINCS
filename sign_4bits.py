import signbit
def keypair():
    p0,s0 = signbit.keypair()
    p1,s1 = signbit.keypair()
    p2,s2 = signbit.keypair()
    p3,s3 = signbit.keypair()
    return p0+p1+p2+p3,s0+s1+s2+s3

def sign(m,secret):
    if type(m) != int:
        raise Exception('message must be int')
    if m < 0 or m > 15:
        raise Exception('message must be between 0 and 15')
    sm0 = signbit.sign(1 & (m >> 0),secret[0:64])
    sm1 = signbit.sign(1 & (m >> 1),secret[64:128])
    sm2 = signbit.sign(1 & (m >> 2),secret[128:192])
    sm3 = signbit.sign(1 & (m >> 3),secret[192:256])
    return sm0, sm1, sm2, sm3

def open(sm,public):
    m0 = signbit.open(sm[0],public[0:64])
    m1 = signbit.open(sm[1],public[64:128])
    m2 = signbit.open(sm[2],public[128:192])
    m3 = signbit.open(sm[3],public[192:256])
    return m0 + 2*m1 + 4*m2 + 8*m3
