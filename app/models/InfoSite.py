from django.db import models
class Config(models.Model):
    NomLab			= models.CharField(max_length=30)
    AdresseContact 	= models.CharField(max_length=30)
    Rue 			= models.CharField(max_length=150)
    ville 			= models.CharField(max_length=30)
    CodePostal		= models.CharField(max_length=30)