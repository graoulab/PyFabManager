from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.conf import settings
from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude =('password','last_login','date_joined','groups','user_permissions')
class UtilisateurAdmin(admin.ModelAdmin):
    exclude =('Image',)
class AtelierAdmin(admin.ModelAdmin):
    list_display = ('Titre', 'date')
    exclude =('UtilisateurInscrit','PlaceReserver',)
class MachineAdmin(admin.ModelAdmin):
    exclude =('Projet',)
@receiver(post_save, sender=Atelier)
def my_callback(sender, **kwargs):
    if kwargs['created'] :
        print(kwargs['instance'].Rang)
        Temp = utilisateur.objects.filter(NewsLetter = True , Rang = kwargs['instance'].Rang)
        ListAdress = []
        for i in Temp :
            ListAdress.append(i.user.email)
        subject = kwargs['instance'].Titre
        from_email = settings.ADRESSECONTACT
        text_content =  ''
        TextFin = 'pour vous désinscrire : ' + settings.BASE_URL + str(reverse('EditNewsLetter'))
        msg = EmailMultiAlternatives(subject, text_content, from_email, ListAdress)
        msg.attach_alternative((kwargs['instance'].Descritpion  + TextFin), "text/html")
        msg.send()
    print("Request finished!")
    
admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
admin.site.register(Atelier,AtelierAdmin)
admin.site.register(Machine,MachineAdmin)
admin.site.register(Matiere)
admin.site.register(Article)
admin.site.register(utilisateur,UtilisateurAdmin)
admin.site.register(Categorie)
admin.site.register(Licences)
