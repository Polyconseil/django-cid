import logging

from cid.locals import get_cid


class CidContextFilter(logging.Filter):

    def filter(self, record):
        record.cid = get_cid()
        return True
