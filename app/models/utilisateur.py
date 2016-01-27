from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.conf import settings
class utilisateur(models.Model):
	user 		= models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
	Image 		= models.ImageField(upload_to='User/Image/', height_field=None, width_field=None, max_length=100)
	PhoneNumber = models.CharField(max_length=15)
	NewsLetter 	= models.BooleanField(default=True)
	Rang 		= models.IntegerField(choices=list(settings.RANG ),default=0)	

	def __str__(self):
		return u'{0}'.format(self.user.username)