from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel

from wagtailmedia.edit_handlers import MediaChooserPanel

@register_snippet
class Video(models.Model):

    description = models.TextField(verbose_name='Beschrijving', null=True, blank=True)
    video = models.ForeignKey(
        'wagtailmedia.Media',
        verbose_name='video',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    class Meta:
		    verbose_name = 'video'
		    verbose_name_plural = 'videos'
		    ordering = ['video', ]
        
    def __str__(self):
		    return self.title

Video.panels = [
	  MultiFieldPanel([
			  FieldRowPanel([
					  FieldPanel('description', classname='col12'),
        ]),
        MediaChooserPanel('video')

    ], heading='Video informatie')
]