from django.shortcuts import render
from Diplome.models import Diplome
from Diplome.forms import DiplomeForm
# Create your views here.


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