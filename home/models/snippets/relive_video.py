from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

@register_snippet
class ReliveVideo(models.Model):

  title_en = models.CharField(max_length=64, null=True)
  title_nl = models.CharField(max_length=64, null=True)
  title_fr = models.CharField(max_length=64, null=True)

  link_en = models.URLField(null=True)
  link_nl = models.URLField(null=True)
  link_fr = models.URLField(null=True)

  class Meta:
    verbose_name = 'Relive video'
    verbose_name_plural = 'Relive videos'
      
  def __str__(self):
    return self.title_en

ReliveVideo.panels = [
	MultiFieldPanel([
    FieldPanel('title_en', classname='col12'),
    FieldPanel('title_nl', classname='col12'),
    FieldPanel('title_fr', classname='col12'),
    FieldPanel('link_en', classname='col12'),
    FieldPanel('link_nl', classname='col12'),
    FieldPanel('link_fr', classname='col12'),
    
  ], heading='Video informatie')
]