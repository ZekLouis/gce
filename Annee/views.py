#-*- coding: utf-8 -*-
from django.shortcuts import render
from Annee.models import Annee
from Annee.forms import AnneeForm
# Create your views here.

"""Cette vue permet d'ajouter une année à la base"""
def ajouterAnnee(request):
	if request.method == 'POST':  
		form = AnneeForm(request.POST)
		if form.is_valid():

			annee = form.cleaned_data['intitule']
			annee_obj = Annee(
					intitule=annee,
	                )
			annee_obj.save()
			res = True
		else :
			print("ERREUR : AJOUTER Annee : VIEW ajouterAnnee : formulaire")
	else :
		form = AnneeForm() 
	return render(request, 'contenu_html/ajouterAnnee.html', locals())

"""Cette vue permet de lister toutes les années présentes dans la base"""
def listerAnnees(request):
	annees = Annee.objects.all()
	return render(request, 'contenu_html/listerAnnees.html', locals())

def supprann(request, id):
	annee = Annee.objects.filter(id=id)

	annee.delete()
	return render(request, 'contenu_html/supprann.html', locals())