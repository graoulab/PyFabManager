from django.utils.translation import ugettext_lazy as _
from django.db import models
from .projet import *
class Machine(models.Model):
    Titre 		= models.CharField(max_length=140)
    Image 		= models.FileField(upload_to='Machine/Image/', max_length=100)
    Descritpion = models.TextField()
    Cout 		= models.IntegerField(verbose_name=_('Prix'))
    CoutAdh 	= models.IntegerField(verbose_name=_('Prix adherant'))
    Projet 		= models.ManyToManyField('Projet')
    fichier 	= models.FileField(upload_to='Machine/File/', max_length=100,default=None,blank=True)
    def __str__(self):
        return u'{0}'.format(self.Titre)