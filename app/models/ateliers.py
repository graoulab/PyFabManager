from django.db import models
from .utilisateur import *
from django.conf import settings
class Atelier(models.Model):
    Titre 				= models.CharField(max_length=140)
    Image 				= models.ImageField(upload_to='Atelier/Image/', height_field=None, width_field=None, max_length=100)
    Descritpion 		= models.TextField()
    nBplace 			= models.IntegerField()
    PlaceReserver		= models.IntegerField(default=0)
    prix				= models.IntegerField()
    prixAdh				= models.IntegerField(default=0)
    date 				= models.DateTimeField(auto_now=False, auto_now_add=False)
    UtilisateurInscrit 	= models.ManyToManyField('utilisateur')
    Rang				= models.IntegerField(choices=list(settings.RANG ),default=0)
    def __str__(self):
        return u'{0}'.format(self.Titre)