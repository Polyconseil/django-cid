.. _usage:

=====
Usage
=====

Django Correlation Ids have a number of options for usage covering logging,
SQL comments, and a template context processor.

All of these rely on the usage of a piece of middleware. To configure the
middleware simply add the following to your list of MIDDLEWARE_CLASSES in
your settings file:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        'cid.middleware.CidMiddleware',
        # other middleware
    )

By default the middleware will look for the correlation id in an incoming
request header called ``X_CORRELATION_ID``. An alternative header name can be
used by putting a value into settings for the ``CID_HEADER``. e.g.:

.. code-block:: python

    CID_HEADER = 'X_MY_CID_HEADER'

.. note::

    Most WSGI implementations sanitize HTTP headers by appending an
    ``HTTP_`` prefix and replacing ``-`` by ``_``. For example, an
    incoming ``X-Correlation-Id`` header would be available as
    ``HTTP_X_CORRELATION_ID`` in Django. When using such a WSGI server
    in front of Django, the latter, sanitized value should be used in
    the settings.

You can also configure Django Correlation Id to generate its own correlation
id if one is not found in the header. For this set ``CID_GENERATE`` to true in
your settings file:

.. code-block:: python

    CID_GENERATE = True

By default, Django Correlation Id sets an HTTP header in the HTTP
response with the same name as configured in ``CID_HEADER``. You may
customize it with ``CID_RESPONSE_HEADER`` in the settings:

.. code-block:: python

    CID_RESPONSE_HEADER = 'X-Something-Completely-Different'

.. note::

    As indicated in the note above, if Django is behind a WSGI server
    that sanitizes HTTP headers, you need to customize
    ``CID_RESPONSE_HEADER`` to have the same header name in the
    response as in the request.

    .. code-block:: python

        # The header is ``X-Correlation-Id`` but is sanitized by the WSGI server.
        CID_HEADER = 'HTTP_X_CORRELATION_ID'
        # Don't use the default value (equal to CID_HEADER) for the response header.
        CID_RESPONSE_HEADER = 'X-Correlation-Id'

If you don't want the header to appear in the HTTP response, you must
explicitly set ``CID_REQUEST_HEADER`` to ``None``.

    .. code-block:: python

        # Don't include the header in the HTTP response.
        CID_RESPONSE_HEADER = None


SQL Comments
------------

To make use of the SQL comments support you will need to change your database
backend to one of the cid wrapped database backends. e.g. for sqlite3 you will
need to use the following:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'cid.backends.sqlite3',
            'NAME': location('db.sqlite3'),
        }
    }

The are database backend wrappers for all the currently support database
backends found in Django.

mysql
    cid.backends.mysql
oracle
    cid.backends.oracle
postgresql
    cid.backends.postgresql
sqlite3
    cid.backends.sqlite3


Logging
-------

To make use of the correlation id in logs you will need to add the cid log
filter to your settings and apply it to each logger.

e.g.

.. code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '[cid: %(cid)s] %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '[cid: %(cid)s] %(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/path/to/django/debug.log',
                'formatter': 'verbose',
            },
        },
        'filters': {
            'correlation': {
                (): 'cid.log.CidContextFilter'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
                'filters': ['correlation']
            },
        },
    }

You can then use your loggers as normal, safe in the knowledge that you can tie
them all back to the correlation id.


Template Context Processor
--------------------------

Django Correlation Id provides a template context processor which adds the
correlation id to the template context if it is available. To enable this you
will need to add the context processor to your settings:

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "cid.context_processos.cid_context_processor",
    )

This will place the context variable ``correlation_id`` in your template
context if a correlation id is available. For example you could add it as a
meta tag in your templates with the follwing snippet:

.. code-block:: django

    {% if correlation_id %}
        <meta name="correlation_id" content="{{ correlation_id }}" />
    {% endif %}
