from django.contrib import admin
from .models import *

# Register your models here.
class AtelierAdmin(admin.ModelAdmin):
    list_display = ('Titre', 'date')
    exclude =('UtilisateurInscrit','PlaceReserver',)
class MachineAdmin(admin.ModelAdmin):
    exclude =('Projet',)
admin.site.register(Atelier,AtelierAdmin)
admin.site.register(Machine,MachineAdmin)
admin.site.register(Matiere)
admin.site.register(utilisateur)
admin.site.register(Categorie)
admin.site.register(Licences)