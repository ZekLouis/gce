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
#-*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from Semestre import views


urlpatterns = [
    
    url(r'^ajouterSemestre', views.ajouterSemestre, name='ajouterSemestre'),
    url(r'^listerSemestre', views.listerSemestre, name='listerSemestre'),
    url(r'^supprsem/(?P<id>\d+)$', views.supprsem, name='supprsem'),
    url(r'^modifierSemestre', views.modifierSemestre, name='modifierSemestre'),
    url(r'^ajouterInstanceSemestre', views.ajouter_instance_semestre, name='ajouter_instance_semestre'),
    url(r'^afficherInstanceSemestre', views.afficherInstanceSemestre, name='afficherInstanceSemestre'),
    url(r'^faireEvoluerInstanceSemestre', views.faireEvoluerInstanceSemestre, name='faireEvoluerInstanceSemestre'),
]
