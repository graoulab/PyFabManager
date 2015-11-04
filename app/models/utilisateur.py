from django.db import models
from django.contrib.auth.models import User
from .autre import TypeAdherent
class utilisateur(models.Model):
	user = models.OneToOneField(User, unique=True)
	UserType = models.ForeignKey('TypeAdherent')
	Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)