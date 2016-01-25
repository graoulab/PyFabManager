from django.db import models
from .projet import *
class Machine(models.Model):
    Titre 		= models.CharField(max_length=140)
    Image 		= models.ImageField(upload_to='Machine/Image/', height_field=None, width_field=None, max_length=100)
    Descritpion = models.TextField()
    Cout 		= models.IntegerField()
    CoutAdh 	= models.IntegerField()
    Projet 		= models.ManyToManyField('Projet')
    fichier 	= models.FileField(upload_to='Machine/File/', max_length=100)
    def __str__(self):
        return u'{0}'.format(self.Titre)