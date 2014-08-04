from django.test import TestCase
from threading import local
from cid.locals import get_cid, set_cid


class TestCidStorage(TestCase):

    def setUp(self):
        self.cid = 'test-cid'

    def tearDown(self):
        _thread_locals = local()
        delattr(_thread_locals, 'CID')

    def test_get_empty_cid(self):
        self.assertIsNone(get_cid)

    def test_set_cid(self):
        self.assertIsNone(get_cid)
        set_cid(self.cid)
        self.assertEqual(self.cid, get_cid)
