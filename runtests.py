#!/usr/bin/env python

# py.test test runner

import pytest
import sys
import coverage

if __name__ == '__main__':
    # Start coverage tracking
    cov = coverage.coverage()
    cov.start()

    # Run pytest
    if len(sys.argv) > 1:
        code = pytest.main(sys.argv)
    else:
        code = pytest.main(args=["-s", "--pep8"])

    # Show coverage report
    cov.stop()
    cov.save()
    cov.report()

    sys.exit(code)
