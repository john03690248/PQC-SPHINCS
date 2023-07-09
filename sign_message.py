import signbit, hashlib
def keypair():
    keys = [signbit.keypair() for n in range(256)]
    public,secret = zip(*keys)
    return public,secret

def sign(message,secret):
    msg = message.encode('utf8')
    h = hashlib.sha3_256(msg).digest()
    hbits = [1 & (h[i//8])>>(i%8) for i in range(256)]
    sigs = [signbit.sign(hbits[i],secret[i]) for i in range(256)]
    return sigs, message

def open(sm,public):
    message = sm[1]
    msg = message.encode('utf8')
    h = hashlib.sha3_256(msg).digest()
    hbits = [1 & (h[i//8])>>(i%8) for i in range(256)]
    for i in range(256):
        if hbits[i] != signbit.open(sm[0][i],public[i]):
            raise Exception('bit %d of hash does not match' % i)
    return message
