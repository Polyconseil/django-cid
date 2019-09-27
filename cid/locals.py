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

    FIXME (dbaty): in version 2, just `return getattr(_thread_locals, 'CID', None)`
    We want the simplest thing here and let `generate_new_cid` do the job.
    """
    cid = getattr(_thread_locals, 'CID', None)
    if cid is None and getattr(settings, 'CID_GENERATE', False):
        cid = _build_cid()
        set_cid(cid)
    return cid


def generate_new_cid(upstream_cid=None):
    """Generate a new correlation id, possibly based on the given one."""
    if upstream_cid is None:
        return _build_cid() if getattr(settings, 'CID_GENERATE', False) else None
    if (
            getattr(settings, 'CID_CONCATENATE_IDS', False)
            and getattr(settings, 'CID_GENERATE', False)
    ):
        return '%s, %s' % (upstream_cid, _build_cid())
    return upstream_cid


def _build_cid():
    """Build a new cid"""
    return str(getattr(settings, 'CID_GENERATOR', uuid.uuid4)())
