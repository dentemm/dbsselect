from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

PARTNER_CHOICES = (
    (1, 'Project Partner'),
    (2, 'Supporting Partner'),
)

@register_snippet
class Partner(models.Model):

    name = models.CharField(verbose_name='Naam', max_length=64)
    url = models.URLField(verbose_name='Website', blank=True)
    description = models.TextField(verbose_name='Beschrijving', null=True, blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    partner_type = models.IntegerField(verbose_name='Partner type', choices=PARTNER_CHOICES, default=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

Partner.panels = [
  	MultiFieldPanel([
        FieldPanel('name', classname='col8'),
        FieldPanel('url', classname='col8'),
        ImageChooserPanel('logo', classname='col10'),
        FieldPanel('description', classname='col10'),
        FieldPanel('partner_type', classname='col8')
    ], heading='Partner informatie')  
]