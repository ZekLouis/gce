#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from operator import itemgetter, attrgetter, methodcaller
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf
import xlwt
from Etudiant.models import Etu
from UE.models import UE
from Note.models import Resultat_UE
from Note.models import Resultat_Semestre
from Matiere.models import Matiere
from Semestre.models import Semestre, InstanceSemestre
from Note.models import Note
from UE.forms import SelectSemestre
from Semestre.forms import SelectInstanceSemestre
# Create your views here.

class etudiant:
	def __init__ (self, numero,resultat):
	#Definition des attributs de chaque instance
		self.numero = numero
		self.resultat = resultat


def testValidite(string, num):
	if string == "VAL":
		note=0*num
	elif string == "VALC":
		note=1*num
	elif string == "ADAC":
		note=2*num
	elif string == "NATT":
		note=3*num
	elif string == "NATB":
		note=4*num
	elif string == "probleme":
			note=4*num
	else:
		note=5*num
	return note


def ordreListe(semestrePrec, semestre):
	liste = []
	etus = Etu.objects.all()
	for etu in etus:
		note1 = ""
		note2 = ""
		str = 0
		semestre1 = InstanceSemestre.objects.get(id=semestrePrec)
		semestre2 = InstanceSemestre.objects.get(id=semestre)
		try:
			note1 = Resultat_Semestre.objects.get(etudiant = etu, instance_semestre=semestre1)
			str = testValidite(note1.resultat, 1000)
			note2 = Resultat_Semestre.objects.get(etudiant = etu, instance_semestre=semestre2)
			str += testValidite(note2.resultat, 100)
			moyG = (note1.note+note2.note)/2
			str-=moyG
		except Resultat_Semestre.DoesNotExist:
			print("probleme")
		if str == 0:
			str = 10000
		e = etudiant(etu.apogee, str)
		liste.append(e)
		liste = sorted(liste, key=attrgetter('resultat'))
	for li in liste:
		print (li.numero, li.resultat)
	return liste




"""Cette vue permet de generer les documents"""
def genererDocuments(request):
	if request.method == 'POST':
		if not request.session['doc']:
			u = InstanceSemestre.objects.all()
			form = SelectInstanceSemestre(request.POST, instanceSemestres=u)
			if form.is_valid() :
				request.session['semestre'] = form.cleaned_data['select']
				request.session['doc'] = True
			semestre = InstanceSemestre.objects.all()
			form = SelectInstanceSemestre(instanceSemestres=semestre)
		else:
			u = InstanceSemestre.objects.all()
			form = SelectInstanceSemestre(request.POST, instanceSemestres=u)
			if form.is_valid() :
				semestrePrec = form.cleaned_data['select']
			style = xlwt.easyxf(' alignment: horizontal center, vertical center; borders: left thin, right thin, top thin, bottom thin;')
			book = open_workbook('docJury/S2.xls',formatting_info=True)
			book.sheet_by_index(0)
			newFeuille = copy(book)
			etus = Etu.objects.all()
			ligne = 7
			cp =0
			liste = ordreListe(semestrePrec, request.session['semestre'])
			for etu in liste:
				etudi = Etu.objects.get(apogee=etu.numero)
				sem1=0
				sem2=0
				colonne = 0
				newFeuille.get_sheet(0).write(ligne,colonne,cp, style)
				colonne +=1
				newFeuille.get_sheet(0).write(ligne,colonne,etudi.apogee, style)
				colonne +=1
				newFeuille.get_sheet(0).write(ligne,colonne,etudi.nom, style)
				colonne +=1
				newFeuille.get_sheet(0).write(ligne,colonne,etudi.prenom, style)
				colonne +=2
				semestre = InstanceSemestre.objects.get(id=semestrePrec)
				s = semestre.semestre
				ues = UE.objects.all().filter(semestre=s)
				for ue in ues:
					try:
						noteUE = Resultat_UE.objects.get(etudiant=etudi, ue=ue)	
						newFeuille.get_sheet(0).write(ligne,colonne,noteUE.note, style)
						colonne +=1
					except Resultat_UE.DoesNotExist:
						print("probleme")
				try:
					resS = Resultat_Semestre.objects.get(etudiant = etudi, instance_semestre=semestre)
					colonne =8
					newFeuille.get_sheet(0).write(ligne,colonne,resS.note, style)
					sem1 = resS.note
					colonne +=1
					newFeuille.get_sheet(0).write(ligne,colonne,resS.resultat, style)
				except Resultat_Semestre.DoesNotExist:
					print("probleme")
				semestre2 = InstanceSemestre.objects.get(id=request.session['semestre'])
				ues = UE.objects.all().filter(semestre=semestre2.semestre)
				colonne = 13
				for ue in ues:
					try:
						noteUE = Resultat_UE.objects.get(etudiant=etudi, ue=ue)	
						newFeuille.get_sheet(0).write(ligne,colonne,noteUE.note, style)
						colonne +=1
					except Resultat_UE.DoesNotExist:
						print("probleme")
				try:
					resS2 = Resultat_Semestre.objects.get(etudiant = etudi, instance_semestre=semestre2)
					colonne =16
					newFeuille.get_sheet(0).write(ligne,colonne,resS2.note, style)
					sem2 = resS2.note
					colonne +=1
					newFeuille.get_sheet(0).write(ligne,colonne,resS2.resultat, style)
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
			newFeuille.save(semestre.semestre.code_ppn+'.xls')
	else :
		res=False
		semestre = InstanceSemestre.objects.all()
		request.session['doc'] = False
		form = SelectInstanceSemestre(instanceSemestres=semestre)
	return render(request, 'contenu_html/genererDocuments.html', locals())




