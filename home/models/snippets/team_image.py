from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class TeamImage(models.Model):

  info = models.CharField(verbose_name='Naam', max_length=128, blank=True)
  image = models.ForeignKey(
    'wagtailimages.Image',
    verbose_name='Foto',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True
  )

  def __str__(self):
    return self.image

  class Meta:
    verbose_name = 'Team foto'
    verbose_name_plural = "Team foto's"

TeamImage.panels = [
  MultiFieldPanel([
    FieldPanel('info', classname='col8'),
    ImageChooserPanel('image', classname='col10'),
  ], heading='Info')  
]