#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from io import StringIO
from django import forms
from Note.forms import FileForm
from Etudiant.models import Etu
from Note.models import Note
from Matiere.models import Matiere

import csv
"""Cette fonction permet d'insérer une virgule a un index donné"""
def insert_comma(string, index):
    return string[:index] + ',' + string[index:]

"""Cette fonction permet de traiter les notes d'un élève"""
def traitement_eleve(ligne,notes,code_eleve,diplome,ret_notes,ret_etu,ret_mat):
	nb_elements_tab = len(ligne)
	apogee=ligne[0]
	nom=ligne[1]
	prenom=ligne[2]

	try :
		etudiant = Etu.objects.get(apogee=apogee)
		print(etudiant)
		print(code_eleve[0],apogee,code_eleve[1],nom,code_eleve[2],prenom)
		print("Diplome : " + diplome)
		#Il faudra get l'élève ici avec son num apogée
		for i in range(3,nb_elements_tab):
			print(notes[i])
			#On ajoutera ici chaque note à l'étudiant
			#Le tableau notes contient le code de la note et ligne la note
			if ligne[i] == "":
				#Cas ou il n'y a pas de notes
				# print(notes[i],"null")
				note = "null"
			elif len(ligne[i]) == 5 and "," not in ligne[i]:
				#Cas ou la note fait 5 char de long ex :"12369"
				note = insert_comma(ligne[i],2)
				# print(notes[i],note)
			elif len(ligne[i]) == 4 and "," not in ligne[i]:
				#Cas ou la note fait 4 char de long ex :"8563"
				note = insert_comma(ligne[i],1)
				# print(notes[i],note)
			else:
				#Cas classique ex :""4,5""
				# print(notes[i],ligne[i])
				note = ligne[i]

			try :
				matiere = Matiere.objects.get(code=notes[i])
				if note != "null":
					note = note.replace(",", ".")
					note = float(note)
					n, created = Note.objects.get_or_create(valeur=note,etudiant=etudiant,matiere=matiere)
					#n = Note(
					#		valeur=note,
					#		etudiant=etudiant,
					#		matiere=matiere,
					#	)
					if created==False:
    						#print("La note",note,etudiant,matiere,"existait deja, elle n'a pas ete ajoutee")
							ret_notes = ret_notes + "<p>La note "+str(note)+" "+etudiant.nom+" "+matiere.intitule+" existait deja, elle n'a pas ete ajoutee</p>"
					n.save()
			except Matiere.DoesNotExist :
				print("Matiere",notes[i],"n'existe pas")
				ret_mat = ret_mat + "<p>La matiere "+notes[i]+" n'existe pas</p>"
	except Etu.DoesNotExist :
		print("L'étudiant",nom,prenom,apogee,"n'existe pas")
		ret_etu = ret_etu + "<p>L'etudiant "+nom+" "+prenom+" "+str(apogee)+" n'existe pas</p>"
	return ret_notes,ret_etu,ret_mat

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

			ret_notes = ""

			ret_etu = ""

			ret_mat = ""

			for row in read:
				if row[0].isdigit():
					ret_notes, ret_etu, ret_mat = traitement_eleve(row,code_notes,code_eleve,diplome,ret_notes,ret_etu,ret_mat)
				elif "Bilan" in row[0]:
					print(row[0])
				elif row[0] == "" and row[1] == "" and row[2] == "" :
					code_notes = row
				elif "GMP" in row[0]:
					diplome = row[0]
				else:
					code_eleve = row

			print(ret_notes,ret_etu,ret_mat)
			if ret_notes=="" and ret_etu=="" and ret_mat=="":
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