from django.test import TestCase, override_settings
from threading import local
from cid.locals import get_cid, set_cid, generate_new_cid


_thread_locals = local()


class TestCidStorage(TestCase):

    def setUp(self):
        self.clear_cid()
        self.cid = 'test-cid'

    def tearDown(self):
        self.clear_cid()

    def clear_cid(self):
        try:
            delattr(_thread_locals, 'CID')
        except AttributeError:
            pass

    def test_get_empty_cid(self):
        self.assertIsNone(get_cid())

    def test_set_cid(self):
        self.assertIsNone(get_cid())
        set_cid(self.cid)
        self.assertEqual(self.cid, get_cid())

    @override_settings(CID_GENERATE=True, CID_GENERATOR=lambda: 'constant_correlation')
    def test_custom_generator(self):
        assert generate_new_cid() == 'constant_correlation'
