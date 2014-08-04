from django.test import TestCase
from mock import Mock, patch

from cid.middleware import CidMiddleware


class TestCidMiddleware(TestCase):

    def setUp(self):
        self.cid = 'test-cid'

    def get_mock_request(self, cid=None):
        request = Mock()
        request.META = {}
        if cid:
            request.META['X_CORRELATION_ID'] = cid
        return request

    @patch('cid.locals._thread_locals')
    def test_process_request(self, _thread_locals):
        request = self.get_mock_request(self.cid)
        middleware = CidMiddleware()
        middleware.process_request(request)
        self.assertEqual(self.cid, getattr(_thread_locals, 'CID', None))

    @patch('cid.locals._thread_locals')
    def test_process_request_with_no_header(self, _thread_locals):
        request = self.get_mock_request()
        middleware = CidMiddleware()
        middleware.process_request(request)
        self.assertEqual(None, getattr(_thread_locals, 'CID', None))
