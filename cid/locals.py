from threading import local

_thread_locals = local()


def set_cid(cid):
    setattr(_thread_locals, 'CID', cid)


def get_cid():
    return getattr(_thread_locals, 'CID', None)


