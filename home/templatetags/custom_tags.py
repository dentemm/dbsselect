from django import template

from ..models import SessionsPage, ContactPage, MediaPage, AboutPage, RelivePage

register = template.Library()

@register.simple_tag
def sessions_page(locale):
  return SessionsPage.objects.all().filter(locale=locale).first().get_url()

@register.simple_tag
def contact_page(locale):
  return ContactPage.objects.all().filter(locale=locale).first().get_url()

@register.simple_tag
def about_page(locale):
  return AboutPage.objects.all().filter(locale=locale).first().get_url()

@register.simple_tag
def media_page(locale):
  return MediaPage.objects.all().filter(locale=locale).first().get_url()

@register.simple_tag
def relive_page(locale):
  return RelivePage.objects.all().filter(locale=locale).first().get_url()