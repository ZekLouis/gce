#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf
import xlwt
from Etudiant.models import Etu
from UE.models import UE
from Note.models import Resultat_UE
from Note.models import Resultat_Semestre
from Matiere.models import Matiere
from Semestre.models import Semestre
from Note.models import Note
from UE.forms import SelectSemestre
# Create your views here.

"""Cette vue permet de generer les documents"""
def genererDocuments(request):
	if request.method == 'POST':  
		semestre = Semestre.objects.all()
		form = SelectSemestre(request.POST, semestres=semestre)
		if form.is_valid() :
			request.session['id_semestre'] = form.cleaned_data['select']
		#book = Workbook()
		style = xlwt.easyxf(' alignment: horizontal center, vertical center; borders: left thin, right thin, top thin, bottom thin;')
		book = open_workbook('DocJury/S2.xls',formatting_info=True)
		book.sheet_by_index(0)
		newFeuille = copy(book)
		etus = Etu.objects.all()
		ligne = 7
		cp =0
		for etu in etus:
			colonne = 0
			newFeuille.get_sheet(0).write(ligne,colonne,cp, style)
			colonne +=1
			newFeuille.get_sheet(0).write(ligne,colonne,etu.apogee, style)
			colonne +=1
			newFeuille.get_sheet(0).write(ligne,colonne,etu.nom, style)
			colonne +=1
			newFeuille.get_sheet(0).write(ligne,colonne,etu.prenom, style)
			colonne +=2
			semestre = Semestre.objects.all().filter(id=request.session['id_semestre'])
			print(semestre)
			ues = UE.objects.all().filter(semestre=semestre)
			for ue in ues:
				try:
					noteUE = Resultat_UE.objects.get(etudiant=etu, ue=ue)	
					newFeuille.get_sheet(0).write(ligne,colonne,noteUE.note, style)
					colonne +=1
				except Resultat_UE.DoesNotExist:
					print("probleme")
			try:
				resS = Resultat_Semestre.objects.get(etudiant = etu, semestre=semestre)
				newFeuille.get_sheet(0).write(ligne,colonne,resS.note, style)
				colonne +=1
				newFeuille.get_sheet(0).write(ligne,colonne,resS.resultat, style)
			except Resultat_Semestre.DoesNotExist:
				print("probleme")
			ligne += 1
			cp+=1
			res=True
		newFeuille.save('output.xls')
	else:
		res=False
		semestre = Semestre.objects.all()
		form = SelectSemestre(semestres=semestre)
	return render(request, 'contenu_html/genererDocuments.html', locals())



'''for etu in Etudiants:
    			# creation de la feuille 
				feuil = book.add_sheet(etu.nom)

				feuil.write(0,0,etu.prenom)
				feuil.write(1,0,etu.nom)
	
				# ajout des en-tetes
				feuil.write(3,0,'Matieres')
				feuil.write(3,1,'Moyenne')
				feuil.write(3,2,'Coefficient')

				matieres = Matiere.objects.all()
				i=4
				for mat in matieres:
    				
					# ajout des valeurs dans la ligne suivante
					ligne = feuil.row(i)
					matiere=mat.intitule
					ligne.write(0,matiere)
					notes=Note.objects.filter(etudiant=etu, matiere=mat)
					for nt in notes:
						ligne.write(1,nt.valeur)
					coeff=mat.coefficient
					ligne.write(2,coeff)
					i+=1
				# ajustement eventuel de la largeur d'une colonne
				feuil.col(0).width = 5000
				#book.save('DocJury/S2.xls')
				res = True
			e = get_object_or_404(Etu, id=request.session['id_etu'])'''

