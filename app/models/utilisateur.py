from django.db import models
from .autre import TypeAdherent
class utilisateur(models.Model):
	Nom = models.CharField(max_length=30)
	Prenom = models.CharField(max_length=30)
	Email = models.EmailField(max_length=254)
	DateDeCreation = models.DateTimeField(auto_now=False, auto_now_add=False)
	UserType = models.ForeignKey('TypeAdherent')
	rang = models.IntegerField()