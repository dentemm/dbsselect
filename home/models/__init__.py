from datetime import datetime

from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel, FieldRowPanel, FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtailmedia.edit_handlers import MediaChooserPanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from .snippets.partner import Partner
from .snippets.location import Location
from .snippets.person import Person
from .snippets.video import Video
from .snippets.relive_video import ReliveVideo
from .snippets.testimonial import Testimonial
from .snippets.session import Session
from .snippets.press import Press
from .snippets.team import TeamMember
from .snippets.publication import Publication

from .blocks.about_stream_block import AboutPageStreamBlock

class HomePagePartner(Orderable, Partner):

    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='partners')

    class Meta:
        ordering = ['sort_order']

class HomePageImage(Orderable, models.Model):

    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='afbeelding',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
    )

HomePageImage.panels = [
    MultiFieldPanel([
        ImageChooserPanel('image')
    ], heading='Afbeelding')
]

class HomePageTestimonial(Orderable, Person):

    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='testimonials')
    testimonial = RichTextField('getuigenis', null=True, features=['bold', ])

    class Meta:
        ordering = ['sort_order']

HomePageTestimonial.panels = Person.panels + [
    FieldPanel('testimonial')
]

class SessionsPageImage(Orderable, models.Model):

    page = ParentalKey('home.SessionsPage', on_delete=models.CASCADE, related_name='gallery')
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='afbeelding',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
    )

SessionsPageImage.panels = [
    ImageChooserPanel('image')
]

class HomePageVideo(Orderable, Video):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='videos')
    
    class Meta:
        ordering = ['sort_order']

class HomePage(Page):

    template = 'home/home_new.html'

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

    # NEW PAGE
    info_text = models.TextField('DBS info', default='', null=True)

    # CHILD PAGES
    info_page = models.ForeignKey(
        'home.AboutPage',
        verbose_name='wat is DBS pagina',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    sessions_page = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name='sessies pagina',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    media_page = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name='media pagina',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    contact_page = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name='contact pagina',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
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

    def project_partners(self):
        return Partner.objects.filter(partner_type=1)

    def supporting_partners(self):
        return Partner.objects.filter(partner_type=2)

    # VIDEOS
    videos_title = models.CharField('Videos', max_length=32, default='More videos')
    videos_discription = models.CharField('Ondertitel', max_length=128, default="", blank=True)

HomePage.content_panels = [
    MultiFieldPanel([
        FieldPanel('title', classname='col8'),
        FieldPanel('subtitle', classname='col8'),
        ImageChooserPanel('background_image', classname='col10'),
        MediaChooserPanel('video', classname='col10'),
        FieldPanel('funded', classname='col8'),
        ImageChooserPanel('funded_image', classname='col10')
    ], heading='Algemene informatie'),
    # MultiFieldPanel([
    #     PageChooserPanel('about_page', 'home.AboutPage'),
    #     PageChooserPanel('sessions_page', 'home.SessionsPage'),
    #     PageChooserPanel('media_page', 'home.MediaPage'),
    #     PageChooserPanel('contact_page', 'home.ContactPage'),

    # ], heading="Andere pagina's"),
    MultiFieldPanel([
        FieldPanel('info_text', classname='col10'),
    ], heading="New website", classname='collapsible collapsed'),
    MultiFieldPanel([
        InlinePanel('images'),
    ], heading="Afbeeldingen", classname='collapsible collapsed'),
    MultiFieldPanel([
        FieldPanel('what', classname='col8'),
        FieldPanel('what_info', classname='col8'),
        FieldPanel('download_text', classname='col8'),
        DocumentChooserPanel('what_file', classname='col8'),
        ImageChooserPanel('what_image', classname='col8')
    ], heading='Sectie 1: wat is DBS?', classname='collapsible collapsed'),
    MultiFieldPanel([
        FieldPanel('sessions', classname='col8'),
        FieldPanel('sessions_info', classname='col8'),
        FieldPanel('data_text', classname='col8'),
        FieldPanel('data_link', classname='col8'),
        ImageChooserPanel('sessions_image', classname='col8')
    ], heading='Sectie 1: DBS Select sessies', classname='collapsible collapsed'),
    MultiFieldPanel([
        FieldPanel('testimonials_title', classname='col8'),
        FieldPanel('testimonials_title', classname='col8'),
        InlinePanel('testimonials')
    ], heading='Sectie 2: Getuigenissen', classname='collapsible collapsed'), 
    MultiFieldPanel([
        FieldPanel('movie_title', classname='col8'),
        FieldPanel('movie_link', classname='col8'),
    ], heading='Sectie 3: DBS Select movie', classname='collapsible collapsed'), 
    MultiFieldPanel([
        FieldPanel('videos_title', classname='col8'),
        FieldPanel('videos_discription', classname='col8'),
        InlinePanel('videos')
    ], heading='Videos', classname='collapsible collapsed'),
    MultiFieldPanel([
        FieldPanel('partners_title', classname='col8'),
        InlinePanel('partners')
    ], heading='Partners', classname='collapsible collapsed'), 
]

HomePage.parent_page_types = []
HomePage.subpage_types = ['home.SessionsPage', 'home.ContactPage', 'home.AboutPage', 'home.MediaPage', 'home.RelivePage', 'home.HomePageNew', 'home.NewAboutPage']

class HomePageNew(Page):

    template = 'home/home_new.html'

    def get_data(self):
        return HomePage.objects.first()

HomePageNew.parent_page_types = ['home.HomePage']
HomePageNew.subpage_types = ['home.SessionsPage', 'home.ContactPage', 'home.AboutPage', 'home.MediaPage', 'home.RelivePage', 'home.HomePageNew', 'home.NewAboutPage']

class AboutPage(Page):

    video = models.ForeignKey(
        'wagtailmedia.Media',
        verbose_name='video',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subscription_link = models.URLField(verbose_name='inschrijvingslink', null=True, blank=True)
    subscription_link_text = models.CharField(verbose_name='tekst voor link', null=True, default='Schrijf je hier in', max_length=64)

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
    ], heading='Video'),
    MultiFieldPanel([
        FieldPanel('subscription_link', classname='col8'),
        FieldPanel('subscription_link_text', classname='col8'),
    ], heading='Video'), 
    StreamFieldPanel('content'),
]

class MediaPage(Page):

    media_title = models.CharField(verbose_name='titel media', default='Media', max_length=64)
    press_title = models.CharField(verbose_name='titel pers', default='Press', max_length=64)

    template = 'home/media_page.html'

    def press_articles(self):
        return Press.objects.all()

MediaPage.content_panels = Page.content_panels + []

MediaPage.parent_page_types = ['home.HomePage']
MediaPage.subpage_types = []

class SessionsPage(Page):

    video = models.URLField(verbose_name='video link', default='https://storage.googleapis.com/coverr-main/mp4/Mt_Baker.mp4')

    subtitle = models.CharField(verbose_name='ondertitel', default='Info over sessies', max_length=64)
    info = models.TextField(verbose_name='info tekst', blank=True, default='')
    subscribe_link = models.URLField(verbose_name='inschrijf link', default='https://www.google.be')
    subscribe_text = models.CharField(verbose_name='link test', default='Schrijf je hier in voor een sessie', max_length=64)

    upcoming_sessions_title = models.CharField(verbose_name='Komende sessies titel', default='Komende sessies', max_length=64)
    subscribe_button = models.CharField(verbose_name='Button tekst', default='Schrijf je in', max_length=64)

    subtitle_calendar = models.CharField(verbose_name='ondertitel', default='Aankomende sessies', max_length=64)

    def upcoming_sessions(self):

        reference = datetime.today()
        return Session.objects.filter(date__gte=reference)

    def testimonials(self):
        return Testimonial.objects.all()

SessionsPage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        FieldPanel('video', classname='col8')
    ], heading='Video'),
    MultiFieldPanel([
        FieldPanel('subtitle', classname='col8'),
        FieldPanel('info', classname='col8'),
        FieldPanel('subscribe_link', classname='col8'),
        FieldPanel('subscribe_text', classname='col8'),
        FieldPanel('subtitle_calendar', classname='col8')
    ], heading='Info'),
    MultiFieldPanel([
        InlinePanel('gallery')
    ], heading='afbeeldingen')
]

class ContactPageTeamMember(Orderable, TeamMember):
    page = ParentalKey('home.ContactPage', on_delete=models.CASCADE, related_name='team')

ContactPageTeamMember.panels = TeamMember.panels

class ContactPageFormField(AbstractFormField):
    page = ParentalKey('home.ContactPage', related_name='form_fields')

class ContactPage(AbstractEmailForm):

    directions_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    send_button = models.CharField(verbose_name='verzend text', default='Verzenden', max_length=28)

    thank_you_text = models.CharField(verbose_name='success message', blank=True, max_length=160)

    team_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    team_text = models.TextField(null=True, blank=True)

    def get_landing_page_template(self, request, *args, **kwargs):
      return self.template

    class Meta:
        verbose_name = 'Contact page'
        verbose_name_plural = 'Contact pages'

ContactPage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        ImageChooserPanel('directions_image')
    ]),
    MultiFieldPanel([
        FieldPanel('subject', classname='col8'),
        FieldPanel('send_button', classname='col8'),
        FieldPanel('thank_you_text', classname='col8'),
        FieldRowPanel([
            FieldPanel('to_address', classname='col6'),
            FieldPanel('from_address', classname='col6')
        ])
    ], heading='Form configuration', classname='collapsible collapsed'),
    MultiFieldPanel([
        InlinePanel('form_fields', label='Form fields'),
    ], heading='Form fields', classname='collapsible collapsed'),
    MultiFieldPanel([
        InlinePanel('team', label='Team members'),
    ], heading='Team members', classname='collapsible collapsed')
]

ContactPage.parent_page_types = ['home.HomePage']
ContactPage.subpage_types = []

class RelivePageImage(Orderable, models.Model):

    page = ParentalKey('home.RelivePage', on_delete=models.CASCADE, related_name='gallery')
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='afbeelding',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
    )

RelivePageImage.panels = [
    ImageChooserPanel('image')
]

class RelivePage(Page):

    subtitle = models.CharField(verbose_name='ondertitel', max_length=64, default='info over DBS')
    info = models.TextField(verbose_name='info tekst', default='Lorem ipsum')

    download_text = models.CharField(verbose_name='Download tekst', max_length=64, default='Download de info brochure')
    download_file = models.ForeignKey(
        'wagtaildocs.Document',
        verbose_name='Download bestand',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )
    read_more = models.CharField(verbose_name='Lees meer', max_length=64)

    subtitle_relive = models.CharField(verbose_name='herbeleef titel', max_length=64, default='Herbeleef de DBS rondleiding')
    subtitle_publication = models.CharField(verbose_name='publicaties titel', max_length=64, default='Externe studies')

    def publications(self):
        return Publication.objects.all()

    def get_videos(self):
        return ReliveVideo.objects.all()

    class Meta:
        verbose_name = 'Relive page'
        verbose_name_plural = 'Relive pages'
    
RelivePage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        FieldPanel('subtitle', classname='col8'),
        FieldPanel('subtitle_relive', classname='col8'),
        FieldPanel('subtitle_publication', classname='col8'),
        FieldPanel('info', classname='col8'),
        FieldPanel('read_more', classname='col8'),
        FieldPanel('download_text', classname='col8'),
        DocumentChooserPanel('download_file', classname='col8'),
    ], heading='Inhoud'),
    MultiFieldPanel([
        InlinePanel('gallery')
    ], heading='afbeeldingen'),
]

RelivePage.parent_page_types = ['home.HomePage']
RelivePage.subpage_types = []

class NewAboutPage(Page):

    template = 'home/new_about_page.html'

    info = RichTextField('Info', null=True, features=['bold', 'link', 'hr'])

NewAboutPage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        FieldPanel('info', classname='col8'),
    ], heading='Inhoud'),
]

NewAboutPage.parent_page_types = ['home.HomePage']
NewAboutPage.subpage_types = []

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
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('email', classname='col6'),
        ]),
        FieldRowPanel([
            FieldPanel('location', classname='col6')
        ])
    ], heading='Algemene informatie'),
    MultiFieldPanel([
        ImageChooserPanel('logo'),
        ImageChooserPanel('logo_white'),
        ImageChooserPanel('favicon')
    ], heading='Logos', classname='collapsible collapsed'),
]