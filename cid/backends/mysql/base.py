from django.db.backends.mysql.base import DatabaseWrapper as BaseMySQLWrapper

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseMySQLWrapper):

    def create_cursor(self, name):
        base_cursor = super(DatabaseWrapper, self).create_cursor(name)
        return CidCursorWrapper(base_cursor)
