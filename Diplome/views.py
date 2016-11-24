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

def listerDiplomes(request):
	dips = Diplome.objects.all()
	return render(request, 'contenu_html/listerDiplomes.html',{'dips': dips})


"""*Cette fonction permet de faire afficher les matieres et les details d'une ue
def detailDiplome(request, id):
	dip = get_object_or_404(Diplome, id=id)
	semestre = Semestre.objects.filter(unite__id=id)
	return render(request, 'contenu_html/detailDiplome.html', locals()) """ 