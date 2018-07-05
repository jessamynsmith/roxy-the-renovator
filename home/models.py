from __future__ import unicode_literals

from django.conf import settings

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from photologue.models import Gallery


class HomePage(Page):
    left_panel = RichTextField(blank=True)
    middle_panel = RichTextField(blank=True)
    right_panel = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('left_panel', classname="full"),
        FieldPanel('middle_panel', classname="full"),
        FieldPanel('right_panel', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        photos = Gallery.objects.get(slug=settings.SLIDE_SHOW_SLUG).photos.all()
        context['slide_show_photos'] = photos
        galleries = Gallery.objects.exclude(slug=settings.SLIDE_SHOW_SLUG)
        galleries = galleries.exclude(title__regex=settings.STARTS_WITH_NUMBER_REGEX)
        galleries = galleries.filter(photos__isnull=False).order_by("?")[:4]
        gallery_thumbnails = []
        for gallery in galleries:
            photo = gallery.photos.all().order_by("?")[0]
            photo.gallery_link = gallery.get_absolute_url()
            gallery_thumbnails.append(photo)
        gallery_iterator = iter(gallery_thumbnails)
        context['gallery_thumbnails'] = list(zip(gallery_iterator, gallery_iterator))
        return context
