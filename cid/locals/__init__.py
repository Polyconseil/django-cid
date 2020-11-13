try:
    # ContextVar is available since python 3.7,
    # Older versions of Python will use thread_local
    from .context import set_cid, get_cid  # noqa
except ImportError:
    from .thread_local import set_cid, get_cid  # noqa

from .base import generate_new_cid


__all__ = (
    'generate_new_cid',
    'set_cid',
    'get_cid',
)
