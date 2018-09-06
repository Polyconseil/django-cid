============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of contributions
----------------------

Report bugs
~~~~~~~~~~~

Report bugs at https://github.com/Polyconseil/django-cid/issues.

If you are reporting a bug, please include:

* the versions of ``django-cid``, Django and Python;
* any details about your local setup that might be helpful in troubleshooting;
* detailed steps to reproduce the bug.


Write documentation
~~~~~~~~~~~~~~~~~~~

``django-cid`` could always use more documentation. Don't hesitate to
report typos or grammar correction.


Submit feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/Polyconseil/django-cid/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome. :)


Get started!
------------

Ready to contribute? Here's how to set up ``django-cid`` for local development.

1. Fork the ``django-cid`` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/django-cid.git

3. Set up a virtual environment and install the dependencies::

    $ pip install -e .
    $ pip install -r requirement/tests.txt

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

Now you can make your changes locally.

5. Test your changes locally by running ``make test``.

5. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

6. Submit a pull request through the GitHub website.


Sandbox project
---------------

The repository has a ``sandbox`` directory that contains a Django
project that showcases features and may help in testing and
debugging. It does not replace automated tests, though.

Install ``django-cid`` and you can run the server::

    $ cd sandbox
    $ ./manage.py runserver
    [...]
    Starting development server at http://127.0.0.1:8000/

The home page at `http://127.0.0.1:8000/ <http://127.0.0.1:8000/>`_ is self-documented.


Pull request guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all supported versions of Python and Django.
   Check https://travis-ci.org/Polyconseil/django-cid/pull_requests
   and make sure that the tests pass for all supported Python versions.
