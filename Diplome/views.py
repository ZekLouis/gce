#-*- coding: utf-8 -*-
from django.shortcuts import render
from Diplome.models import Diplome
from Annee.models import Annee
from Diplome.forms import DiplomeForm
from Diplome.forms import DiplomeFormCreation, SelectDip, RenseignerDip
from Annee.forms import AnneeForm
from Matiere.models import Matiere
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

"""Cette vue permet d'afficher le détail d'un diplôme"""
def detailDiplome(request):
	if request.method == 'POST':
		Diplomes = Diplome.objects.all()
		form = SelectDip(request.POST, diplomes=Diplomes)
		if form.is_valid() :

			id_detdip = form.cleaned_data['select']
			request.session['id_detdip'] = id_detdip
			detdip = True

		d = get_object_or_404(Diplome, id=request.session['id_detdip'])
		sem_exist = Semestre.objects.filter(diplome__id=request.session['id_detdip'])

		if sem_exist:
			semestres = Semestre.objects.all().filter(diplome__id=request.session['id_detdip'])
			tab_ue = []
			for s in semestres :
				tab_ue.append(UE.objects.all().filter(semestre=s))

				ues = UE.objects.all().filter(semestre=s)
				tab_matieres = []
				for ue in ues :
					tab_matieres.append(Matiere.objects.all().filter(ue=ue))
			lignes = Semestre.objects.all().filter(diplome__id=request.session['id_detdip']).count() + 1
			#lignes += UE.objects.all().filter(semestre=s).count() + 1

			for unites in tab_ue :
				for unite in unites :
					lignes += 1
					for matieres in tab_matieres :
						for matiere in matieres :
							lignes += 1

			colonnes = 4
			lst = [[""] * colonnes for _ in range(lignes)]
			lst[0][0] = "Arborescence"
			lst[0][1] = "Coefficient"
			lst[0][2] = "Modification"
			lst[0][3] = "Suppression"

			i = 1

			for unite in tab_ue :
				i += 1
				lst[i][0]= unite[0].semestre.intitule
				lst[i][1]= "Coefficient"
				lst[i][2]= '<a href="../Semestre/modifierSemestre/">Modifier</a></td>'
				lst[i][3]= '<a href="../Semestre/supprsem/'+str(unite[0].semestre.id)+'">Supprimer</a></td>'
				
				for matieres in tab_matieres :
					i += 1
					lst[i][0]=matieres[0].ue
					lst[i][1]= matieres[0].ue.coefficient 
					lst[i][2]= '<a href="../UE/modifierUe/">Modifier</a></td>'
					lst[i][3] = '<a href="../UE/supprue/'+str(matieres[0].ue.id)+'">Supprimer</a></td>'
					for matiere in matieres :
						i += 1
						lst[i][0]= matiere.intitule
						lst[i][1]= matiere.coefficient
						lst[i][2]= '<a href="../Matiere/modifierMatiere/">Modifier</a></td>'
						lst[i][3] = '<a href="../Matiere/supprmat/'+str(matiere.id)+'">Supprimer</a></td>'
				#lst[1][1] = moy/coeff
				res = True
	else :
		Diplomes = Diplome.objects.all()
		form = SelectDip(diplomes=Diplomes)
	return render(request, 'contenu_html/detailDiplome.html', locals())
