import os
from hashlib import sha3_256
def keypair():
    secret = sha3_256(os.urandom(32)).digest()
    public = sha3_256(secret).digest()
    return public, secret

def sign(message,secret):
    if message != '':
        raise Exception('nonempty message')
    signedmessage = secret
    return signedmessage

def open(signedmessage,public):
    if sha3_256(signedmessage).digest() != public:
        raise Exception('bad signature')
    message = ''
    return message