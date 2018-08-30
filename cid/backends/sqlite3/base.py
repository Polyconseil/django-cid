from django.db.backends.sqlite3.base import (
    DatabaseWrapper as BaseSqliteWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseSqliteWrapper):

    def create_cursor(self, name):
        base_cursor = super().create_cursor(name)
        return CidCursorWrapper(base_cursor)
