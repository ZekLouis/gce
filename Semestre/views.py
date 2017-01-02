#-*- coding: utf-8 -*-
from django.shortcuts import render
from Semestre.models import Semestre
from Semestre.forms import SemestreForm
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