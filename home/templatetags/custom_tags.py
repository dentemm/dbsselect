from django import template

from ..models import SessionsPage, ContactPage, MediaPage, AboutPage, RelivePage

register = template.Library()

@register.simple_tag
def sessions_page(locale):
  return SessionsPage.objects.all().first().get_url()

  # return SessionsPage.objects.all().filter(locale=locale).first().get_url()

@register.simple_tag
def contact_page(locale):
  return ContactPage.objects.all().first().get_url()

  # return ContactPage.objects.all().filter(locale=locale).first().get_url()

@register.simple_tag
def about_page(locale):
  return AboutPage.objects.all().first().get_url()
  # return AboutPage.objects.all().filter(locale=locale).first().get_url()

@register.simple_tag
def media_page(locale):
  return MediaPage.objects.all().first().get_url()

@register.simple_tag
def relive_page(locale):
  return RelivePage.objects.all().first().get_url()

@register.simple_tag
def check_current_page(slug, reference):
  return reference in slug