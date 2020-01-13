from django.db import models

from wagtail.snippets.models import register_snippet

@register_snippet
class Partner(models.Model):

    name = models.CharField(max_length=64)
    url = models.URLField(verbose_name='Website', blank=True)
    description = models.TextField(verbose_name='Beschrijving', null=True, blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
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
            FieldRowPanel([
                FieldPanel('name', classname='col6'),
                ImageChooserPanel('logo_white', classname='col6'),
            ]),
            FieldRowPanel([
                FieldPanel('url', classname='col6')
                
            ]),
            FieldRowPanel([
                FieldPanel('description', classname='col8'),
            ])
		], 
        heading='Partner informatie'
	)  
]