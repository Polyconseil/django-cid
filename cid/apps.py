from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CidAppConfig(AppConfig):
    name = 'cid'
    verbose_name = _('Django Correlation Id')
