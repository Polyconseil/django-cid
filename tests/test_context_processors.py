from unittest import mock

from django.test import TestCase

from cid.context_processors import cid_context_processor


class TestContextProcessor(TestCase):

    @mock.patch('cid.context_processors.get_cid')
    def test_cid_added(self, get_cid):
        get_cid.return_value = 'a-text-cid'
        self.assertEqual(
            {'correlation_id': 'a-text-cid'},
            cid_context_processor(mock.Mock())
        )

    @mock.patch('cid.context_processors.get_cid')
    def test_cid_not_added_if_not_present(self, get_cid):
        get_cid.return_value = None
        self.assertEqual({}, cid_context_processor(mock.Mock()))
