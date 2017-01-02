#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from Etudiant.models import Etu
from Groupe.models import Groupe
from Groupe.forms import GroupeForm
from django import forms
import os
from io import StringIO

"""Cette vue permet d'ajouter un groupe à la base"""
def ajouterGroupe(request):
	if request.method == 'POST':  
		form = GroupeForm(request.POST)
		if form.is_valid() :

			nom = form.cleaned_data['nom']
			numero = form.cleaned_data['numero']

			g = Groupe(
					nom=nom,
					numero=numero,
	                )
			g.save()
			res = True
		else :
			print("ERREUR : AJOUT GROUPE : VIEW ajouterGroupe")
	else :
		form = GroupeForm() 
	return render(request, 'contenu_html/ajouterGroupe.html', locals())

"""Cette vue permet de lister les groupes"""
def listerGroupes(request):
	groupes = Groupe.objects.all()
	return render(request, 'contenu_html/listerGroupes.html',{'groupe': groupes})


def supprgrp(request, id):
	groupe = get_object_or_404(Groupe, id=id)
	etus = Etu.objects.filter(groupe=id)
	groupe.delete()

	if etus :
		etus.delete()
	return render(request, 'contenu_html/supprgrp.html', locals())

"""Cette vue permet de lister les étudiants et les groupes"""
def listerEtuGroupe(request, id):
	etus = Etu.objects.filter(groupe=id)
	groupe = get_object_or_404(Groupe, id=id)
	return render(request, 'contenu_html/listerEtuGroupe.html', locals())