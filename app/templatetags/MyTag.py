from django import template
from ..models import *
register = template.Library()
@register.simple_tag
def SiteName():
    return Config.objects.all().last().NomLab