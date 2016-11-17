from django.shortcuts import render, get_object_or_404
from Matiere.models import Matiere
from UE.models import UniteE
from Enseignant.models import Enseignant
from Matiere.forms import MatiereForm,  SelectUE
from django import forms

# Create your views here.



def listermatieres(request):
	matieres = Matiere.objects.all()
	enseignants = Enseignant.objects.all()
	return render(request, 'contenu_html/listermatieres.html', locals())


def ajouterMatiere(request):

	if request.method == 'POST':

		if not request.session['ue']:
			unites =  UniteE.objects.all()
			form = SelectUE(request.POST, ues=unites)
			if form.is_valid() :
				id_ue = form.cleaned_data['select']
				request.session['id_ue'] = id_ue
				request.session['ue'] = True
				res = True
			e = get_object_or_404(UniteE, id=request.session['id_ue'])
			form=MatiereForm()
		else:
			form = MatiereForm(request.POST)
			if form.is_valid() :
				intitule = form.cleaned_data['intitule']
				code = form.cleaned_data['code']
				coefficient = form.cleaned_data['coefficient']
				e = get_object_or_404(UniteE, id=request.session['id_ue'])

				mat = Matiere(
						intitule=intitule,
						code=code,
						coefficient = coefficient,
						unite=e,
		                )
				mat.save()
				request.session['ue'] = False
				res2=True
			else :
				print("ERREUR")	
	else :
		unites =  UniteE.objects.all()
		request.session['ue'] = False
		form = SelectUE(ues=unites)
	return render(request, 'contenu_html/ajouterMatiere.html', locals())









