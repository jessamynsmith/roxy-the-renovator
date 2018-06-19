from django.conf.urls import include, patterns, url

from photologue import urls as photologue_urls

from .views import GalleryArchiveListView, GalleryListView


urlpatterns = patterns(
    '',
    url(r'', include(photologue_urls)),
    url(r'^gallerylist/$', GalleryListView.as_view(), name='gallery-list'),
    url(r'^gallerylist/archive/$', GalleryArchiveListView.as_view(),
        name='gallery-archive-list'),
)
