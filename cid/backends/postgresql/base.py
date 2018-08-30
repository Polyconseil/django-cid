from django.db.backends.postgresql_psycopg2.base import (
    DatabaseWrapper as BasePostgresqlWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BasePostgresqlWrapper):

    def create_cursor(self, name=None):
        base_cursor = super().create_cursor(name)
        return CidCursorWrapper(base_cursor)
