import signempty
def keypair():
    p0,s0 = signempty.keypair()
    p1,s1 = signempty.keypair()
    return p0+p1,s0+s1

def sign(message,secret):
    if message == 0:
        return ('0' , signempty.sign('',secret[0:32]))
    if message == 1:
        return ('1' , signempty.sign('',secret[32:64]))
    raise Exception('message must be 0 or 1')

def open(signedmessage,public):
    if signedmessage[0] == '0':
        signempty.open(signedmessage[1],public[0:32])
    return 0
    if signedmessage[0] == '1':
        signempty.open(signedmessage[1],public[32:64])
    return 1
    raise Exception('message must be 0 or 1')
