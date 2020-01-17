from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel

from ..helpers.address import Address


@register_snippet
class Location(Address):

    name = models.CharField(verbose_name='Naam', max_length=64)
    
    class Meta:
		    verbose_name = 'locatie'
		    verbose_name_plural = 'locaties'
		    ordering = ['name', ]
        
    def __str__(self):
		    return self.name
        
    @property
    def to_string(self):
		    return '%s %s %s' % (self.street, self.number, self.city)

Location.panels = [
	  MultiFieldPanel([
			  FieldRowPanel([
					  FieldPanel('name', classname='col6'),
				    ]	
			  ),
			  FieldRowPanel([
					  FieldPanel('street', classname='col8'),
					  FieldPanel('number', classname='col4')
          ]),
        FieldRowPanel([
            FieldPanel('city', classname='col8'),
            FieldPanel('postal_code', classname='col4')
        ])
    ], heading='Location details')
]