from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField

class HomePage(Page):

    content = StreamField(HomePageStreamBlock(), null=True)
