import os
import sys

import cid

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = cid.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-cid',
    version=version,
    description="""Correlation IDs in Django for debugging requests""",
    long_description=readme + '\n\n' + history,
    author='Snowball One',
    maintainer="Polyconseil",
    maintainer_email="opensource+django-cid@polyconseil.fr",
    url='https://github.com/snowball-digital/cid',
    packages=[
        'cid',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='cid',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
