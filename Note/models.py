#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Etudiant.models import Etu
from Matiere.models import Matiere
from Annee.models import Annee
from Semestre.models import Semestre
from UE.models import UE
class Resultat_Semestre(models.Model):
	annee = models.ForeignKey(Annee, null=False)
	etudiant = models.ForeignKey(Etu, null=False)
	semestre = models.ForeignKey(Semestre, null=False)
	note = models.FloatField()
	note_calc = models.FloatField(null=True)
	resultat = models.CharField(max_length=15, null=True)
	resultat_pre_jury = models.CharField(max_length=15, null=True)
	resultat_jury = models.CharField(max_length=15, null=True)
	def __str__(self):
		return str(self.etudiant)

class Resultat_UE(models.Model):
	annee = models.ForeignKey(Annee, null=False)
	etudiant = models.ForeignKey(Etu, null=False)
	ue = models.ForeignKey(UE, null=False)
	note = models.FloatField()
	note_calc = models.FloatField(null=True)
	def __str__(self):
		return str(self.etudiant)

class Note(models.Model):
	valeur = models.FloatField()
	etudiant = models.ForeignKey(Etu, null=False)
	annee = models.ForeignKey(Annee, null=True)
	matiere = models.ForeignKey(Matiere, null=False)
	def __str__(self):
		return str(self.valeur)
