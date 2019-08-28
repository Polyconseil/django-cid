import logging

from django.conf import settings

from cid.locals import get_cid


class CidContextFilter(logging.Filter):

    def filter(self, record):
        setattr(record, getattr(settings, 'CID_LOG_RECORD_NAME', 'cid'), get_cid())
        return True
