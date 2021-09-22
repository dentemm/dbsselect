from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel, FieldRowPanel, FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtailcaptcha.models import WagtailCaptchaForm

from wagtailmedia.edit_handlers import MediaChooserPanel

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.models import ClusterableModel

from .snippets.partner import Partner
from .snippets.location import Location
from .snippets.person import Person
from .snippets.video import Video
from .snippets.testimonial import Testimonial
from .snippets.session import Session
from .snippets.press import Press
from .snippets.team import TeamMember

from .blocks.about_stream_block import AboutPageStreamBlock

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

class SessionsPageTestimonial(Orderable, models.Model):
    page = ParentalKey('home.SessionsPage', on_delete=models.CASCADE, related_name='testimonials')
    testimonial = models.ForeignKey(verbose_name='getuigenis', to=Testimonial, on_delete=models.CASCADE)

    class Meta:
        ordering = ['sort_order']
        unique_together = ('page', 'testimonial')

SessionsPageTestimonial.panels = [
    SnippetChooserPanel('testimonial')
]

class SessionsPageSession(Orderable, models.Model):
    page = ParentalKey('home.SessionsPage', on_delete=models.CASCADE, related_name='sessions')
    session = models.ForeignKey(verbose_name='sessie', to=Testimonial, on_delete=models.CASCADE)

    class Meta:
        ordering = ['sort_order']
        unique_together = ('page', 'session')

SessionsPageSession.panels = [
    SnippetChooserPanel('session')
]

class HomePageVideo(Orderable, Video):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='videos')
    
    class Meta:
        ordering = ['sort_order']

class HomePage(Page):

    video = models.ForeignKey(
        'wagtailmedia.Media',
        verbose_name='video',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subtitle = RichTextField('Ondertitel', null=True, features=['bold', ])
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
    )
    funded = models.CharField('Funded by', max_length=32, default='Project funded by')
    funded_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Afbeelding',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
    )

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
    what_file = models.ForeignKey(
        'wagtaildocs.Document',
        verbose_name='Bestand',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
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
    data_link = models.URLField('Link', null=True)

    # RichTextField('Beschrijving', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])

    # TESTIMONIALS
    testimonials_title = models.CharField('Getuigenissen', max_length=32, default='Testimonials')
    testimonials_subtitle = models.CharField('Ondertitel', max_length=64, default='from people participating in a DBS session')

    # MOVIE
    movie_title = models.CharField('Titel', max_length=64, null=True)
    movie_link = models.URLField('Link', null=True)

    # PARTNERS
    partners_title = models.CharField('Partners', max_length=32, default='Partners')

    # VIDEOS
    videos_title = models.CharField('Videos', max_length=32, default='More videos')
    videos_discription = models.CharField('Ondertitel', max_length=128, default="", blank=True)

HomePage.content_panels = [
    MultiFieldPanel(
        [
            FieldPanel('title', classname='col8'),
            FieldPanel('subtitle', classname='col8'),
            ImageChooserPanel('background_image', classname='col10'),
            MediaChooserPanel('video', classname='col10'),
            FieldPanel('funded', classname='col8'),
            ImageChooserPanel('funded_image', classname='col10')
        ],
        heading='Algemene informatie'
    ),
    MultiFieldPanel(
        [
            FieldPanel('what', classname='col8'),
            FieldPanel('what_info', classname='col8'),
            FieldPanel('download_text', classname='col8'),
            DocumentChooserPanel('what_file', classname='col8'),
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
            FieldPanel('data_link', classname='col8'),
            ImageChooserPanel('sessions_image', classname='col8')
        ],
        heading='Sectie 1: DBS Select sessies',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('testimonials_title', classname='col8'),
            FieldPanel('testimonials_title', classname='col8'),
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
    MultiFieldPanel([
        FieldPanel('videos_title', classname='col8'),
        FieldPanel('videos_discription', classname='col8'),
        InlinePanel('videos')
    ], 
        heading='Videos',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('partners_title', classname='col8'),
            InlinePanel('partners')
        ],
        heading='Partners',
        classname='collapsible collapsed'
    ), 
]

HomePage.parent_page_types = []
HomePage.subpage_types = ['home.SessionsPage', 'home.ContactPage', 'home.AboutPage', 'home.MediaPage']

class AboutPage(Page):

    video = models.ForeignKey(
        'wagtailmedia.Media',
        verbose_name='video',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content = StreamField(AboutPageStreamBlock(), null=True)

    block_1_title = models.CharField('titel', max_length=54, blank=True)
    block_1_description = models.TextField('beschrijving', blank=True)
    block_1_image = models.ForeignKey(
        verbose_name='Afbeelding',
        to='wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        blank=True
    )

    block_2_title = models.CharField('titel', max_length=54, blank=True)
    block_2_description = models.TextField('beschrijving', blank=True)
    block_2_image = models.ForeignKey(
        verbose_name='Afbeelding',
        to='wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        blank=True
    )

    block_3_title = models.CharField('titel', max_length=54, blank=True)
    block_3_description = models.TextField('beschrijving', blank=True)
    block_3_image = models.ForeignKey(
        verbose_name='Afbeelding',
        to='wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        blank=True
    )

    template = 'home/about_page.html'        

AboutPage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        MediaChooserPanel('video')
    ]),
    StreamFieldPanel('content'),
    # MultiFieldPanel([
    #     FieldPanel('block_1_title', classname='col9'),
    #     FieldPanel('block_1_description', classname='col9'),
    #     ImageChooserPanel('block_1_image', classname='col6')
    # ], heading="Deel 1"),
    # MultiFieldPanel([
    #     FieldPanel('block_2_title', classname='col9'),
    #     FieldPanel('block_2_description', classname='col9'),
    #     ImageChooserPanel('block_2_image', classname='col6')
    # ], heading="Deel 2"),
    # MultiFieldPanel([
    #     FieldPanel('block_3_title', classname='col9'),
    #     FieldPanel('block_3_description', classname='col9'),
    #     ImageChooserPanel('block_3_image', classname='col6')
    # ], heading="Deel 3")
]

class MediaPage(Page):

    media_title = models.CharField(verbose_name='titel media', default='Media', max_length=64)
    press_title = models.CharField(verbose_name='titel pers', default='Press', max_length=64)

    template = 'home/media_page.html'

    def press_articles(self):
        return Press.objects.all()

MediaPage.content_panels = Page.content_panels + [

]

MediaPage.parent_page_types = ['home.HomePage']
MediaPage.subpage_types = []


class SessionsPage(Page):

    # sessions = ParentalManyToManyField(verbose_name='sessies', to=Session, blank=True, null=True)
    pass

SessionsPage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        InlinePanel('testimonials')
    ], heading='Getuigenissen'),
     MultiFieldPanel([
        InlinePanel('sessions')
    ], heading='Sessies'),   
]

# HomePage.settings_panels = Page.settings_panels + [
#     FieldPanel('locale')
# ]

class ContactPageFormField(AbstractFormField):
    page = ParentalKey('home.ContactPage', related_name='form_fields')

class ContactPage(WagtailCaptchaForm, AbstractEmailForm):

    directions_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    send_button = models.CharField(verbose_name='verzend text', default='Verzenden', max_length=28)

    thank_you_text = models.CharField(verbose_name='success message', blank=True, max_length=160)

    class Meta:
        verbose_name = 'Contact page'
        verbose_name_plural = 'Contact pages'

ContactPage.content_panels = Page.content_panels + [
    MultiFieldPanel(
        [
            FieldPanel('subject', classname='col8'),
            FieldPanel('send_button', classname='col8'),
            FieldPanel('thank_you_text', classname='col8'),
            FieldRowPanel([
                FieldPanel('to_address', classname='col6'),
                FieldPanel('from_address', classname='col6')
            ])
        ],
        heading='Form configuration',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            InlinePanel('form_fields', label='Form fields'),
        ],
        heading='Form fields',
        classname='collapsible collapsed'
    )
]

ContactPage.parent_page_types = ['home.HomePage']
ContactPage.subpage_types = []

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

    favicon = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='favicon',
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
        ImageChooserPanel('logo_white'),
        ImageChooserPanel('favicon')
    ], 
        heading='Logos',
        classname='collapsible collapsed'
    ),
]