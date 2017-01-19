#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Etudiant.models import Etu
from Matiere.models import Matiere
from Annee.models import Annee
from Semestre.models import Semestre, InstanceSemestre
from UE.models import UE

class Resultat_Semestre(models.Model):
	instance_semestre = models.ForeignKey(InstanceSemestre, null=False)
	etudiant = models.ForeignKey(Etu, null=False)
	note = models.FloatField()
	note_calc = models.FloatField(null=True)
	resultat = models.CharField(max_length=15, null=True)
	resultat_pre_jury = models.CharField(max_length=15, null=True)
	resultat_jury = models.CharField(max_length=15, null=True)
	def __str__(self):
		return str(self.etudiant)
<<<<<<< HEAD
=======

<<<<<<< HEAD
=======
>>>>>>> 8e3e1ae186a98e66268d2cefc752139a989a8e99

>>>>>>> 546ec0433c90ae320adba731dd83b0023931bc05
class Resultat_UE(models.Model):
	instance_semestre = models.ForeignKey(InstanceSemestre, null=False)
	etudiant = models.ForeignKey(Etu, null=False)
	ue = models.ForeignKey(UE, null=False)
	note = models.FloatField()
	note_calc = models.FloatField(null=True)
	def __str__(self):
		return str(self.etudiant).encode('utf-8')

class Note(models.Model):
	valeur = models.FloatField()
	etudiant = models.ForeignKey(Etu, null=False)
	instance_semestre = models.ForeignKey(InstanceSemestre, null=False)
	matiere = models.ForeignKey(Matiere, null=False)
	def __str__(self):
		return str(self.valeur).encode('utf-8')
