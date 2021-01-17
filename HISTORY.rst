History
-------

2.2 (unreleased)
++++++++++++++++

- Add support of Django 3.1.

- Remove support of Python 3.5.

- Under Python 3.7 and later, use context variables (with the contextvars module)
  instead of a thread-local variable to avoid state bleeding in concurrent code.


2.1 (2020-06-22)
++++++++++++++++

* Add support of Django 3.0
* |backward-incompatible| Drop support of Django 2.1.


2.0 (2019-09-27)
++++++++++++++++

* |backward-incompatible| Drop support of Python 3.4.
* |backward-incompatible| Drop support of Django 1.11 and Django 2.0.
* Add ``CID_GENERATOR`` setting to allow the customization of the
  correlation id.


1.3 (2018-10-09)
++++++++++++++++

- **bugfix**: Fix packaging bug (introduced in version 1.2) that
  caused two extra packages ``tests`` and ``sandbox`` to be installed.


1.2 (2018-10-08)
++++++++++++++++

- **bugfix:** Fix bug (introduced in version 1.0) that caused the
  correlation id to be reused across all requests that were processed
  by the same thread.


1.1 (2018-10-01)
++++++++++++++++

- Allow to concatenate an upstream correlation id with a
  locally-generated one, with a new ``CID_CONCATENATE_IDS`` setting.


1.0 (2018-10-01)
++++++++++++++++

**Warning:** this release includes changes that are not backward
compatible. Be sure to read the details below to know if and how you
can migrate.

* |backward-incompatible| Drop support of Django 1.10 and earlier.

* |backward-incompatible| Drop support of Python 2.

* Add support of Django 2. Version 0.x could already be used with
  Django 2 but tests were not run against it. They now are.

* Generate cid outside of the middleware when ``GENERATE_CID`` is
  enabled, so that it's available even if the middleware is not used.

* Fix support of Django 1.11 in database backends.

* Add PostGIS database backend.

* Add ``CID_SQL_COMMENT_TEMPLATE`` to customize how the cid is
  included as comments in SQL queries.

* |backward-incompatible| Change the app name to be used in
  INSTALLED_APPS.

  **Migration from version 0.x:** if you had ``cid`` in ``INSTALLED_APPS``,
  replace it by ``cid.apps.CidAppConfig``. If you did not, add the
  latter.

* |backward-incompatible| Drop compatibility with
  ``MIDDLEWARE_CLASSES``.  You should use the ``MIDDLEWARE``
  setting. If you already did, no change is necessary.

  If you really must use the old ``MIDDLEWARE_CLASSES`` setting,
  include ``CidOldStyleMiddleware`` instead of ``CidMiddleware``.


0.2.0 (2016-12-06)
++++++++++++++++++

* Added support for Django 1.10 middleware (thanks @qbey)


0.1.2 (2016-12-01)
++++++++++++++++++

* Made CID repsonse header configurable, and optional (thanks @dbaty)

0.1.0 (2014-08-05)
++++++++++++++++++

* First release on PyPI.


.. role:: raw-html(raw)

.. |backward-incompatible| raw:: html

    <span style="background-color: #ffffbc; padding: 0.3em; font-weight: bold;">backward incompatible</span>
