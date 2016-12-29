from django.shortcuts import render
from Diplome.models import Diplome
from Annee.models import Annee
from Diplome.forms import DiplomeForm
from Diplome.forms import DiplomeFormCreation
from Annee.forms import AnneeForm
from UE.models import UniteE
from UE.forms import UEForm
from Semestre.models import Semestre
from Semestre.forms import SemestreForm
from django.shortcuts import render, get_object_or_404
# Create your views here.

# def ajouterDiplomeCreation(request, annee):
# 	#on recupere le diplome avec l'annee choisie avant
# 	Anneeobj= Annee.objects.get(annee=annee)
# 	return render(request, 'contenu_html/ajouterDiplomeCreation.html',locals())

def ajouterDiplome(request):
	if request.method == 'POST':  
		form = DiplomeForm(request.POST)
		if form.is_valid():
			nom = form.cleaned_data['nom']
			annee = form.cleaned_data['annee']
			dip = Diplome(
					nom=nom,
					annee=annee,
	                )
			dip.save()

			res = True
		else :
			print("ERREUR : AJOUTER Diplome : VIEW ajouterDiplome : formulaire")
	else :
		form = DiplomeForm() 
	return render(request, 'contenu_html/ajouterDiplome.html', locals())

def listerDiplomes(request):
	dips = Diplome.objects.all()
	return render(request, 'contenu_html/listerDiplomes.html',{'dips': dips})

