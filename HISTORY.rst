.. :changelog:

History
-------

0.1.0 (2014-08-05)
++++++++++++++++++

* First release on PyPI.

0.1.2 (2016-12-01)
++++++++++++++++++

* Made CID repsonse header configurable, and optional (thanks @dbaty)

0.2.0 (2016-12-06)
++++++++++++++++++

* Added support for Django 1.10 middleware (thanks @qbey)

1.0 (unreleased)
++++++++++++++++

* Drop support of Django < 1.11.
* Drop support of Python 2.
* Generate cid outside of the middleware when ``GENERATE_CID`` is
  enabled, so that it's available even if the middleware is not used
* Fix support of Django 1.11 in database backends.
