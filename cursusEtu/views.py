#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

"""Cette vue permet de faire afficher l'accueil"""
def accueil(request):
	return render(request, 'templates/contenu_html/accueil.html')

"""Cette vue permet de faire afficher la page d'aides"""
def aides(request):
	return render(request, 'templates/contenu_html/aides.html')

def onAdmin(request):
	request.session['admin'] = True
