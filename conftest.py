import os
import sys

from django import conf
from django.core.files import temp as tempfile


sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sandbox'))


def location(x):
    os.path.join(os.path.dirname(os.path.realpath(__file__)), x)


def pytest_configure():
    BASE_SETTINGS = dict(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        DEBUG=False,
        SITE_ID=1,
        EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
        ROOT_URLCONF='sandbox.urls',

        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.admin',

            'cid.apps.CidAppConfig',
            'testapp',
        ],

        STATICFILES_DIRS=(location('static/'),),
        STATIC_ROOT=location('public'),
        STATIC_URL='/static/',
        MEDIA_ROOT=tempfile.gettempdir(),
        MEDIA_URL='/media/',

        TEMPLATE_CONTEXT_PROCESSORS=(
            "django.contrib.auth.context_processors.auth",
            "django.core.context_processors.request",
            "django.core.context_processors.debug",
            "django.core.context_processors.i18n",
            "django.core.context_processors.media",
            "django.core.context_processors.static",
            "django.contrib.messages.context_processors.messages",
        ),
        TEMPLATE_DIRS=(
            location('templates'),
        ),

        # Other settings go here
        LOGGING={
            'version': 1,
            'formatters': {
                'verbose': {
                    'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(cid)s %(message)s'  # noqa
                },
                'simple': {
                    'format': '%(levelname)s %(message)s'
                }
            },
            'filters': {
                'cid': {
                    '()': 'cid.log.CidContextFilter'
                }
            },
            'handlers': {
                'cid': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose',
                    'filters': ['cid']
                }
            },
            'loggers': {
                'cid': {
                    'handlers': ['cid'],
                    'propagate': True,
                    'level': 'DEBUG'
                }
            }
        }
    )
    conf.settings.configure(**BASE_SETTINGS)
