"""
Definition of models.
"""

from django.db import models
class Atelier(models.Model):
    Titre = models.CharField(max_length=30)
    Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Descritpion = models.CharField(max_length=1500)
    nBplace = models.IntegerField()
    PlaceReserver= models.IntegerField()
    prix= models.IntegerField()
    date= models.DateTimeField(auto_now=False, auto_now_add=False)