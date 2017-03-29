"""cursusEtu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from Etudiant import views


urlpatterns = [
    url(r'^listeretus$', views.listeretus, name='listeretus'),
    url(r'^suppall$', views.suppall, name='suppall'),
    url(r'^importer_etu$', views.importer_etu, name='importer_etu'),
    url(r'^listeretu/(?P<id>\d+)$', views.listeretu),
    url(r'^listerPromotion$', views.listerPromotion, name ='listerPromotion'),
    url(r'^ajouterEtudiant', views.ajouterEtudiant, name='ajouterEtudiant'),
    #url(r'^completer_etu', views.complement_etu, name='completer_etu'),
    url(r'^complement_etu', views.complement_etu, name='complement_etu'),
    url(r'^affichageComplet', views.affichageComplet, name='affichageComplet'),
    url(r'^suppretu/(?P<id>\d+)$', views.suppretu, name='suppretu'),
    # url(r'^faireEvoluerPromotion', views.faireEvoluerPromotion, name='faireEvoluerPromotion'),
]
