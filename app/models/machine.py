from django.db import models
class Machine(models.Model):
    Titre 		= models.CharField(max_length=30)
    Image 		= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Descritpion = models.CharField(max_length=1500)
    Cout 		= models.IntegerField()