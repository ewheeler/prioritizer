from unittest import TestCase
from models.encoder import Encoder


class TestEncoder(TestCase):
    def test_that_encode_text_using_md5(self):
        text = "important text"
        encoder = Encoder()
        encoded_text = encoder.encode(text)
        self.assertEquals(encoded_text, '0577b6f9b176bd6a7a13cfbb1de0554a')

    def test_encoding_without_text(self):
        text = None
        encoder = Encoder()
        self.assertRaises(AssertionError, encoder.encode, text)

    def test_encoding_with_blank_text(self):
        text = ''
        encoder = Encoder()
        self.assertRaises(AssertionError, encoder.encode, text)

    def test_encoding_with_space_text(self):
        text = ' '
        encoder = Encoder()
        self.assertRaises(AssertionError, encoder.encode, text)
