from django.db.backends.postgresql_psycopg2.base import (
    DatabaseWrapper as BasePostgresqlWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BasePostgresqlWrapper):

    def create_cursor(self, name=None):
        if name:
            base_cursor = super(DatabaseWrapper, self).create_cursor(name)
        else:
            base_cursor = super(DatabaseWrapper, self).create_cursor()
        return CidCursorWrapper(base_cursor)
