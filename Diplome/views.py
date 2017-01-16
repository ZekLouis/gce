#-*- coding: utf-8 -*-
from django.shortcuts import render
from Diplome.models import Diplome
from Annee.models import Annee
from Diplome.forms import DiplomeForm
from Diplome.forms import DiplomeFormCreation, SelectDip, RenseignerDip
from Annee.forms import AnneeForm
from UE.models import UE
from UE.forms import UEForm
from Semestre.models import Semestre
from Semestre.forms import SemestreForm
from django.shortcuts import render, get_object_or_404
# Create your views here.

# def ajouterDiplomeCreation(request, annee):
# 	#on recupere le diplome avec l'annee choisie avant
# 	Anneeobj= Annee.objects.get(annee=annee)
# 	return render(request, 'contenu_html/ajouterDiplomeCreation.html',locals())

"""Cette méthode permet d'ajouter un diplome à la base"""
def ajouterDiplome(request):
	if request.method == 'POST':  
		form = DiplomeForm(request.POST)
		if form.is_valid():
			intitule = form.cleaned_data['intitule']
			dip = Diplome(
					intitule=intitule,
	                )
			dip.save()

			res = True
		else :
			print("ERREUR : AJOUTER Diplome : VIEW ajouterDiplome : formulaire")
	else :
		form = DiplomeForm() 
	return render(request, 'contenu_html/ajouterDiplome.html', locals())

"""Cette vue permet de lister les differents diplomes"""
def listerDiplomes(request):
	dips = Diplome.objects.all()
	return render(request, 'contenu_html/listerDiplomes.html',{'dips': dips})

"""Cette vue permet de supprimer un diplome"""
def supprdip(request, id):
	dip = Diplome.objects.filter(id=id)

	dip.delete()
	return render(request, 'contenu_html/supprdip.html', locals())

"""Cette vue permet de modifier un diplome"""
def modifierDiplome(request):
	if request.method == 'POST':
		if not request.session['dip']:
			Diplomes = Diplome.objects.all()
			form = SelectDip(request.POST, diplomes=Diplomes)
			if form.is_valid() :
				id_dip = form.cleaned_data['select']
				request.session['id_dip'] = id_dip
				request.session['dip'] = True
			res = True
			d = get_object_or_404(Diplome, id=request.session['id_dip'])
			form = RenseignerDip(diplome=d)
		else:
			d = get_object_or_404(Diplome, id=request.session['id_dip'])
			form = RenseignerDip(request.POST, diplome=d)
			if form.is_valid() :
				diplome = get_object_or_404(Diplome, id=request.session['id_dip'])
				if form.cleaned_data['intitule']:
					diplome.intitule = form.cleaned_data['intitule']
				if form.cleaned_data['annee']:
					diplome.annee = form.cleaned_data['annee']
				diplome.save()	
				#request.session['mat'] = False
				res2=True
			else :
				print("ERREUR : MODIFIER Diplome : VIEW modifierDiplome : formulaire")	
	else :
		Diplomes = Diplome.objects.all()
		request.session['dip'] = False
		form = SelectDip(diplomes=Diplomes)
	return render(request, 'contenu_html/modifierDiplome.html', locals())
