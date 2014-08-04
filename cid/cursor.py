from .locals import get_cid


class CidCursorWrapper(object):
    """
    A cursor wrapper that attempts to add a cid comment to each query
    """
    def __init__(self, cursor):
        self.cursor = cursor

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def add_comment(self, sql):
        cid = get_cid()
        if cid:
            cid = cid.replace('/*', '\/\*').replace('*/', '\*\/')
            return "/* cid: {} */\n{}".format(cid, sql)
        return sql

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
