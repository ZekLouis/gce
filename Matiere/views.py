from django.shortcuts import render, get_object_or_404
from Matiere.models import Matiere
from UE.models import UniteE
from Enseignant.models import Enseignant
from Matiere.forms import MatiereForm,  SelectUE, SelectMat, RenseignerMat
from django import forms

# Create your views here.



def listermatieres(request):
	matieres = Matiere.objects.all()
	enseignants = Enseignant.objects.all()
	return render(request, 'contenu_html/listermatieres.html', locals())

def supprmat(request, id):
	matiere = Matiere.objects.filter(id=id)
	enseignant = Enseignant.objects.filter(matiere=id)

	if enseignant :
		enseignant.delete()

	matiere.delete()
	return render(request, 'contenu_html/supprmat.html', locals())


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



def modifierMatiere(request):
	if request.method == 'POST':
		if not request.session['mat']:
			Matieres = Matiere.objects.all()
			form = SelectMat(request.POST, matieres=Matieres)
			if form.is_valid() :
				id_mat = form.cleaned_data['select']
				request.session['id_mat'] = id_mat
				request.session['mat'] = True
			res = True
			m = get_object_or_404(Matiere, id=request.session['id_mat'])
			form = RenseignerMat(matiere=m)
		else:
			m = get_object_or_404(Matiere, id=request.session['id_mat'])
			form = RenseignerMat(request.POST, matiere=m)
			if form.is_valid() :
				matiere = get_object_or_404(Matiere, id=request.session['id_mat'])
				if form.cleaned_data['intitule']:
					matiere.intitule = form.cleaned_data['intitule']
				if form.cleaned_data['coefficient']:
					matiere.coefficient = form.cleaned_data['coefficient']
				if form.cleaned_data['code']:
					matiere.code = form.cleaned_data['code']
				#if form.cleaned_data['unite']:
					#matiere.unite = form.cleaned_data['unite']
				matiere.save()	
				#request.session['mat'] = False
				res2=True
			else :
				print("Form Non Valide")	
	else :
		Matieres = Matiere.objects.all()
		request.session['mat'] = False
		form = SelectMat(matieres=Matieres)
	return render(request, 'contenu_html/modifierMatiere.html', locals())





