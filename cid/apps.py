from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CidAppConfig(AppConfig):
    """
    Django 1.7+ application configuration
    """
    name = 'cid'
    verbose_name = _('Django Correlation Id')
