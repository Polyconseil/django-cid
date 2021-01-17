from contextvars import ContextVar

from django.conf import settings

from .base import build_cid


correlation_id = ContextVar('correlation_id', default=None)


def set_cid(cid):
    """Set the correlation id on the context."""
    correlation_id.set(cid)


def get_cid():
    """Return the currently set correlation id (if any).
    """
    cid = correlation_id.get()
    if cid is None and getattr(settings, 'CID_GENERATE', False):
        cid = build_cid()
        set_cid(cid)
    return cid
