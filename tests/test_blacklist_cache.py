from unittest import TestCase
from mock import patch, Mock
from mockredis import mock_strict_redis_client
from models.blacklist_cache import BlacklistCache
from models.encoder import Encoder


class TestBlacklistCache(TestCase):
    def setUp(self):
        self.client = mock_strict_redis_client()
        self.cache = BlacklistCache(self.client)

    @patch('redis.StrictRedis', mock_strict_redis_client)
    def test_blacklist_is_updated_with_new_word(self):
        text = "new info"
        key_name = "my script"
        self.cache.key_name = Mock(return_value=key_name)
        self.cache.encoder = Encoder()

        self.cache.add_to_blacklist(text)
        self.assertTrue(self.client.sismember(key_name, "a3e8c519de8eedc62d52727c059053e2"))

    @patch('redis.StrictRedis', mock_strict_redis_client)
    def test_blacklist_is_not_updated_without_text(self):
        text = None
        key_name = "my script"
        self.cache.key_name = Mock(return_value=key_name)
        self.cache.encoder = Encoder()

        self.assertRaises(AssertionError, self.cache.add_to_blacklist, text)

    def test_that_key_name_is_blacklist(self):
        self.assertEquals(self.cache.key_name(), "ureport-high-priority-blacklist")

