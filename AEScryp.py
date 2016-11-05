#version 1.0
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class AEScryp():
    def __init__(self,priKey):
        self.key = fillText(priKey)
        self.mode = AES.MODE_CBC

    def encrypt(self,info):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        cipherinfo = cryptor.encrypt(fillText(info))
        return b2a_hex(cipherinfo)

    def decrypt(self,info):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        plain_info  = cryptor.decrypt(a2b_hex(info))
        return plain_info.rstrip('\0')

def fillText(text):
    length = 16
    count = len(text)
    if count < length:
        add = (length-count)
        info = text + ('\0' * add)
    elif count > length:
        add = (length-(count % length))
        info = text + ('\0' * add)
    return info

def test():#test code
    testObj = AEScryp('myownkey11111111')
    before = 'before encode'
    after = testObj.encrypt(before);
    recover = testObj.decrypt(after);
    print 'Original: '+before
    print 'Secure Code: '+after
    print 'Recover: '+recover

if __name__ == '__main__':
    test()
