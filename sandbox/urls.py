from django.conf.urls import include, url

from .views import ping_view


urlpatterns = [
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ping/$', ping_view, name='ping'),
    # url(r'^admin/', include(admin.site.urls)),
]
