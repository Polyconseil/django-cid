from django.db.backends.oracle.base import (
    DatabaseWrapper as BaseOracleWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseOracleWrapper):

    def create_cursor(self, name=None):
        base_cursor = super().create_cursor(name)
        return CidCursorWrapper(base_cursor)
