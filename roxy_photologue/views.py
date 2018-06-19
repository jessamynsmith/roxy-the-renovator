from django.views.generic.list import ListView
from photologue.models import Gallery


class GalleryArchiveListView(ListView):
    queryset = Gallery.objects.filter(is_public=False).on_site().order_by('title')
    paginate_by = 20
    template_name = 'photologue/gallery_archive_list.html'


class GalleryListView(ListView):
    queryset = Gallery.objects.on_site().is_public()
    paginate_by = 20
