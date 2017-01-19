#-*- coding: utf-8 -*-
from django.shortcuts import render
from Semestre.models import Semestre, InstanceSemestre
from Semestre.forms import SemestreForm, SelectSem, RenseignerSem,InstanceSemestreForm,SelectInstanceSemestre
from django.shortcuts import render, get_object_or_404
from Etudiant.models import Appartient
# Create your views here.

"""Cette vue permet d'ajouter un semestre"""
def ajouterSemestre(request):
	if request.method == 'POST':  
		form = SemestreForm(request.POST)
		if form.is_valid():

			code_ppn = form.cleaned_data['code_ppn']
			code_apogee = form.cleaned_data['code_apogee']
			dip = form.cleaned_data['diplome']
			intitule = form.cleaned_data['intitule']
			sem = Semestre(
					code_ppn=code_ppn,
					code_apogee=code_apogee,
					intitule=intitule,
					diplome = dip,					
	                )
			sem.save()
			res = True
		else :
			print("ERREUR : AJOUTER Semestre : VIEW ajouterUE : formulaire")
	else :
		form = SemestreForm() 
	return render(request, 'contenu_html/ajouterSemestre.html', locals())

"""Cette vue permet de lister les semestres"""
def listerSemestre(request):
	semestre = Semestre.objects.all()
	return render(request, 'contenu_html/listerSemestre.html',{'semestre': semestre})

"""Cette vue permet de supprimer un semestre"""
def supprsem(request, id):
	semestre = Semestre.objects.filter(id=id)

	semestre.delete()
	return render(request, 'contenu_html/supprsem.html', locals())

"""Cette vue permet de modifier un semestre"""
def modifierSemestre(request):
	if request.method == 'POST':
		if not request.session['sem']:
			Semestres = Semestre.objects.all()
			form = SelectSem(request.POST, semestres=Semestres)
			if form.is_valid() :
				id_sem = form.cleaned_data['select']
				request.session['id_sem'] = id_sem
				request.session['sem'] = True
			res = True
			s = get_object_or_404(Semestre, id=request.session['id_sem'])
			form = RenseignerSem(semestre=s)
		else:
			s = get_object_or_404(Semestre, id=request.session['id_sem'])
			form = RenseignerSem(request.POST, semestre=s)
			if form.is_valid() :
				semestre = get_object_or_404(Semestre, id=request.session['id_sem'])
				if form.cleaned_data['intitule']:
					semestre.intitule = form.cleaned_data['intitule']
				if form.cleaned_data['code']:
					semestre.code = form.cleaned_data['code']
				if form.cleaned_data['diplome']:
					semestre.diplome = form.cleaned_data['diplome']
				semestre.save()	
				#request.session['mat'] = False
				res2=True
			else :
				print("ERREUR : MODIFIER Semestre : VIEW modifierSemestre : formulaire")	
	else :
		Semestres = Semestre.objects.all()
		request.session['sem'] = False
		form = SelectSem(semestres=Semestres)
	return render(request, 'contenu_html/modifierSemestre.html', locals())


def ajouter_instance_semestre(request):
	if request.method == 'POST':  
		form = InstanceSemestreForm(request.POST)
		if form.is_valid():

			annee = form.cleaned_data['annee']
			semestre = form.cleaned_data['semestre']
			
			# L'instance du semestre
			IS = InstanceSemestre(
					annee=annee,
					semestre = semestre,					
			)

			IS.save()
			res = True
		else :
			print("ERREUR : AJOUTER IS : VIEW ajouter_instance_semestre : formulaire")
	else :
		form = InstanceSemestreForm()
	return render(request, 'contenu_html/ajouterInstanceSemestre.html', locals())


"""Cette vue permet de faire afficher les étudiants d'une Instance de semestre"""
def afficherInstanceSemestre(request):
	if request.method == 'POST':
		instanceSemestres = InstanceSemestre.objects.all()
		form = SelectInstanceSemestre(request.POST, instanceSemestres=instanceSemestres)
		if form.is_valid() :
			id_inst = form.cleaned_data['select']
			instanceSemestre = get_object_or_404(InstanceSemestre, id=id_inst)
			listeEtu = Appartient.objects.filter(instance_semestre=instanceSemestre)
			res = True
		else:
			print("ERREUR : Afficher promotion: VIEW afficher Promotion : formulaire")	
	else:
		instanceSemestres = InstanceSemestre.objects.all()
		form = SelectInstanceSemestre(instanceSemestres=instanceSemestres)
	return render(request, 'contenu_html/afficherInstanceSemestre.html', locals())