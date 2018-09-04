from django.conf import settings

from .locals import get_cid


DEFAULT_CID_SQL_COMMENT_TEMPLATE = 'cid: {cid}'


class CidCursorWrapper:
    """
    A cursor wrapper that attempts to add a cid comment to each query
    """
    def __init__(self, cursor):
        self.cursor = cursor

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def add_comment(self, sql):
        cid_sql_template = getattr(
            settings, 'CID_SQL_COMMENT_TEMPLATE', DEFAULT_CID_SQL_COMMENT_TEMPLATE
        )
        cid = get_cid()
        if not cid:
            return sql
        # FIXME (dbaty): we could use "--" prefixed comments so that
        # we would not have to bother with escaping the cid (assuming
        # it does not contain newline characters).
        cid = cid.replace('/*', r'\/\*').replace('*/', r'\*\/')
        return "/* {} */\n{}".format(cid_sql_template.format(cid=cid), sql)

    # The following methods cannot be implemented in __getattr__, because the
    # code must run when the method is invoked, not just when it is accessed.

    def callproc(self, procname, params=None):
        return self.cursor.callproc(procname, params)

    def execute(self, sql, params=None):
        sql = self.add_comment(sql)
        return self.cursor.execute(sql, params)

    def executemany(self, sql, param_list):
        sql = self.add_comment(sql)
        return self.cursor.executemany(sql, param_list)
