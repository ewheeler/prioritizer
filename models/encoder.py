import hashlib

class Encoder(object):
    def encode(self,text):
        md5 = hashlib.md5()
        md5.update(text)
        return md5.digest()
