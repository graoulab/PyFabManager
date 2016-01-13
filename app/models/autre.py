from django.db import models
class Matiere(models.Model):
    Nom = models.CharField(max_length=30)
class Categorie(models.Model):
    Nom = models.CharField(max_length=30)
class Licences(models.Model):
    Nom = models.CharField(max_length=30)
    Description = models.CharField(max_length=30)