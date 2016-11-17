#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from Etudiant.models import Etu,Groupe
from Etudiant.forms import EtudiantForm, RenseignerEtu, SelectEtu, GroupeForm

# Create your views here.

def listeretu(request, id):
	etu = get_object_or_404(Etu, id=id)
	notes = Note.objects.filter(etu__id=id)
	return render(request, 'contenu_html/listeretu.html', locals())


def ajouterEtudiant(request):
	if request.method == 'POST':  
		form = EtudiantForm(request.POST)
		if form.is_valid() :

			nom = form.cleaned_data['nom']
			prenom = form.cleaned_data['prenom']
			age = form.cleaned_data['age']

			e = Etu(
					nom=nom,
					prenom=prenom,
					age=age,
	                )
			e.save()
			res = True
		else :
			print("Erreur à l'ajout")
	else :
		form = EtudiantForm() 
	return render(request, 'contenu_html/ajouterEtudiant.html', locals())


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
			print("Erreur ajouter un groupe")
	else :
		form = GroupeForm() 
	return render(request, 'contenu_html/ajouterGroupe.html', locals())

def listeretus(request):
	etus = Etu.objects.all()
	return render(request, 'contenu_html/listeretus.html',{'etus': etus})


def completer_etu(request):
	if request.method == 'POST':
		form = SelectEtu(request.POST)
		if form.is_valid() :
			id_etu = form.cleaned_data['select']
			e = get_object_or_404(Etu, id=id_etu)
			request.session['id_etu'] = id_etu
			form = RenseignerEtu()
		else :
			print("ERREUR")
		res = True
	else :
		form = SelectEtu()
	return render(request, 'contenu_html/completer_etu.html', locals())

def complement_etu(request):
	if request.method == 'POST':
		if form.is_valid() :
			etudiant = get_object_or_404(Etu, id=request.session['id_etu'])
			etudiant.age = form.cleaned_data['age']
			etudiant.apogee = form.cleaned_data['apogee']
			etudiant.date_naissance = form.cleaned_data['date_naissance']
			etudiant.sexe = form.cleaned_data['sexe']
			etudiant.adresse = form.cleaned_data['adresse']
			etudiant.ine = form.cleaned_data['ine']
			etudiant.adresse_parents = form.cleaned_data['adresse_parents']
			etudiant.tel = form.cleaned_data['tel']
			etudiant.tel_par = form.cleaned_data['tel_par']
			etudiant.lieu_naissance = form.cleaned_data['lieu_naissance']
			etudiant.nationalite = form.cleaned_data['nationalite']
			etudiant.situation_familiale = form.cleaned_data['situation_familiale']
			etudiant.situation_militaire = form.cleaned_data['situation_militaire']
			etudiant.cate_socio_pro_chef_famille = form.cleaned_data['cate_socio_pro_chef_famille']
			etudiant.cate_socio_pro_autre_parent = form.cleaned_data['cate_socio_pro_autre_parent']
			etudiant.aide_financiere = form.cleaned_data['aide_financiere']
			etudiant.bourse = form.cleaned_data['bourse']
			etudiant.save()	
		else :
			print("Form Non Valide")
	else : 
		erreur = "ERR"
	return render(request, 'contenu_html/complement_etu.html', locals())


