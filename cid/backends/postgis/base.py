from django.contrib.gis.db.backends.postgis.base import (
    DatabaseWrapper as BasePostgisWrapper
)

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BasePostgisWrapper):

    def create_cursor(self, *args, **kwargs):
        base_cursor = super(DatabaseWrapper, self).create_cursor(*args, **kwargs)
        return CidCursorWrapper(base_cursor)
