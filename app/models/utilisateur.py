# coding: utf-8 
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class utilisateur(models.Model):
    user 		= models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
    Image 		= models.FileField(upload_to='User/Image/', max_length=100)
    PhoneNumber = models.CharField(max_length=15,verbose_name=_('Numéro de téléphonne'))
    NewsLetter 	= models.BooleanField(default=True)
    Rang 		= models.IntegerField(choices=list(settings.RANG ),default=0)	

    def __str__(self):
        return u'{0}'.format(self.user.last_name + ' ' + self.user.first_name)