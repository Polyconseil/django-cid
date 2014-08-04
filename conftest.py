import os
import sys

from django.conf import settings
from django.core.files import temp as tempfile
# from django.utils.translation import ugettext_lazy as _


sys.path.insert(0, os.path.dirname(__file__))

location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)  # noqa


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
            'django.contrib.flatpages',
            'cid',
        ],

        MIDDLEWARE_CLASSES=(
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ),

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
    )
    settings.configure(**BASE_SETTINGS)
