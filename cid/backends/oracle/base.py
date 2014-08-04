from django.db.backends.oracle.base import (
    DatabaseWrapper as BaseOracleWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseOracleWrapper):

    def create_cursor(self):
        base_cursor = super(DatabaseWrapper, self).create_cursor()
        return CidCursorWrapper(base_cursor)
