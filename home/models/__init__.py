from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel, FieldRowPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.models import ClusterableModel

from .snippets.partner import Partner
from .snippets.location import Location
from .snippets.person import Person

class HomePagePartner(Orderable, Partner):

    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='partners')

    class Meta:
        ordering = ['sort_order']

class HomePageTestimonial(Orderable, Person):

    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='testimonials')
    testimonial = RichTextField('getuigenis', null=True, features=['bold', ])

    class Meta:
        ordering = ['sort_order']

HomePageTestimonial.panels = Person.panels + [
    FieldPanel('testimonial')
]

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

    movie_title = models.CharField('Titel', max_length=64, null=True)
    movie_link = models.URLField('Link', null=True)


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
        heading='Sectie 1: wat is DBS?',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('sessions', classname='col8'),
            FieldPanel('sessions_info', classname='col8'),
            FieldPanel('data_text', classname='col8'),
            ImageChooserPanel('sessions_image', classname='col8')
        ],
        heading='Sectie 1: DBS Select sessies',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            InlinePanel('testimonials')
        ],
        heading='Sectie 2: Getuigenissen',
        classname='collapsible collapsed'
    ), 
    MultiFieldPanel(
        [
            FieldPanel('movie_title', classname='col8'),
            FieldPanel('movie_link', classname='col8'),
        ],
        heading='Sectie 3: DBS Select movie',
        classname='collapsible collapsed'
    ), 
    MultiFieldPanel(
        [
            InlinePanel('partners')
        ],
        heading='Partners',
        classname='collapsible collapsed'
    ), 
]


@register_setting
class BDSSelectSettings(ClusterableModel, BaseSetting):

    email = models.EmailField(null=True)

    logo = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='logo',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    logo_white = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='logo (wit)',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
        )

    error_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'DBS Select data'

BDSSelectSettings.panels = [
    MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('email', classname='col6'),
            ]),
            FieldRowPanel([
                FieldPanel('location', classname='col6')
            ])
        ], 
        heading='Algemene informatie'
    ),
    MultiFieldPanel([
        ImageChooserPanel('logo'),
        ImageChooserPanel('logo_white')
    ], 
        heading='Logos',
        classname='collapsible collapsed'
    ),
]