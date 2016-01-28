from django import template
from django.conf import settings
register = template.Library()
import datetime

@register.simple_tag
def SiteName():
    return settings.NOMLAB 

@register.simple_tag
def InfoAdresseContact ():
    return settings.ADRESSECONTACT 

@register.simple_tag
def AffichPrix():
	return settings.AFFICHERPRIX

@register.simple_tag
def InfoRue():
	return settings.RUE

@register.simple_tag
def Infoville():
    return settings.VILLE 

@register.simple_tag
def InfoCodePostal():
    return settings.CODEPOSTAL
 
@register.simple_tag
def Infodisqus():
    return settings.DISQUS
