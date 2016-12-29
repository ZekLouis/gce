from __future__ import unicode_literals

from django.db import models
from Matiere.models import Matiere

# Create your models here.

class Enseignant(models.Model):
	nom = models.CharField(max_length=30,null=False)
	prenom = models.CharField(max_length=30,null=False)
	matiere = models.ForeignKey(Matiere, null=True)
	def __str__(self):
		return self.id