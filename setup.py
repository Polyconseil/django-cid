from setuptools import setup, find_packages


def clean_history(history):
    # PyPI does not allow the `raw` directive. We'll laboriously
    # replace it. Hang tight, it's going to be ugly.
    history = history.replace('|backward-incompatible|', '**backward incompatible:** ')
    lines = []
    for line in history.split('\n'):
        if line.startswith('.. role:: raw-html'):
            break
        lines.append(line)
    return '\n'.join(lines)


readme = open('README.rst').read()
changelog = clean_history(open('HISTORY.rst').read())

setup(
    name='django-cid',
    version='2.2.dev0',
    description="""Correlation IDs in Django for debugging requests""",
    long_description=readme + '\n\n' + changelog,
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
