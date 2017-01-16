#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from Etudiant.models import Etu
from Groupe.models import Groupe
from Groupe.forms import GroupeForm, SelectGrp, RenseignerGrp
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
			print("ERREUR : AJOUT GROUPE : VIEW ajouterGroupe : formulaire")
	else :
		form = GroupeForm() 
	return render(request, 'contenu_html/ajouterGroupe.html', locals())

"""Cette vue permet de lister les groupes"""
def listerGroupes(request):
	groupes = Groupe.objects.all()
	return render(request, 'contenu_html/listerGroupes.html',{'groupe': groupes})

"""Cette vue permet de supprimer un groupe"""
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

"""Cette vue permet de modifier un groupe"""
def modifierGroupe(request):
	if request.method == 'POST':
		if not request.session['grp']:
			Groupes = Groupe.objects.all()
			form = SelectGrp(request.POST, groupes=Groupes)
			if form.is_valid() :
				id_grp = form.cleaned_data['select']
				request.session['id_grp'] = id_grp
				request.session['grp'] = True
			res = True
			g = get_object_or_404(Groupe, id=request.session['id_grp'])
			form = RenseignerGrp(groupe=g)
		else:
			g = get_object_or_404(Groupe, id=request.session['id_grp'])
			form = RenseignerGrp(request.POST, groupe=g)
			if form.is_valid() :
				groupe = get_object_or_404(Groupe, id=request.session['id_grp'])
				if form.cleaned_data['nom']:
					groupe.nom = form.cleaned_data['nom']
				if form.cleaned_data['numero']:
					groupe.prenom = form.cleaned_data['numero']
				groupe.save()	
				#request.session['mat'] = False
				res2=True
			else :
				print("ERREUR : MODIFIER Groupe : VIEW modifierGroupe : formulaire")	
	else :
		Groupes = Groupe.objects.all()
		request.session['grp'] = False
		form = SelectGrp(groupes=Groupes)
	return render(request, 'contenu_html/modifierGroupe.html', locals())