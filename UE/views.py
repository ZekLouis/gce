from django.shortcuts import render, get_object_or_404
from UE.models import UniteE
from Semestre.models import Semestre
from Matiere.models import Matiere
from UE.forms import UEForm, SelectSemestre


# Create your views here.

"""Cette fonction permet de faire afficher toutes les UE"""
def listerUE(request):
	ues = UniteE.objects.all()
	return render(request, 'contenu_html/listerUE.html',{'ues': ues})


"""Cette fonction permet de faire afficher les matieres et les details d'une ue"""
def detailUE(request, id):
	ue = get_object_or_404(UniteE, id=id)
	matieres = Matiere.objects.filter(unite__id=id)
	return render(request, 'contenu_html/detailUE.html', locals())


def ajouterUE(request):

	if request.method == 'POST':

		if not request.session['sem']:
			sem = Semestre.objects.all()
			form = SelectSemestre(request.POST, semestres = sem)
			if form.is_valid() :
				id_sem = form.cleaned_data['select']
				request.session['id_sem'] = id_sem
				request.session['sem'] = True
				res = True
			e = get_object_or_404(Semestre, id=request.session['id_sem'])
			form=UEForm()
		else:
			form = UEForm(request.POST)
			if form.is_valid() :
				intitule = form.cleaned_data['intitule']
				code = form.cleaned_data['code']
				e = get_object_or_404(Semestre, id=request.session['id_sem'])
				coef = form.cleaned_data['coefficient']
				ue = UniteE(
						intitule=intitule,
						code=code,
						semestre=e,
						coef=coef,
		                )
				ue.save()
				request.session['sem'] = False
				res2=True
			else :
				print("ERREUR")	
	else :
		sem = Semestre.objects.all()
		request.session['sem'] = False
		form = SelectSemestre(semestres = sem)
	return render(request, 'contenu_html/ajouterUE.html', locals())

