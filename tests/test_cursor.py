from django.test import TestCase
from mock import Mock, patch

from cid.cursor import CidCursorWrapper


class TestCidCursor(TestCase):

    def setUp(self):
        self.cursor = Mock()
        self.cursor.execute = Mock(return_value=None)
        self.cursor.executemany = Mock(return_value=None)
        self.cursor_wrapper = CidCursorWrapper(self.cursor)

    @patch('cid.cursor.get_cid')
    def test_adds_comment(self, get_cid):
        get_cid.return_value = 'testing-cursor'
        expected = "/* cid: testing-cursor */\nSELECT 1;"
        self.assertEqual(
            expected,
            self.cursor_wrapper.add_comment("SELECT 1;")
        )

    @patch('cid.cursor.get_cid')
    def test_no_comment_when_cid_is_none(self, get_cid):
        get_cid.return_value = None
        expected = "SELECT 1;"
        self.assertEqual(
            expected,
            self.cursor_wrapper.add_comment("SELECT 1;")
        )

    @patch('cid.cursor.CidCursorWrapper.add_comment')
    def test_execute_calls_add_comment(self, add_comment):
        sql = "SELECT 1;"
        self.cursor_wrapper.execute(sql)
        add_comment.assert_called_with(sql)

    @patch('cid.cursor.CidCursorWrapper.add_comment')
    def test_executemany_calls_add_comment(self, add_comment):
        sql = "SELECT 1;"
        self.cursor_wrapper.executemany(sql, [])
        add_comment.assert_called_with(sql)
