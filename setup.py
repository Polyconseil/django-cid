from setuptools import setup, find_packages


with open('README.rst', encoding="utf-8") as fp:
    readme = fp.read()

setup(
    name='django-cid',
    version='2.3',
    description="""Correlation IDs in Django for debugging requests""",
    long_description=readme,
    author='Snowball One',
    author_email='opensource+django-cid@polyconseil.fr',
    maintainer="Polyconseil",
    maintainer_email="opensource+django-cid@polyconseil.fr",
    url='https://github.com/Polyconseil/django-cid',
    packages=find_packages(exclude=('sandbox*', 'tests*')),
    include_package_data=True,
    install_requires=[
        'django>=2.2',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
