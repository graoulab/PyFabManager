from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from .utilisateur import *

class Atelier(models.Model):
    Titre 				= models.CharField(max_length=140)
    Image 				= models.FileField(upload_to='Atelier/Image/',  max_length=100)
    Descritpion 		= models.TextField()
    nBplace 			= models.IntegerField(verbose_name=_('Place disponible'))
    PlaceReserver		= models.IntegerField(default=0)
    prix				= models.IntegerField(verbose_name=_('Prix'))
    prixAdh				= models.IntegerField(default=0,verbose_name=_('Prix adherant'))
    date 				= models.DateTimeField(auto_now=False, auto_now_add=False)
    Durer               = models.TimeField()
    UtilisateurInscrit 	= models.ManyToManyField('utilisateur')
    Rang				= models.IntegerField(choices=list(settings.RANG ),default=0,verbose_name=_("Qui peut s'inscrire"))
    def __str__(self):
        return u'{0}'.format(self.Titre)