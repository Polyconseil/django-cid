from django.db.backends.oracle.base import (
    DatabaseWrapper as BaseOracleWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseOracleWrapper):

    def create_cursor(self, name=None):
        if name:
            base_cursor = super(DatabaseWrapper, self).create_cursor(name)
        else:
            base_cursor = super(DatabaseWrapper, self).create_cursor()
        return CidCursorWrapper(base_cursor)
