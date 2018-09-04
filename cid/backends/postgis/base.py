from django.contrib.gis.db.backends.postgis.base import \
    DatabaseWrapper as BaseDatabaseWrapper

from ...cursor import CidCursorWrapper


class DatabaseWrapper(BaseDatabaseWrapper):
    # Don't warn about abstract `_start_transaction_under_autocommit`
    # pylint: disable=abstract-method

    def create_cursor(self, name=None):
        base_cursor = super().create_cursor(name)
        return CidCursorWrapper(base_cursor)
