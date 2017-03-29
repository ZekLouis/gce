from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from cursusEtu import views


urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    url(r'^admin/', admin.site.urls),
    url(r'^Etudiant/',include('Etudiant.urls')),
    url(r'^Note/',include('Note.urls')),
    url(r'^UE/',include('UE.urls')),
    url(r'^Matiere/',include('Matiere.urls')),
    url(r'^Semestre/',include('Semestre.urls')),
    url(r'^Diplome/',include('Diplome.urls')),
     url(r'^Annee/',include('Annee.urls')),
    url(r'^Documents/',include('Documents.urls')),
    url(r'^aides', views.aides, name='aides'),
    url(r'^onAdmin', views.onAdmin, name='onAdmin'),
]
