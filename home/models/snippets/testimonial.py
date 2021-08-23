from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .person import Person

@register_snippet
class Testimonial(models.Model):

  content = models.CharField(verbose_name='Inhoud getuigenis', max_length=512)
  person = models.ForeignKey(to=Person, on_delete=models.CASCADE, related_name='+')

  def __str__(self):
    return self.person.name

  class Meta:
    verbose_name = 'Getuigenis'
    verbose_name_plural = 'Getuigenissen'

Testimonial.panels = [
  MultiFieldPanel([
    FieldPanel('content', classname='col8'),
  ], heading='Inhoud'),
  SnippetChooserPanel('person')
]