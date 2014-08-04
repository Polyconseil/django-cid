from django.test import TestCase
from django.test.utils import override_settings
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

    @patch('cid.middleware.set_cid')
    def test_process_request(self, set_cid):
        request = self.get_mock_request(self.cid)
        middleware = CidMiddleware()
        middleware.process_request(request)
        set_cid.assert_called_with(self.cid)

    @patch('cid.middleware.set_cid')
    def test_process_request_with_no_header(self, set_cid):
        request = self.get_mock_request()
        middleware = CidMiddleware()
        middleware.process_request(request)
        set_cid.assert_called_with(None)

    @patch('cid.middleware.set_cid')
    @override_settings(CID_HEADER='A_TEST_HEADER')
    def test_process_request_with_custom_header(self, set_cid):
        request = Mock()
        request.META = {'A_TEST_HEADER': 'different-cid'}
        middleware = CidMiddleware()
        middleware.process_request(request)
        set_cid.assert_called_with('different-cid')

    @patch('cid.middleware.get_cid')
    def test_process_response(self, get_cid):
        get_cid.return_value = self.cid
        request = Mock()
        response = {}
        middleware = CidMiddleware()
        middleware.process_response(request, response)
        self.assertEqual(response['X_CORRELATION_ID'], self.cid)

    @patch('cid.middleware.get_cid')
    def test_process_response_with_no_cid(self, get_cid):
        get_cid.return_value = None
        request = Mock()
        response = {}
        middleware = CidMiddleware()
        middleware.process_response(request, response)
        self.assertNotIn('X_CORRELATION_ID', response.keys())



