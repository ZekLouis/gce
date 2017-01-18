from __future__ import unicode_literals
from django.db import models
from UE.models import UE 
from Semestre.models import Semestre
from Annee.models import Annee
# Create your models here.

class Matiere(models.Model):
	intitule = models.CharField(max_length=30,null=False)
	code = models.CharField(max_length=30,null=False)
	coefficient = models.FloatField(default=1.0)
	ue = models.ForeignKey('UE.ue', null=True)	
	def __str__(self):
		return self.intitule.encode('utf8')

class Moyenne_matiere(models.Model):
	matiere=models.ForeignKey(Matiere, null=True)
	semestre=models.ForeignKey(Semestre, null=True)
	annee=models.ForeignKey(Annee, null=True)
	moyenne=models.FloatField(null=True)
	def __str__(self):
		return self.matiere.encode('utf8')