#-*- coding: utf-8 -*-
from django.shortcuts import render
from Semestre.models import Semestre
from Semestre.forms import SemestreForm, SelectSem, RenseignerSem
from django.shortcuts import render, get_object_or_404
# Create your views here.


def ajouterSemestre(request):
	if request.method == 'POST':  
		form = SemestreForm(request.POST)
		if form.is_valid():

			code = form.cleaned_data['code']
			dip = form.cleaned_data['diplome']
			intitule = form.cleaned_data['intitule']
			sem = Semestre(
					code=code,
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

def listerSemestre(request):
	semestre = Semestre.objects.all()
	return render(request, 'contenu_html/listerSemestre.html',{'semestre': semestre})

def supprsem(request, id):
	semestre = Semestre.objects.filter(id=id)

	semestre.delete()
	return render(request, 'contenu_html/supprsem.html', locals())

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
				print("Form Non Valide")	
	else :
		Semestres = Semestre.objects.all()
		request.session['sem'] = False
		form = SelectSem(semestres=Semestres)
	return render(request, 'contenu_html/modifierSemestre.html', locals())