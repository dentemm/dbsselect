from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import (
  FieldPanel,
  MultiFieldPanel,
  InlinePanel,
  PageChooserPanel,
)

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from django_extensions.db.fields import AutoSlugField

class MenuItem(Orderable, ClusterableModel):

  link_title = models.CharField(
    blank=True,
    null=True,
    max_length=50
  )

  link_page = models.ForeignKey(
    'wagtailcore.Page',
    null=True,
    blank=False,
    related_name="+",
    on_delete=models.CASCADE,
  )

  menu = ParentalKey("Menu", related_name="menu_items", null=True)

  @property
  def link(self) -> str:
    return self.link_page.url

  @property
  def title(self) -> str:
    if self.link_page and not self.link_title:
      return self.link_page.title
    elif self.link_title:
      return self.link_title
    return 'Missing Title'

MenuItem.panels = [
  FieldPanel('link_title'),
  PageChooserPanel('link_page'),
]

# Main menu
@register_snippet
class Menu(ClusterableModel):

  title = models.CharField(max_length=100, default="")
  identifier = AutoSlugField(populate_from="title", editable=True, null=True)

  def __str__(self):
    return self.title

Menu.panels = [
  MultiFieldPanel([
    FieldPanel('title'),
    FieldPanel('identifier'),
  ], heading="Menu"),
  InlinePanel('menu_items', label="Menu Item")
]