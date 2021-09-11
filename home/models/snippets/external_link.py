from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class ExternalLink(models.Model):

    name_nl = models.CharField(verbose_name='naam_nl', max_length=64)
    name_en = models.CharField(verbose_name='naam_en', max_length=64)
    name_de = models.CharField(verbose_name='naam_dui', max_length=64)
    name_fr = models.CharField(verbose_name='naam_fr', max_length=64)

    link_name_nl = models.CharField(verbose_name='button nl', max_length=64)
    link_name_en = models.CharField(verbose_name='button en', max_length=64)
    link_name_de = models.CharField(verbose_name='button dui', max_length=64)
    link_name_fr = models.CharField(verbose_name='button fr', max_length=64)

    link = models.URLField(verbose_name='externe link', blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='afbeelding',
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

Partner.panels = [
  	MultiFieldPanel(
        [
            FieldPanel('name', classname='col8'),
            FieldPanel('url', classname='col8'),
            ImageChooserPanel('image', classname='col10'),
		], 
        heading='Studie / Externe link'
	)  
]