from datetime import date

from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class Session(models.Model):

  date = models.DateField(verbose_name='Datum', default=date.today)
  link = models.URLField(verbose_name='URL', max_length=64)
  image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True
  )

  def __str__(self):
    return f'Sessie {self.date.strftime("%d %m")}'

  class Meta:
    verbose_name = 'Sessie'
    verbose_name_plural = 'Sessies'

Session.panels = [
  MultiFieldPanel([
    FieldPanel('date', classname='col8'),
    FieldPanel('link', classname='col8'),
    ImageChooserPanel('image', classname='col10'),
	], 
    heading='Persoonsgegevens'
	)  
]