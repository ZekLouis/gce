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
		if not request.session['doc']:
			u = Semestre.objects.all()
			form = SelectSemestre(request.POST, semestres=u)
			if form.is_valid() :
				request.session['semestre'] = form.cleaned_data['select']
				request.session['doc'] = True
			semestre = Semestre.objects.all()
			form = SelectSemestre(semestres=semestre)
		else:
			u = Semestre.objects.all()
			form = SelectSemestre(request.POST, semestres=u)
			if form.is_valid() :
				semestrePrec = form.cleaned_data['select']
			style = xlwt.easyxf(' alignment: horizontal center, vertical center; borders: left thin, right thin, top thin, bottom thin;')
			book = open_workbook('DocJury/S2.xls',formatting_info=True)
			book.sheet_by_index(0)
			newFeuille = copy(book)
			etus = Etu.objects.all()
			ligne = 7
			cp =0
			for etu in etus:
				sem1=0
				sem2=0
				colonne = 0
				newFeuille.get_sheet(0).write(ligne,colonne,cp, style)
				colonne +=1
				newFeuille.get_sheet(0).write(ligne,colonne,etu.apogee, style)
				colonne +=1
				newFeuille.get_sheet(0).write(ligne,colonne,etu.nom, style)
				colonne +=1
				newFeuille.get_sheet(0).write(ligne,colonne,etu.prenom, style)
				colonne +=2
				semestre = Semestre.objects.get(id=request.session['semestre'])
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
					colonne =8
					newFeuille.get_sheet(0).write(ligne,colonne,resS.note, style)
					sem1 = resS.note
					colonne +=1
					newFeuille.get_sheet(0).write(ligne,colonne,resS.resultat, style)
				except Resultat_Semestre.DoesNotExist:
					print("probleme")
				semestre2 = Semestre.objects.get(id=semestrePrec)
				ues = UE.objects.all().filter(semestre=semestre2)
				colonne = 13
				for ue in ues:
					try:
						noteUE = Resultat_UE.objects.get(etudiant=etu, ue=ue)	
						newFeuille.get_sheet(0).write(ligne,colonne,noteUE.note, style)
						colonne +=1
					except Resultat_UE.DoesNotExist:
						print("probleme")
				try:
					resS = Resultat_Semestre.objects.get(etudiant = etu, semestre=semestre)
					colonne =16
					newFeuille.get_sheet(0).write(ligne,colonne,resS.note, style)
					sem2 = resS.note
					colonne +=1
					newFeuille.get_sheet(0).write(ligne,colonne,resS.resultat, style)
				except Resultat_Semestre.DoesNotExist:
					print("probleme")
				colonne = 21
				if sem1>0 and sem2>0:
					moyAn = (sem1+sem2)/2
					newFeuille.get_sheet(0).write(ligne,colonne,moyAn, style)
					colonne +=1
					if moyAn < 8:
						jury = "Barre"
					elif moyAn<10 and moyAn >= 8:
						jury = "NVAL"
					else:
						jury = "VAL"
					newFeuille.get_sheet(0).write(ligne,colonne,jury, style)
				ligne += 1
				cp+=1
				res=True
			print(semestre)
			newFeuille.save(semestre.code+'.xls')
	else :
		res=False
		semestre = Semestre.objects.all()
		request.session['doc'] = False
		form = SelectSemestre(semestres=semestre)
	return render(request, 'contenu_html/genererDocuments.html', locals())





'''	if request.method == 'POST':  
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

	
'''
	
