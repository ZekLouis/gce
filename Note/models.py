from __future__ import unicode_literals

from django.db import models
from Etudiant.models import Etu
from Matiere.models import Matiere

class Note(models.Model):
	valeur = models.FloatField()
	etudiant = models.ForeignKey(Etu, null=True)
	matiere = models.ForeignKey(Matiere, null=True)
	def __str__(self):
		return str(self.valeur)
