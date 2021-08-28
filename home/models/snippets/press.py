from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class Press(models.Model):

    title = models.CharField(verbose_name='titel', max_length=128)
    content = models.CharField(verbose_name='korte inhoud', max_length=512)
    url = models.URLField(verbose_name='link')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'pers artikel'
        verbose_name_plural = 'pers artikels'

Press.panels = [
  	MultiFieldPanel(
        [
            FieldPanel('title', classname='col8'),
            FieldPanel('content', classname='col8'),
            FieldPanel('link', classname='col6'),
            ImageChooserPanel('image', classname='col10'),

		], 
        heading='Pers artikel'
	  )  
]