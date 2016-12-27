from __future__ import unicode_literals

from django.db import models

class Groupe(models.Model):
	nom = models.CharField(max_length=30, null=False)
	numero = models.IntegerField()
	def __str__(self):
		return self.nom
