from threading import local
import uuid

from django.conf import settings

_thread_locals = local()


def set_cid(cid):
    """
    Sets the Correlation Id for a a request
    """
    setattr(_thread_locals, 'CID', cid)


def get_cid():
    """
    Retrieves the currently set Correlation Id
    """
    cid = getattr(_thread_locals, 'CID', None)
    if cid is None and getattr(settings, 'CID_GENERATE', False):
        cid = str(uuid.uuid4())
        set_cid(cid)
    return cid
