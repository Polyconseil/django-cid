from django.db.backends.mysql.base import DatabaseWrapper as BaseMySQLWrapper

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseMySQLWrapper):

    def create_cursor(self, name=None):
        base_cursor = super().create_cursor(name)
        return CidCursorWrapper(base_cursor)
