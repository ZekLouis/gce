from __future__ import unicode_literals

from django.db import models
from Annee.models import Annee
# Create your models here.


class Diplome(models.Model):
	intitule = models.CharField(max_length=30,null=False)
	def __str__(self):
		return self.intitule
