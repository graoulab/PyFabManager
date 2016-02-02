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
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
from app import views
from django.contrib.auth import views as auth_views
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += i18n_patterns(
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^Profil$', views.ViewProfil, name='Profil'),
    url(r'^Profil/EditNewsLetter$', views.EditNewsLetter, name='EditNewsLetter'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^Article/(?P<NbPage>\d+)$', views.ViewArticle, name='ViewArticle'),
    url(r'^Projet/AddProjet/$', views.CreationProjet, name='NewProjet'),
    url(r'^Projet/EditProjet/(?P<NbPage>\d+)$', views.EditProjet, name='EditProjet'),
    url(r'^Projet/DeleteProjet/(?P<NbPage>\d+)$', views.DeleteProjet, name='DeleteProjet'),
    url(r'^Projet/(?P<NbPage>\d+)$', views.ViewProjet, name='ViewProjet'),
    url(r'^Atelier/(?P<NbPage>\d+)$', views.ViewAtelier, name='ViewAtelier'),
    url(r'^Atelier/Desinscription/(?P<Action>\d+)/$', views.DesinscriptionAtelier, name='DesinscriptionAtelier'),
    url(r'^Atelier/Inscription/(?P<Action>\d+)/$', views.InscriptionAtelier, name='InscriptionAtelier'),
    url(r'^Machine/(?P<NbPage>\d+)$', views.ViewMachine, name='ViewMachine'),
    url(r'^ListMachine/$', views.ListMachine, name='ListMachine'),
    url(r'^ListMachine/(?P<NbPage>\d+)$', views.ListMachine, name=''),    
    url(r'^ListAtelier/$', views.ListAtelier, name='ListAtelier'),
    url(r'^ListAtelier/(?P<NbPage>\d+)$', views.ListAtelier, name='PListAtelier'),
    url(r'^ListArticle/$', views.ListArticle, name='ListArticle'),
    url(r'^ListArticle/(?P<NbPage>\d+)$', views.ListArticle, name='PListArticle'),
    url(r'^ListProjet/$', views.ListProjet, name='ListProjet'),
    url(r'^Admin/', admin.site.urls , name='AdminPage'),
    url(r'^Admin/SendMail/', views.EnvoieMail , name='SendMailPage'),
    url(r'^ListProjet/(?P<NbPage>\d+)$', views.ListProjet, name=''),
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
)
