from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = (
    url(r'^ping/$', views.ping_view, name='ping'),
    url(r'^admin/', admin.site.urls),
)
