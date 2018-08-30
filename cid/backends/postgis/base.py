from django.contrib.gis.db.backends.postgis.base import (
    DatabaseWrapper as BasePostgisWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BasePostgisWrapper):

    def create_cursor(self, name=None):
        base_cursor = super(DatabaseWrapper, self).create_cursor(name)
        return CidCursorWrapper(base_cursor)
