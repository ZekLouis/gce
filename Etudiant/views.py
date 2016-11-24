#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from Etudiant.models import Etu
from Etudiant.forms import EtudiantForm, RenseignerEtu, SelectEtu
from Groupe.forms import GroupeForm
from Groupe.models import Groupe
from Note.models import Note
from UE.models import UniteE
from Matiere.models import Matiere

# Create your views here.

def listeretu(request, id):
	etu = get_object_or_404(Etu, id=id)
	notes = Note.objects.filter(etudiant__id=id)
	return render(request, 'contenu_html/listeretu.html', locals())


def ajouterEtudiant(request):
	if request.method == 'POST':  
		form = EtudiantForm(request.POST)
		if form.is_valid() :

			nom = form.cleaned_data['nom']
			prenom = form.cleaned_data['prenom']
			apogee = form.cleaned_data['apogee']

			e = Etu(
					nom=nom,
					prenom=prenom,
					apogee=apogee,
	                )
			e.save()
			res = True
		else :
			print("Erreur à l'ajout")
	else :
		form = EtudiantForm() 
	return render(request, 'contenu_html/ajouterEtudiant.html', locals())

def affichageComplet(request):
	if request.method == 'POST':
		Etudiants = Etu.objects.all()
		form = SelectEtu(request.POST, etus=Etudiants)
		if form.is_valid() :
			id_etu = form.cleaned_data['select']
			e = get_object_or_404(Etu, id=id_etu)
			semestre = e.semestre
			ues = UniteE.objects.all().filter(semestre=semestre)
			matieres = []
			for ue in ues :
				matieres.append(Matiere.objects.all().filter(unite=ue))
			#diplome = Diplome.objects.all().filter()
			notes = Note.objects.all().filter(etudiant__id=id_etu)
			res = True
		else:
			print("Erreur Form")
	else :
		Etudiants = Etu.objects.all()
		form = SelectEtu(etus=Etudiants)
	return render(request, 'contenu_html/affichageComplet.html', locals())


def listeretus(request):
	etus = Etu.objects.all()
	return render(request, 'contenu_html/listeretus.html',{'etus': etus})


def completer_etu(request):
	if request.method == 'POST':
		Etudiants = Etu.objects.all()
		form = SelectEtu(request.POST, etus=Etudiants)
		if form.is_valid() :
			id_etu = form.cleaned_data['select']
			e = get_object_or_404(Etu, id=id_etu)
			request.session['id_etu'] = id_etu
			form = RenseignerEtu()
		else :
			print("ERREUR")
		res = True
	else :
		Etudiants = Etu.objects.all()
		form = SelectEtu(etus=Etudiants)
	return render(request, 'contenu_html/completer_etu.html', locals())

def complement_etu(request):
	if request.method == 'POST':
		form = RenseignerEtu(request.POST)
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
			etudiant.groupe = form.cleaned_data['groupe']
			etudiant.semestre = form.cleaned_data['semestre']
			etudiant.save()	
		else :
			print("Form Non Valide")
	else : 
		erreur = "ERR"
	return render(request, 'contenu_html/complement_etu.html', locals())


