from unittest import mock

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.utils import override_settings

import cid.locals
from cid.middleware import CidMiddleware


class DummyResponse:
    def __init__(self, request):
        self.headers = {}
        self.request = request
    def __getitem__(self, header):
        return self.headers[header]
    def __setitem__(self, header, value):
        self.headers[header] = value


def get_response(request):
    return DummyResponse(request)


def make_request(cid=None, header_name='X_CORRELATION_ID'):
    request = mock.Mock()
    request.META = {}
    if cid:
        request.META[header_name] = cid
    return request


class TestCidMiddleware(TestCase):

    def tearDown(self):
        super().tearDown()
        cid.locals.set_cid(None)  # don't leak cid between each test

    def test_with_cid_from_upstream(self):
        request = make_request('cid-from-upstream')
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertEqual(request.correlation_id, 'cid-from-upstream')
        self.assertEqual(cid.locals.get_cid(), 'cid-from-upstream')
        self.assertEqual(response['X_CORRELATION_ID'], 'cid-from-upstream')

    def test_no_cid_from_upstream(self):
        request = make_request(cid=None)
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertIsNone(request.correlation_id, None)
        self.assertIsNone(cid.locals.get_cid(), None)
        self.assertEqual(response.headers, {})

    @override_settings(CID_GENERATE=True)
    @mock.patch('uuid.uuid4')
    def test_generate_cid(self, uuid4):
        uuid4.return_value = 'generated-cid'
        request = make_request(cid=None)
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertEqual(request.correlation_id, 'generated-cid')
        self.assertEqual(cid.locals.get_cid(), 'generated-cid')
        self.assertEqual(response['X_CORRELATION_ID'], 'generated-cid')

    @override_settings(CID_HEADER='X_CUSTOM_HEADER')
    def test_custom_request_header(self):
        request = make_request('cid-from-upstream', header_name='X_CUSTOM_HEADER')
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertEqual(request.correlation_id, 'cid-from-upstream')
        self.assertEqual(cid.locals.get_cid(), 'cid-from-upstream')
        self.assertEqual(response['X_CUSTOM_HEADER'], 'cid-from-upstream')

    @override_settings(CID_RESPONSE_HEADER='X_CUSTOM_HEADER')
    def test_custom_response_header(self):
        request = make_request('cid-from-upstream')
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertEqual(request.correlation_id, 'cid-from-upstream')
        self.assertEqual(cid.locals.get_cid(), 'cid-from-upstream')
        self.assertEqual(response['X_CUSTOM_HEADER'], 'cid-from-upstream')

    @override_settings(CID_RESPONSE_HEADER=None)
    def test_no_response_header(self):
        request = make_request('cid-from-upstream')
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertEqual(request.correlation_id, 'cid-from-upstream')
        self.assertEqual(cid.locals.get_cid(), 'cid-from-upstream')
        self.assertEqual(response.headers, {})


class TestIntegration(TestCase):

    def _test_integration(self):
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

    @override_settings(
        MIDDLEWARE=('cid.middleware.CidMiddleware', ),
        CID_GENERATE=True,
    )
    def test_integration(self):
        self._test_integration()

    @override_settings(
        MIDDLEWARE_CLASSES=('cid.middleware.CidOldStyleMiddleware', ),
        CID_GENERATE=True,
    )
    def test_integration_with_old_style_middleware_classes(self):
        self._test_integration()
