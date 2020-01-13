from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel

class Address(models.Model):

    city = models.CharField(verbose_name='plaats', max_length=40)
    postal_code = models.CharField(verbose_name='postcode', max_length=8)
    street = models.CharField(verbose_name='straat', max_length=40)
    number = models.CharField(verbose_name='huisnummer', max_length=8)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addressen'
        ordering = ['city', 'strees']
        
    def __str__(self):
        return '%s - %s' % (self.city, self.street)
