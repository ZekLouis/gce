#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from Matiere.models import Matiere
from Enseignant.forms import EnseignantForm, SelectMatiere
from Enseignant.forms import Enseignant, SelectEns, RenseignerEns

from django import forms

# Create your views here.

"""Cette vue permet d'ajouter un Enseignant"""
def ajouterEnseignant(request):

	if request.method == 'POST':

		if not request.session['mat']:
			mats = Matiere.objects.all()
			form = SelectMatiere(request.POST, matieres=mats)
			if form.is_valid() :
				id_mat = form.cleaned_data['select']
				request.session['id_mat'] = id_mat
				request.session['mat'] = True
				res = True
			e = get_object_or_404(Matiere, id=request.session['id_mat'])
			form=EnseignantForm()
		else:
			form = EnseignantForm(request.POST)
			if form.is_valid() :
				nom = form.cleaned_data['nom']
				prenom = form.cleaned_data['prenom']
				e = get_object_or_404(Matiere, id=request.session['id_mat'])

				ens = Enseignant(
						nom=nom,
						prenom=prenom,
						matiere=e,
		                )
				ens.save()
				request.session['mat'] = False
				res2=True
			else :
				print("ERREUR")	
	else :
		mats = Matiere.objects.all()
		request.session['mat'] = False
		form = SelectMatiere(matieres=mats)
	return render(request, 'contenu_html/ajouterEnseignant.html', locals())

"""Cette vue permet de lister les Enseignants"""
def listerEnseignants(request):
	ens = Enseignant.objects.all()
	return render(request, 'contenu_html/listerEnseignants.html',{'ens': ens})

def supprens(request, id):
	ens = Enseignant.objects.filter(id=id)
	ens.delete()
	return render(request, 'contenu_html/supprens.html', locals())

def modifierEnseignant(request):
	if request.method == 'POST':
		if not request.session['ens']:
			Enseignants = Enseignant.objects.all()
			form = SelectEns(request.POST, enseignants=Enseignants)
			if form.is_valid() :
				id_ens = form.cleaned_data['select']
				request.session['id_ens'] = id_ens
				request.session['ens'] = True
			res = True
			e = get_object_or_404(Enseignant, id=request.session['id_ens'])
			form = RenseignerEns(enseignant=e)
		else:
			e = get_object_or_404(Enseignant, id=request.session['id_ens'])
			form = RenseignerEns(request.POST, enseignant=e)
			if form.is_valid() :
				enseignant = get_object_or_404(Enseignant, id=request.session['id_ens'])
				if form.cleaned_data['nom']:
					enseignant.nom = form.cleaned_data['nom']
				if form.cleaned_data['prenom']:
					enseignant.prenom = form.cleaned_data['prenom']
				if form.cleaned_data['matiere']:
					enseignant.matiere = form.cleaned_data['matiere']
				enseignant.save()	
				#request.session['mat'] = False
				res2=True
			else :
				print("Form Non Valide")	
	else :
		Enseignants = Enseignant.objects.all()
		request.session['ens'] = False
		form = SelectEns(enseignants=Enseignants)
	return render(request, 'contenu_html/modifierEnseignant.html', locals())