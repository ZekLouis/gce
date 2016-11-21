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
    url(r'^Enseignant/',include('Enseignant.urls')),
    url(r'^Groupe/',include('Groupe.urls')),
    url(r'^aides', views.aides, name='aides'),
]
