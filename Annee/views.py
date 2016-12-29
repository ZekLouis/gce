from django.shortcuts import render
from Annee.models import Annee
from Annee.forms import AnneeForm
# Create your views here.


def ajouterAnnee(request):
	if request.method == 'POST':  
		form = AnneeForm(request.POST)
		if form.is_valid():

			annee = form.cleaned_data['annee']
			annee = Annee(
					annee=annee,
	                )
			annee.save()
			res = True
		else :
			print("ERREUR : AJOUTER Annee : VIEW ajouterAnnee : formulaire")
	else :
		form = AnneeForm() 
	return render(request, 'contenu_html/ajouterAnnee.html', locals())

def listerAnnees(request):
	annees = Annee.objects.all()
	return render(request, 'contenu_html/listerAnnees.html', locals())