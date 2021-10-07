from datetime import date

from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class Publication(models.Model):

  name = models.CharField(verbose_name='naam', max_length=64)
  link = models.URLField(verbose_name='URL', max_length=64)
  image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True
  )

  def __str__(self):
    return f'{self.name}'

  class Meta:
    verbose_name = 'Pulicatie'
    verbose_name_plural = 'Pulicaties'

Publication.panels = [
  MultiFieldPanel([
    FieldPanel('name', classname='col8'),
    FieldPanel('link', classname='col8'),
    ImageChooserPanel('image', classname='col10'),
	], 
    heading='Publicatie info'
	)  
]