from threading import local
import uuid

from django.conf import settings


_thread_locals = local()


def set_cid(cid):
    """Set the correlation id for the current request."""
    setattr(_thread_locals, 'CID', cid)


def get_cid():
    """Return the currently set correlation id (if any).

    If no correlation id has been set and ``CID_GENERATE`` is enabled
    in the settings, a new correlation id is set and returned.
    """
    cid = getattr(_thread_locals, 'CID', None)
    if cid is None and getattr(settings, 'CID_GENERATE', False):
        cid = str(uuid.uuid4())
        set_cid(cid)
    return cid
