from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtail.core.fields import StreamField, RichTextField

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from .snippets.partner import Partner

class HomePagePartner(Orderable, Partner):

    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='partners')

    class Meta:
        ordering = ['sort_order']

class HomePageTestimonial(Orderable, Testimonial):

    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='testimonials')

    class Meta:
        ordering = ['sort_order']


class HomePage(Page):

    # content = StreamField(HomePageStreamBlock(), null=True)
    # partners = ClusterTaggableManager(through=HomePagePartner, blank=True)
    pass

HomePage.content_panels = Page.content_panels + [
    MultiFieldPanel(
        [
            InlinePanel('partners')
        ],
        heading='Partners',
        classname='collapsible'
    ), 
]


