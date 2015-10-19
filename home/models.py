from __future__ import unicode_literals

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

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['slide_show_photos'] = Gallery.objects.get(slug='slide-show').photos.all()
        return context
