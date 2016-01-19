from django.db import models
from .projet import *
class Machine(models.Model):
    Titre 		= models.CharField(max_length=30)
    Image 		= models.ImageField(upload_to='Machine/Image/', height_field=None, width_field=None, max_length=100)
    Descritpion = models.TextField()
    Cout 		= models.IntegerField()
    CoutAdh 	= models.IntegerField()
    Projet 		= models.ManyToManyField('Projet')