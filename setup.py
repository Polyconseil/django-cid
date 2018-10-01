from setuptools import setup, find_packages


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-cid',
    version='1.1.dev0',
    description="""Correlation IDs in Django for debugging requests""",
    long_description=readme + '\n\n' + history,
    author='Snowball One',
    author_email='opensource+django-cid@polyconseil.fr',
    maintainer="Polyconseil",
    maintainer_email="opensource+django-cid@polyconseil.fr",
    url='https://github.com/Polyconseil/django-cid',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=1.11',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django logging correlation id debugging',
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
