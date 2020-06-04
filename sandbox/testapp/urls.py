from django.urls import path

from . import views


urlpatterns = (
    path('ok', views.ok, name='ok'),
    path('', views.testit, name='testit'),
)
