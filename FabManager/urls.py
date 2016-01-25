"""
Definition of urls for FabManager.
"""

from datetime import datetime
from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.i18n import i18n_patterns
from app.forms import BootstrapAuthenticationForm
from django.conf.urls.static import static
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
from app import views
from django.contrib.auth import views as auth_views
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += i18n_patterns(
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about', views.about, name='about'),
    url(r'^Profil', views.ViewProfil, name='Profil'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^Projet/AddProjet/$', views.CreationProjet, name='NewProjet'),
    url(r'^Projet/EditProjet/(?P<NbPage>\d+)$', views.EditProjet, name='EditProjet'),
    url(r'^Projet/DeleteProjet/(?P<NbPage>\d+)$', views.DeleteProjet, name='DeleteProjet'),
    url(r'^Projet/(?P<NbPage>\d+)$', views.ViewProjet, name='ViewProjet'),
    url(r'^Atelier/(?P<NbPage>\d+)$', views.ViewAtelier, name='ViewAtelier'),
    url(r'^Atelier/Edit/(?P<NbPage>\d+)$', views.EditAtelier, name='EditAtelier'),
    url(r'^Atelier/Desinscription/(?P<Action>\d+)/$', views.DesinscriptionAtelier, name='DesinscriptionAtelier'),
    url(r'^Atelier/Inscription/(?P<Action>\d+)/$', views.InscriptionAtelier, name='InscriptionAtelier'),
    url(r'^Machine/(?P<NbPage>\d+)$', views.ViewMachine, name='ViewMachine'),
    url(r'^ListMachine/$', views.ListMachine, name='ListMachine'),
    url(r'^ListMachine/(?P<NbPage>\d+)$', views.ListMachine, name=''),    
    url(r'^ListAtelier/$', views.ListAtelier, name='ListAtelier'),
    url(r'^ListAtelier/(?P<NbPage>\d+)$', views.ListAtelier, name='PListAtelier'),
    url(r'^ListProjet/$', views.ListProjet, name='ListProjet'),
    url(r'^ListProjet/(?P<NbPage>\d+)$', views.ListProjet, name=''),
    url(r'^Admin/$', views.AdminIndex, name='admin'),
    url(r'^Admin/Config/$', views.ConfigWebView, name='Config'),
    url(r'^Admin/ListMateriaux/$', views.ListMateriaux, name='ListMateriaux'),
    url(r'^Admin/ListLicence/$', views.ListLicence, name='ListLicence'),
    url(r'^Admin/ListCategorie/$', views.ListCategorie, name='ListCategorie'),
    url(r'^Admin/ListUser/$', views.ListUser, name='ListUser'),
    url(r'^Admin/ListUser/(?P<NbPage>\d+)$', views.ListUser, name=''),
    url(r'^Admin/User/(?P<Action>\w+)/(?P<NbPage>\d+)$', views.GestionUser, name='GestionUser'),
    url(r'^Admin/Machine/Delete/(?P<NbPage>\d+)$', views.DeleteMachine, name='DeleteMachine'),
    url(r'^Admin/Machine/Edit/(?P<NbPage>\d+)$', views.EditMachine, name='EditMachine'),
    url(r'^Admin/Atelier/Delete/(?P<NbPage>\d+)$', views.DeleteAtelier, name='DeleteAtelier'),
    url(r'^Admin/AddMachine/$', views.CreationMachine, name='AddMachine'),
    url(r'^Admin/Atelier/$', views.CreationAtelier, name='AddAtelier'),
    url(r'^Admin/Categorie/(?P<Action>\w+)/$', views.ModifCategorie, name='ModifCategorie'),
    url(r'^Admin/Licences/(?P<Action>\w+)/$', views.ModifLicence, name='ModifLicences'),
    url(r'^Admin/Matiere/(?P<Action>\w+)/$', views.ModifMateriaux, name='ModifMateriaux'),
    url(r'^login/$', auth_views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
