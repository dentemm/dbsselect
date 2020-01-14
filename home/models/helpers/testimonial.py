from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel

from ..snippets.person import Person

class Testimonial(models.Model):

    text = models.TextField()
    person = models.Foreignkey(
        Person,
        on_delete=models.CASCADE,
        related_name='testimonials'
    )

    class Meta:
        verbose_name = 'Getuigenis'
        verbose_name_plural = 'Getuigenissen'
        
    # def __str__(self):
    #     return '%s - %s' % (self.city, self.street)
