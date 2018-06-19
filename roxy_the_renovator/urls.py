from django.conf.urls import include, url
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from roxy_photologue import urls as roxy_photologue_urls


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^photologue/', include(roxy_photologue_urls, namespace='photologue')),
    url(r'^search/$', 'search.views.search', name='search'),

    url(r'', include(wagtail_urls)),
]
