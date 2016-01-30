from django.db import models
from .utilisateur import *
from django.conf import settings
class Article(models.Model):
    Titre 				= models.CharField(max_length=140)
    Image 				= models.FileField(upload_to='Article/Image/', max_length=100)
    date 				= models.DateTimeField(auto_now_add=True)
    Descritpion         = models.TextField()
    Rang				= models.IntegerField(choices=list(settings.RANG ),default=0)
    def __str__(self):
        return u'{0}'.format(self.Titre)