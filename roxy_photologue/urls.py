from django.conf.urls import include, patterns, url

from photologue import urls as photologue_urls

from .views import GalleryArchiveListView, GalleryListView


urlpatterns = patterns(
    '',
    url(r'', include(photologue_urls)),
    # I should be able to have this set to /gallerylist/ and have it override the one
    # in photologue, but it didn't work.
    url(r'^gallerylist/current/$', GalleryListView.as_view(), name='gallery-list'),
    url(r'^gallerylist/archive/$', GalleryArchiveListView.as_view(),
        name='gallery-archive-list'),
)
