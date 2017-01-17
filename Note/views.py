#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from io import StringIO
from django import forms
from Note.forms import FileForm, SelectNote, RenseignerNote
from Etudiant.forms import SelectEtu
from UE.forms import SelectSemestre
from Etudiant.models import Etu
from Note.models import Note,Resultat_Semestre,Resultat_UE
from Matiere.models import Matiere
from Semestre.models import Semestre
from Annee.models import Annee
from UE.models import UE
import csv
import datetime

#Cette vue permet d'afficher les résultats jury pour un étudiant
def resultatJury(request):
	if request.method == 'POST':
			Etudiants = Etu.objects.all()
			form = SelectEtu(request.POST, etus=Etudiants)
			if form.is_valid() :
				id_etu = form.cleaned_data['select']
				request.session['id_etu'] = id_etu
				request.session['etu'] = True
				res = True
				resultatsJury = Resultat_Semestre.objects.filter(etudiant_id=request.session['id_etu'])
			else :
				print("ERREUR : MODIFIER Diplome : VIEW modifierDiplome : formulaire")	
	else :
		Etudiants = Etu.objects.all()
		request.session['etu'] = False
		form = SelectEtu(etus=Etudiants)
	return render(request, 'contenu_html/resultatJury.html', locals())



"""Cette vue permet de supprimer tous les étudiants"""
def suppall(request):
	Note.objects.all().delete()
	return listernotes(request)



"""Cette fonction permet d'insérer une virgule a un index donné"""
def insert_comma(string, index):
    return string[:index] + ',' + string[index:]

"""Cette fonction permet de traiter les notes d'un élève"""
def traitement_eleve(ligne,notes,code_eleve,diplome,ret_notes,ret_etu,ret_mat,ret_ue,ret_sem,compteur_eleve_error,nb_ligne,compteur_note_error,compteur_note):
	nb_elements_tab = len(ligne)
	apogee=ligne[0]
	nom=ligne[1]
	prenom=ligne[2]

	#Création de l'année 
	now = datetime.datetime.now()
	year = now.year
	yearMoins = year-1
	annee, cr = Annee.objects.get_or_create(intitule=str(yearMoins) +"-"+str(year))
	annee.save()

	try :
		etudiant = Etu.objects.get(apogee=apogee)
		print(etudiant)
		print(code_eleve[0],apogee,code_eleve[1],nom,code_eleve[2],prenom)
		print("Diplome : " + diplome)
		#Il faudra get l'élève ici avec son num apogée
		for i in range(3,nb_elements_tab):
			nb_ligne=nb_ligne+1
			print(notes[i])
			#On ajoutera ici chaque note à l'étudiant
			#Le tableau notes contient le code de la note et ligne la note
			if ligne[i] == "":
				#Cas ou il n'y a pas de notes
				# print(notes[i],"null")
				note = "null"
				compteur_note_error = compteur_note_error + 1
			elif len(ligne[i]) == 5 and "," not in ligne[i]:
				#Cas ou la note fait 5 char de long ex :"12369"
				note = insert_comma(ligne[i],2)
				compteur_note = compteur_note +1
				# print(notes[i],note)
			elif len(ligne[i]) == 4 and "," not in ligne[i]:
				#Cas ou la note fait 4 char de long ex :"8563"
				note = insert_comma(ligne[i],1)
				compteur_note = compteur_note+1
				# print(notes[i],note)
			else:
				#Cas classique ex :""4,5""
				# print(notes[i],ligne[i])
				note = ligne[i]
				compteur_note = compteur_note +1

			try :
				#si on lit un chaine contenant par "Semestre"	
				if "Semestre" in notes[i] :
					semestre = Semestre.objects.get(code=notes[i])
					note = note.replace(",", ".")
					note = float(note)
					ResSem = Resultat_Semestre.objects.get_or_create(
						annee = annee,
						etudiant = etudiant,
						semestre = semestre,
						note= note,
						note_calc = 0.0,#note qui sera modifiée dans une autre vue
						resultat = "",
						resultat_pre_jury= "",
						resultat_jury= ""
					)
				#si on lit un chaine contenants par "UE"	
				elif "UE" in notes[i]:
					#on commence par récupérer l'ue à l'aide de son code 
					ue = UE.objects.get(code=notes[i])
					note = note.replace(",", ".")
					note = float(note)
					#on peut maintenant récupérer toutes les informations 
					Resultat_UE.objects.get_or_create(
						annee = annee,
						etudiant = etudiant,
						ue = ue,
						note= note,
						note_calc = 0.0,#note qui sera modifiée dans une autre vue
					)	

				else:	
					#on commence par créer la matière	
					matiere = Matiere.objects.get(code=notes[i])
					if note != "null":
						note = note.replace(",", ".")
						note = float(note)
						n, created = Note.objects.get_or_create(valeur=note,etudiant=etudiant,matiere=matiere,annee=annee)
						
						if created==False:
								ret_notes.add(str(note)+" "+etudiant.nom+" "+matiere.intitule)
						n.save()
			except Matiere.DoesNotExist :
				ret_mat.add("La matiere "+notes[i]+" n'existe pas")
			except Semestre.DoesNotExist :
				ret_sem.add("Le semestre "+notes[i]+" n'existe pas")
			except UE.DoesNotExist :
				ret_ue.add("L'UE "+notes[i]+" n'existe pas")
	except Etu.DoesNotExist :
		print("L'étudiant",nom,prenom,apogee,"n'existe pas")
		ret_etu = ret_etu.append("L'etudiant "+nom+" "+prenom+" "+str(apogee)+" n'existe pas")
		compteur_eleve_error=compteur_eleve_error+1
	return ret_notes,ret_etu,ret_mat,ret_ue,ret_sem,compteur_eleve_error,nb_ligne,compteur_note_error,compteur_note

# Create your views here.
"""Cette fonction permet d'importer via un formulaire un fichier CSV complet exporté par signature"""
def importer_csv(request):
	if request.method == "POST":
		form = FileForm(request.POST, request.FILES)
		if form.is_valid() :
			fichier = form.cleaned_data['fichier']
			
			import csv
			csvf = StringIO(fichier.read().decode('latin-1'))
			read = csv.reader(csvf, delimiter=',')

			nb_ligne = 0
			compteur_eleve=0
			compteur_eleve_error=0
			compteur_note=0
			compteur_note_error=0

			ret_notes = set()
			ret_etu = set()
			ret_mat = set()
			ret_ue = set()
			ret_sem = set()

			for row in read:
				if row[0].isdigit():
					compteur_eleve = compteur_eleve+1
					ret_notes, ret_etu, ret_mat,ret_ue,ret_sem,compteur_eleve_error,nb_ligne,compteur_note_error,compteur_note = traitement_eleve(row,code_notes,code_eleve,diplome,ret_notes,ret_etu,ret_mat,ret_ue,ret_sem,compteur_eleve_error,nb_ligne,compteur_note_error,compteur_note)
				elif "Bilan" in row[0]:
					print(row[0])
				elif row[0] == "" and row[1] == "" and row[2] == "" :
					code_notes = row
				elif "GMP" in row[0]:
					diplome = row[0]
				else:
					code_eleve = row
	
			print(ret_notes,ret_etu,ret_mat)
			if len(ret_notes)==0 and len(ret_etu)==0 and len(ret_mat)==0:
    				perf=True
			else:
					perf=False
			res = True
		else :
			print("ERREUR : IMPORT CSV : VIEW importer_csv : Formulaire")
	else :
		form = FileForm()
	return render(request, 'contenu_html/select_csv.html', locals())

"""Cette fonction permet de lister toutes les notes"""
def listernotes(request):
	notes = Note.objects.all().order_by('etudiant__nom')
	return render(request, 'contenu_html/listernotes.html',{'notes': notes})

"""Cette vue permet de supprimer une note"""
def supprnote(request, id):
	note = Diplome.objects.filter(id=id)

	note.delete()
	return render(request, 'contenu_html/supprnote.html', locals())

"""Cette vue permet de modifier une note"""
def modifierNote(request):
	if request.method == 'POST':
		if not request.session['note']:
			Notes = list(set(Note.objects.values_list('etudiant_id','etudiant__nom' )))
			form = SelectNote(request.POST, notes=Notes)
			if form.is_valid() :
				etudiant = form.cleaned_data['select']
				request.session['etudiant'] = etudiant
				request.session['note'] = True
			res = True
			NOTES = Note.objects.filter(etudiant_id=request.session['etudiant'])
			form = RenseignerNote(notes=NOTES)
	
		else:
			NOTES = Note.objects.filter(etudiant_id=request.session['etudiant'])
			form = RenseignerNote(request.POST, notes=NOTES)
			if form.is_valid() :
				for note in NOTES:
					note_temp = get_object_or_404(Note, id=note.id)
					if form.cleaned_data[note_temp.matiere.code]:
						note_temp.valeur = form.cleaned_data[note.matiere.code]
				note_temp.save()	
				res2=True
			else :
				print("ERREUR : MODIFIER Note : VIEW modifierNote : formulaire")	
	else :
		Notes = list(set(Note.objects.values_list('etudiant_id', 'etudiant__nom')))
		request.session['note'] = False
		form = SelectNote(notes=Notes)
	return render(request, 'contenu_html/modifierNote.html', locals())



def renseignerResultat(request):
	if request.method == 'POST':
		u = Semestre.objects.all()
		form = SelectSemestre(request.POST, semestres=u)
		if form.is_valid() :
			semes = form.cleaned_data['select']
			semestre = Semestre.objects.get(id=semes)
		etus = Etu.objects.all()
		ues  = UE.objects.filter(semestre=semes)
		
		for etu in etus:
			try:
				res = Resultat_Semestre.objects.get(etudiant=etu,semestre = semes)
				if res is not None:
					notes = Note.objects.all().filter(etudiant=etu)
					moy = 0
					coeff = 0
					for ue in ues:
						matieres = Matiere.objects.filter(ue=ue)
						for matiere in matieres :
							for note in notes :
								if note.matiere.intitule == matiere.intitule :
									note = Note.objects.get(etudiant=etu, matiere=matiere)
									print(note)

									moy += (note.valeur*matiere.coefficient)
									coeff += matiere.coefficient
						moyG = moy/coeff
						resultatSem = Resultat_Semestre.objects.get(etudiant=etu, semestre=semes)
						if moyG < 8:
							jury = "Barre"
						elif moyG<10 and moyG >= 8:
							jury = "NVAL"
						else:
							jury = "VAL"
						resultatSem.note_calc = moyG
						resultatSem.resultat = jury
						
						resultatSem.save()
			except Resultat_Semestre.DoesNotExist:
				print("probleme")
	else :
		u = Semestre.objects.all()
		form = SelectSemestre(semestres=u)
	return render(request, 'contenu_html/listerResultat.html',locals())