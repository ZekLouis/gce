#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Etudiant.models import Etu
from Matiere.models import Matiere
from Annee.models import Annee
from Semestre.models import Semestre

class Resultat_Semestre(models.Model):
	annee = models.ForeignKey(Annee, null=False)
	etudiant = models.ForeignKey(Etu, null=False)
	semestre = models.ForeignKey(Semestre, null=False)
	note = models.FloatField()
	note_calc = models.FloatField()
	resultat = models.CharField(max_length=15, null=False)
	resultat_pre_jury = models.CharField(max_length=15, null=False)
	resultat_jury = models.CharField(max_length=15, null=False)
	def __str__(self):
		return str(self.semestre)

class Note(models.Model):
	valeur = models.FloatField()
	etudiant = models.ForeignKey(Etu, null=False)
	annee = models.ForeignKey(Annee, null=False)
	matiere = models.ForeignKey(Matiere, null=False)
	def __str__(self):
		return str(self.valeur)
