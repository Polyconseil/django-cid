import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version, PackageNotFoundError
else:
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version('django-cid')
except PackageNotFoundError:
    raise PackageNotFoundError("The package `django-cid` is not properly installed.")
