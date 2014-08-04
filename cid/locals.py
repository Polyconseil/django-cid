from threading import local


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
    return getattr(_thread_locals, 'CID', None)
