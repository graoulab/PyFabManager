from django.db import models
from .utilisateur import utilisateur 
from .machine import *
from .autre import *
class Projet(models.Model):
	titre 		= models.CharField(max_length=140)
	Image 		= models.FileField(upload_to='Projet/Image/', max_length=100)
	Utilisateur = models.ManyToManyField('utilisateur')
	fichier 	= models.FileField(upload_to='Projet/File/', max_length=100)
	Materiaux 	= models.ManyToManyField('Matiere')
	Machine 	= models.ManyToManyField('Machine')
	Contenue 	= models.TextField()
	Licence 	= models.ManyToManyField('Licences')
	Date 		= models.DateTimeField(auto_now=True)
	Categorie 	= models.ManyToManyField('Categorie')
	def __str__(self):
		return u'{0}'.format(self.titre)