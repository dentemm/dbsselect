from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class TeamMember(models.Model):

    name = models.CharField(verbose_name='Naam', max_length=64)
    title = models.CharField(verbose_name='Titel', max_length=128)
    text = models.CharField(verbose_name='Info', max_length=300)
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Foto',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teamlid'
        verbose_name_plural = 'Teamleden'

TeamMember.panels = [
  	MultiFieldPanel([
        FieldPanel('name', classname='col8'),
        FieldPanel('title', classname='col8'),
        FieldPanel('text', classname='col8'),
        ImageChooserPanel('image', classname='col10'),
    ], heading='Info')  
]