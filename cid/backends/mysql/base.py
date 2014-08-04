from django.db.backends.mysql.base import DatabaseWrapper as BaseMySQLWrapper

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseMySQLWrapper):

    def create_cursor(self):
        base_cursor = super(DatabaseWrapper, self).create_cursor()
        return CidCursorWrapper(base_cursor)
