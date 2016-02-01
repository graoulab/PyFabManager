from django.db import models 
class Matiere(models.Model):
    Nom = models.CharField(max_length=30)
    def __str__(self):
        return u'{0}'.format(self.Nom)
class Categorie(models.Model):
    Nom = models.CharField(max_length=30)
    def __str__(self):
        return u'{0}'.format(self.Nom)
class Licences(models.Model):
    Nom = models.CharField(max_length=30)
    Description = models.CharField(max_length=30)
    def __str__(self):
        return u'{0}'.format(self.Nom)