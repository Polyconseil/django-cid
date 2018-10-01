from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'ok', views.ok, name='ok'),
    url(r'', views.testit, name='testit'),
)
