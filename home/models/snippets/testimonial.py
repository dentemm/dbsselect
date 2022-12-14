from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .person import Person

@register_snippet
class Testimonial(models.Model):

  content = models.CharField(verbose_name='Getuigenis (EN)', max_length=512)
  content_nl = models.CharField(verbose_name='Getuigenis (NL)', max_length=512)
  content_fr = models.CharField(verbose_name='Getuigenis (FR)', max_length=512)
  content_de = models.CharField(verbose_name='Getuigenis (DE)', max_length=512)

  person = models.ForeignKey(to=Person, on_delete=models.CASCADE, related_name='+')

  def get_testimonial_content(self, language_code):

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
    return self.person.name

  class Meta:
    verbose_name = 'Getuigenis'
    verbose_name_plural = 'Getuigenissen'

Testimonial.panels = [
  MultiFieldPanel([
    FieldPanel('content', classname='col8'),
    FieldPanel('content_nl', classname='col8'),
    FieldPanel('content_fr', classname='col8'),
    FieldPanel('content_de', classname='col8'),
  ], heading='Inhoud'),
  SnippetChooserPanel('person')
]