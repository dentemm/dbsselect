from datetime import date

from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

LANGUAGE_CHOICES = (
    ('EN', 'English'),
    ('NL', 'Nederlands'),
    ('FR', 'Francais'),
    ('DE', 'Deutsch'),
)

@register_snippet
class Session(models.Model):

  date = models.DateField(verbose_name='Datum', default=date.today)
  link = models.URLField(verbose_name='URL', max_length=200)
  image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True
  )
  language = models.CharField(choices=LANGUAGE_CHOICES, default='EN', null=True, max_length=18)

  def __str__(self):
    return f'Sessie {self.date.strftime("%d %m")} ({self.language})'

  class Meta:
    verbose_name = 'Sessie'
    verbose_name_plural = 'Sessies'
    ordering = ['date']

Session.panels = [
  MultiFieldPanel([
    FieldPanel('date', classname='col8'),
    FieldPanel('link', classname='col8'),
    FieldPanel('language', classname='col8'),
    ImageChooserPanel('image', classname='col10'),
	], 
    heading='Persoonsgegevens'
	)  
]