from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Diplome(models.Model):
	nom = models.CharField(max_length=30,null=False)
	annee = models.FloatField(default=2016.0)
	def __str__(self):
		return self.nom
