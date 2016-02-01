from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
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