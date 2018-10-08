import unittest
from unittest import mock

from django import VERSION as DJANGO_VERSION
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse

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

    def setUp(self):
        super().setUp()
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
        uuid4.return_value = 'first-cid'
        request = make_request(cid=None)
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertEqual(request.correlation_id, 'first-cid')
        self.assertEqual(cid.locals.get_cid(), 'first-cid')
        self.assertEqual(response['X_CORRELATION_ID'], 'first-cid')

        uuid4.return_value = 'second-cid'
        request = make_request(cid=None)
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertEqual(request.correlation_id, 'second-cid')
        self.assertEqual(cid.locals.get_cid(), 'second-cid')
        self.assertEqual(response['X_CORRELATION_ID'], 'second-cid')

    @override_settings(CID_GENERATE=True, CID_CONCATENATE_IDS=True)
    @mock.patch('uuid.uuid4')
    def test_concatenate_ids(self, uuid4):
        uuid4.return_value = 'local-cid'
        request = make_request(cid='upstream-cid')
        middleware = CidMiddleware(get_response=get_response)
        response = middleware(request)
        self.assertEqual(request.correlation_id, 'upstream-cid, local-cid')
        self.assertEqual(cid.locals.get_cid(), 'upstream-cid, local-cid')
        self.assertEqual(response['X_CORRELATION_ID'], 'upstream-cid, local-cid')

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
        url = reverse('ok')  # comes from sandbox/testapp

        # A request without any correlation id
        response = self.client.get(url)
        cid = response.get('X_CORRELATION_ID')
        self.assertIsNotNone(cid)

        # A request *with* a correlation id
        response = self.client.get(url, **{'X_CORRELATION_ID': cid})
        self.assertEqual(response['X_CORRELATION_ID'], cid)

    @override_settings(
        MIDDLEWARE=('cid.middleware.CidMiddleware', ),
        CID_GENERATE=True,
    )
    def test_integration(self):
        self._test_integration()

    @unittest.skipIf(
        DJANGO_VERSION[:2] >= (2, 0),
        "Support of MIDDLEWARE_CLASSES has been removed in Django 2")
    @override_settings(
        MIDDLEWARE_CLASSES=('cid.middleware.CidOldStyleMiddleware', ),
        CID_GENERATE=True,
    )
    def test_integration_with_old_style_middleware_classes(self):
        self._test_integration()
