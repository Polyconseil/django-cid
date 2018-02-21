======================
Django Correlation IDs
======================

.. image:: https://travis-ci.org/snowball-one/cid.png?branch=master
    :target: https://travis-ci.org/snowball-one/cid

.. image:: https://coveralls.io/repos/snowball-one/cid/badge.png?branch=master
    :target: https://coveralls.io/r/snowball-one/cid?branch=master


Logging is important. Anyone who has had a call at 3am to say the site is down
knows this. Without quality logging it is almost impossible to work out what
on earth is happening.

Even with plenty of logs it can be hard to track down exactly what the effects
of a particular request are. Enter Django Correlation IDs. The approach
is quite a simple one. Incoming requests are assigned a unique id (a uuid).
This can either happen in say your public facing web server (e.g. nginx) or be
applied as soon as it hits django.

This ``cid`` is then available through the django request/response cycle. We
provide filters for logging witch adds the ``cid`` to the logging record so you
can add it to your formatting string. We also provide wrappers around all the
standard database backends which adds the ``cid`` as a comment before each SQL
request.

Features
--------

* Processing/Generation of a correlation id
* Database wrappers to add correlation id to each sql call
* Logging filter to inject the correlation id into logs
* A template context processor to make correlation id available in templates
* Output correlation id as a header

Documentation can be found at:  http://django-correlation-id.readthedocs.org/
