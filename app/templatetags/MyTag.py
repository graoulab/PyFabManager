from django import template
from ..models import *
register = template.Library()
@register.simple_tag
def SiteName():
    return Config.objects.all().last().NomLab
import datetime
@register.simple_tag
def date_now():
    return datetime.datetime.now()