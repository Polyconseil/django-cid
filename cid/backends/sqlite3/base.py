from django.db.backends.sqlite3.base import (
    DatabaseWrapper as BaseSqliteWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseSqliteWrapper):

    def create_cursor(self, name=None):
        if name:
            base_cursor = super(DatabaseWrapper, self).create_cursor(name)
        else:
            base_cursor = super(DatabaseWrapper, self).create_cursor()
        return CidCursorWrapper(base_cursor)
