"""
Definition of urls for FabManager.
"""

from datetime import datetime
from django.conf import settings
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from django.conf.urls.static import static
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
from app import views
from django.contrib.auth import views as auth_views
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=[ 
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^Projet/AddProjet/$', views.CreationProjet, name='NewProjet'),
    url(r'^Atelier/(?P<NbPage>\d+)$', views.ViewAtelier, name=''),
    url(r'^Atelier/Edit/(?P<NbPage>\d+)$', views.EditAtelier, name=''),
    url(r'^Atelier/Desinscription/(?P<Action>\d+)/$', views.DesinscriptionAtelier, name=''),
    url(r'^Atelier/Inscription/(?P<Action>\d+)/$', views.InscriptionAtelier, name=''),
    url(r'^Machine/(?P<NbPage>\d+)$', views.ViewMachine, name=''),
    url(r'^Machine/Edit/(?P<NbPage>\d+)$', views.EditMachine, name=''),
    url(r'^ListMachine/$', views.ListMachine, name='ListMachine'),
    url(r'^ListMachine/(?P<NbPage>\d+)$', views.ListMachine, name=''),    
    url(r'^ListAtelier/$', views.ListAtelier, name='ListAtelier'),
    url(r'^ListAtelier/(?P<NbPage>\d+)$', views.ListAtelier, name=''),
    url(r'^ListProjet/$', views.ListProjet, name='ListProjet'),
    url(r'^ListProjet/(?P<NbPage>\d+)$', views.ListProjet, name=''),
    url(r'^Admin/$', views.AdminIndex, name='admin'),
    url(r'^Admin/Config/$', views.ConfigWebView, name='Config'),
    url(r'^Admin/ListMateriaux/$', views.ListMateriaux, name='ListMateriaux'),
    url(r'^Admin/ListLicence/$', views.ListLicence, name='ListLicence'),
    url(r'^Admin/ListCategorie/$', views.ListCategorie, name='ListCategorie'),
    url(r'^Admin/ListUser/$', views.ListUser, name='ListUser'),
    url(r'^Admin/ListUser/(?P<NbPage>\d+)$', views.ListUser, name=''),
    url(r'^Admin/User/(?P<Action>\w+)/(?P<NbPage>\d+)$', views.GestionUser, name=''),
    url(r'^Admin/Machine/Delete/(?P<NbPage>\d+)$', views.DeleteMachine, name=''),
    url(r'^Admin/Atelier/Delete/(?P<NbPage>\d+)$', views.DeleteAtelier, name=''),
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
]
