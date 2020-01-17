from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from .snippets.partner import Partner

class HomePagePartner(Orderable, Partner):

    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='partners')

    class Meta:
        ordering = ['sort_order']

# class HomePageTestimonial(Orderable, Testimonial):

#     page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='testimonials')


#     class Meta:
#         ordering = ['sort_order']


class HomePage(Page):

    subtitle = RichTextField('Ondertitle', null=True, features=['bold', ])

    # SECTION 1
    what = RichTextField('Wat?', null=True, features=['bold', ])
    what_info = RichTextField('Info', null=True, features=['bold', 'link', 'hr'])
    what_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Afbeelding',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
    )
    download_text = models.CharField('Download tekst', max_length=32, default='Download DBS Brochure')

    sessions = RichTextField('Sessies', null=True, features=['bold', ])
    sessions_info = RichTextField('Info', null=True, features=['bold', 'link', 'hr'])
    sessions_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Afbeelding',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
    )
    data_text = models.CharField('Data tekst', max_length=32, default='Check dates') 

    # RichTextField('Beschrijving', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])

    # content = StreamField(HomePageStreamBlock(), null=True)


HomePage.content_panels = [
    MultiFieldPanel(
        [
            FieldPanel('title', classname='col8'),
            FieldPanel('subtitle', classname='col8')
        ],
        heading='Algemene informatie'
    ),
    MultiFieldPanel(
        [
            FieldPanel('what', classname='col8'),
            FieldPanel('what_info', classname='col8'),
            FieldPanel('download_text', classname='col8'),
            ImageChooserPanel('what_image', classname='col8')
        ],
        heading='Sectie 1: wat is BDS?',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('sessions', classname='col8'),
            FieldPanel('sessions_info', classname='col8'),
            FieldPanel('data_text', classname='col8'),
            ImageChooserPanel('sessions_image', classname='col8')
        ],
        heading='Sectie 1: BDS Select sessies',
        classname='collapsible collapsed'
    ), 
    MultiFieldPanel(
        [
            InlinePanel('partners')
        ],
        heading='Partners',
        classname='collapsible'
    ), 
]


