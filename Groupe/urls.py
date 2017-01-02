from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from Groupe import views

urlpatterns = [
    url(r'^ajouterGroupe', views.ajouterGroupe, name='ajouterGroupe'),
    url(r'^listerGroupes', views.listerGroupes, name='listerGroupes'),
    url(r'^listerEtuGroupe/(?P<id>\d+)$', views.listerEtuGroupe, name='listerEtuGroupe'),
    url(r'^supprgrp/(?P<id>\d+)$', views.supprgrp, name='supprgrp'),
    url(r'^modifierGroupe', views.modifierGroupe, name='modifierGroupe'),

]
