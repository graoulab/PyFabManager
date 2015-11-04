from django.db import models
from .utilisateur import utilisateur
from .machine import Machine
from .autre import *
class Projet(models.Model):
	titre = models.CharField(max_length=30)
	Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	Utilisateur = models.OneToOneField('utilisateur')
	fichier = models.FileField(upload_to=None, max_length=100)
	Materiaux = models.ManyToManyField('Matiere')
	Machine = models.ManyToManyField('Machine')
	Contenue = models.CharField(max_length=1500)
	Licence = models.OneToOneField('Licences')
	Date = models.DateTimeField(auto_now=False, auto_now_add=False)
	Categorie = models.OneToOneField('Categorie')