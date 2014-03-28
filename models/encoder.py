import hashlib

class Encoder(object):
    def encode(self, text):
        # TODO anything else we should assert about the text?
        assert text not in ['', ' ', None]
        # use hexdigest() not digest() so hash is double length and only ascii
        return hashlib.md5(text).hexdigest()
