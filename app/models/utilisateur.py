from django.db import models
from django.contrib.auth.models import User
from .autre import TypeAdherent
class utilisateur(models.Model):
	user = models.OneToOneField(User, unique=True)
	UserType = models.ForeignKey('TypeAdherent')