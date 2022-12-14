from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class Press(models.Model):

    title = models.CharField(verbose_name='titel (EN)', max_length=128)
    content = models.CharField(verbose_name='korte inhoud (EN)', max_length=512)

    title_nl = models.CharField(verbose_name='titel (NL)', max_length=128)
    content_nl = models.CharField(verbose_name='korte inhoud (NL)', max_length=512)

    title_fr = models.CharField(verbose_name='titel (FR)', max_length=128)
    content_fr = models.CharField(verbose_name='korte inhoud (FR)', max_length=512)

    title_de = models.CharField(verbose_name='titel (DE)', max_length=128)
    content_de = models.CharField(verbose_name='korte inhoud (DE)', max_length=512)

    url = models.URLField(verbose_name='link')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def get_title(self, language_code):

        if language_code == 'en':
            return self.title

        elif language_code == 'nl':
            return self.title_nl

        elif language_code == 'fr':
            return self.title_fr

        elif language_code == 'de':
            return self.title_de

        return self.title

    def get_content(self, language_code):

        if language_code == 'en':
            return self.content

        elif language_code == 'nl':
            return self.content_nl

        elif language_code == 'fr':
            return self.content_fr

        elif language_code == 'de':
            return self.content_de

        return self.content


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'pers artikel'
        verbose_name_plural = 'pers artikels'

Press.panels = [
  	MultiFieldPanel(
        [
            FieldPanel('title', classname='col8'),
            FieldPanel('content', classname='col8'),
            FieldPanel('title_nl', classname='col8'),
            FieldPanel('content_nl', classname='col8'),
            FieldPanel('title_fr', classname='col8'),
            FieldPanel('content_fr', classname='col8'),
            FieldPanel('title_de', classname='col8'),
            FieldPanel('content_de', classname='col8'),

            FieldPanel('url', classname='col6'),
            ImageChooserPanel('image', classname='col10'),
		], 
        heading='Pers artikel'
	  )  
]