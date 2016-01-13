from django.db import models
from django.contrib.auth.models import User
class utilisateur(models.Model):
	user = models.OneToOneField(User, unique=True)
	Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	PhoneNumber = models.CharField(max_length=15)