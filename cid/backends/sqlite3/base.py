from django.db.backends.sqlite3.base import (
    DatabaseWrapper as BaseSqliteWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseSqliteWrapper):

    def create_cursor(self):
        base_cursor = super(DatabaseWrapper, self).create_cursor()
        return CidCursorWrapper(base_cursor)
