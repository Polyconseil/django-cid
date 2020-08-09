import uuid

from django.conf import settings


def generate_new_cid(upstream_cid=None):
    """Generate a new correlation id, possibly based on the given one."""
    if upstream_cid is None:
        return build_cid() if getattr(settings, 'CID_GENERATE', False) else None
    if (
            getattr(settings, 'CID_CONCATENATE_IDS', False)
            and getattr(settings, 'CID_GENERATE', False)
    ):
        return '%s, %s' % (upstream_cid, build_cid())
    return upstream_cid


def build_cid():
    """Build a new cid"""
    return str(getattr(settings, 'CID_GENERATOR', uuid.uuid4)())
