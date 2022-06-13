from .locals import get_cid


def cid_context_processor(request):
    """
    Adds the correlation id as ``correlation_id`` to template contexts
    """
    cid = get_cid()
    if cid:
        return {'correlation_id': get_cid()}
    return {}
