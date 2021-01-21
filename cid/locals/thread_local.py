from threading import local

from django.conf import settings

from .base import build_cid


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
        cid = build_cid()
        set_cid(cid)
    return cid
