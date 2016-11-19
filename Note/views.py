#-*- coding: utf-8 -*-
from django.shortcuts import render
from io import StringIO
from django import forms
from Note.forms import FileForm

# Create your views here.

def importer_csv(request):
	if request.method == "POST":
		form = FileForm(request.POST, request.FILES)
		if form.is_valid() :
			fichier = form.cleaned_data['fichier']
	
			import csv
			csvf = StringIO(fichier.read().decode())
			read = csv.reader(csvf, delimiter=',')

			i = 0
			for row in read:
				i += 1
				if(i==2):
					print row[4],row[5]
				if(i>4):
					print row[4],row[5]
					#if(row):
						#print(row[0])
						#if i == 1:
						#	intitule_matiere = row[0].split(": ")
						#	intitule_matiere = intitule_matiere[1]
						#if i == 2:
						#	date_n = row[0].split(": ")
						#	date_n = date_n[1]
						#	date_n = datetime.strptime(date_n, '%d/%m/%Y').strftime('%Y-%m-%d')
						#if i == 3:
						#	data = row[0].split(": ")
						#	enseignant = data[1].split(" ")
						#	prenom = enseignant[0]
						#	nom = enseignant[1]
						#	m, created = Matiere.objects.get_or_create(
						#		intitule=intitule_matiere,
						#		nom_ens=nom,
						#		pre_ens=prenom,
						#		)
				#else:
				#	e, created = Etu.objects.get_or_create(
			    #            nom=row[0],
			    #            prenom=row[1],
			    #            )
				#	n = Note(
			        #        note=row[2],
			        #        etu=e,
			         #       matiere=m,
			         #       date_note=date_n,
			         #       )
					#n.save()
			res = True
		else :
			print("ERREUR : IMPORT CSV : VIEW importer_csv : Formulaire")
	else :
		form = FileForm()
	return render(request, 'contenu_html/select_csv.html', locals())