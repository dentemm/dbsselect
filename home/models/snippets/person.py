from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class Person(models.Model):

    name = models.CharField(verbose_name='Naam', max_length=64)
    info = models.CharField(verbose_name='Info', max_length=64)
    age = models.IntegerField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Persoon'
        verbose_name_plural = 'Personen'

Person.panels = [
  	MultiFieldPanel(
        [
            FieldPanel('name', classname='col8'),
            FieldPanel('info', classname='col8'),
            FieldPanel('age', classname='col6'),
            ImageChooserPanel('image', classname='col10'),

		], 
        heading='Persoonsgegevens'
	  )  
]