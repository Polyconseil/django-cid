============
Installation
============

At the command line::

    $ pip install django-cid

You will need to add ``cid`` to your list of installed apps.

.. code-block:: python

    INSTALLED_APPS = (
        # some apps
        'cid',
        # some other apps
    )

For more information on how to actually make use of Django Correlation Id see
the :ref:`usage` section.

Correlation ID Generation
-------------------------

Django correlation id can handle the generation of correlation id in a couple
of different ways. Either internally or from an incoming header.

To use the internal generator you will need to set ``CID_GENERATE`` to true in
you settings file:

.. code-block:: python

    CID_GENERATE = True

This approach is perfectly acceptable but does suffer one drawback. If you host
your django application behind another web server such as nginx, then the nginx
logs won't contain the correlation id. Django Correlation Id can handle this
situation by extracting a correlation id created in nginx and passed through as
a header in the HTTP request. By default Django Correlation Id will look for
the header ``X_CORRELATION_ID``, but you can change this with the
``CID_HEADER`` settings.

A simple way to generate the correlation id in nginx is to use one of the
available built in scripting languages. e.g. the embedded perl.

One Ubuntu and Debian systems this requires the installation of
``nginx-extras`` and ``libossp-uuid-perl``.

.. code-block:: bash

    sudo apt-get install nginx-extras libossp-uuid-perl


And then a couple of configuration changes.

in /etc/nginx.conf you will need to add the following within the http section:

.. code-block:: none

    http {
        perl_require "Data/UUID.pm";
        perl_set $uuid 'sub {
            $ug = new Data::UUID;
            $str = $ug->create_str();
            return $str;
        }';

        # Remaining http config
    }

This tell nginx to generate uuids. The next step is to assign them to your
proxy or uwsgi pass through for you application. This is done within a server
block of your site configuration

.. code-block:: none

    server {
        proxy_set_header    X-Correlation-Id    $uuid;

        # Remainder of site config
    }
