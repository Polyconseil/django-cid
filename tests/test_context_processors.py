from django.test import TestCase
from mock import Mock, patch

from cid.context_processors import cid_context_processor


class TestContextProcessor(TestCase):

    @patch('cid.context_processors.get_cid')
    def test_cid_added(self, get_cid):
        get_cid.return_value = 'a-text-cid'
        self.assertEquals(
            {'correlation_id': 'a-text-cid'},
            cid_context_processor(Mock())
        )

    @patch('cid.context_processors.get_cid')
    def test_cid_not_added_if_not_present(self, get_cid):
        get_cid.return_value = None
        self.assertEquals({}, cid_context_processor(Mock()))
