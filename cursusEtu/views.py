#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
	return render(request, 'templates/contenu_html/accueil.html')

def aides(request):
	return render(request, 'templates/contenu_html/aides.html')