=======================
Releasing a new version
=======================

We use the excellent `zest.releaser`_ tool to make new releases. There
is a Makefile rule that does a bit more cleaning beforehand. Just
type::

    make release

And then follow the instructions.

We try to use `semantic versioning`_, i.e. use MAJOR.MINOR.PATCH
version numbers with:

- MAJOR version when we make incompatible API changes;
- MINOR version when we add functionality in a backwards-compatible manner;
- PATCH version when we make backwards-compatible bug fixes.

Although the distinction between MINOR and PATCH has not always been
followed, the changelog should be clear enough.


.. _zest.releaser: https://zestreleaser.readthedocs.io/en/latest/
.. _semantic versioning: https://semver.org/
