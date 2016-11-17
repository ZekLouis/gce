from django.shortcuts import render, get_object_or_404
from Matiere.models import Matiere
from Enseignant.forms import EnseignantForm, SelectMatiere
from Enseignant.forms import Enseignant

from django import forms

# Create your views here.


def ajouterEnseignant(request):

	if request.method == 'POST':

		if not request.session['mat']:
			ens = Enseignant.objects.all()
			form = SelectMatiere(request.POST, enseignants=ens)
			if form.is_valid() :
				id_mat = form.cleaned_data['select']
				request.session['id_mat'] = id_mat
				request.session['mat'] = True
				res = True
			e = get_object_or_404(Matiere, id=request.session['id_mat'])
			form=EnseignantForm()
		else:
			form = EnseignantForm(request.POST)
			if form.is_valid() :
				nom = form.cleaned_data['nom']
				prenom = form.cleaned_data['prenom']
				e = get_object_or_404(Matiere, id=request.session['id_mat'])

				ens = Enseignant(
						nom=nom,
						prenom=prenom,
						matiere=e,
		                )
				ens.save()
				request.session['mat'] = False
				res2=True
			else :
				print("ERREUR")	
	else :
		mats = Matiere.objects.all()
		request.session['mat'] = False
		form = SelectMatiere(matieres=mats)
	return render(request, 'contenu_html/ajouterEnseignant.html', locals())



