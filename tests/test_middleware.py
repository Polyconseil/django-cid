from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.utils import override_settings
from mock import Mock, patch

import cid.locals
from cid.middleware import CidMiddleware


class TestCidMiddleware(TestCase):

    def setUp(self):
        self.cid = 'test-cid'

    def tearDown(self):
        super().tearDown()
        cid.locals.set_cid(None)  # don't leak cid between each test

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

    @patch('uuid.uuid4')
    @patch('cid.middleware.set_cid')
    @override_settings(CID_GENERATE=True)
    def test_process_request_generates_uuid(self, set_cid, uuid4):
        uuid4.return_value = '6fa459ea-ee8a-3ca4-894e-db77e160355e'
        request = self.get_mock_request()
        middleware = CidMiddleware()
        middleware.process_request(request)
        set_cid.assert_called_with('6fa459ea-ee8a-3ca4-894e-db77e160355e')

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
        response = middleware.process_response(request, response)
        self.assertEqual(response['X_CORRELATION_ID'], self.cid)

    @patch('cid.middleware.get_cid')
    @override_settings(CID_RESPONSE_HEADER="X-Custom-Name")
    def test_process_response_custom_header_name(self, get_cid):
        get_cid.return_value = self.cid
        request = Mock()
        response = {}
        middleware = CidMiddleware()
        response = middleware.process_response(request, response)
        self.assertEqual(response['X-Custom-Name'], self.cid)

    @patch('cid.middleware.get_cid')
    @override_settings(CID_RESPONSE_HEADER=None)
    def test_process_response_no_header(self, get_cid):
        get_cid.return_value = self.cid
        request = Mock()
        response = {}
        middleware = CidMiddleware()
        response = middleware.process_response(request, response)
        self.assertNotIn('X_CORRELATION_ID', response.keys())

    @patch('cid.middleware.get_cid')
    def test_process_response_with_no_cid(self, get_cid):
        get_cid.return_value = None
        request = Mock()
        response = {}
        middleware = CidMiddleware()
        response = middleware.process_response(request, response)
        self.assertNotIn('X_CORRELATION_ID', response.keys())

    @override_settings(
        MIDDLEWARE_CLASSES=('cid.middleware.CidMiddleware', ),
        CID_GENERATE=True,
    )
    def test_integration(self):
        """Assert the middleware works with the Django initialization"""
        # First call generates an new Correlation ID
        response = self.client.get(reverse('ping'))  # comes from the sandbox
        cid = response.get('X_CORRELATION_ID')
        self.assertIsNotNone(cid)

        # Later calls with the header will keep it
        response = self.client.get(
            reverse('ping'),  # comes from the sandbox
            **{'X_CORRELATION_ID': cid}
        )
        self.assertEqual(response['X_CORRELATION_ID'], cid)
