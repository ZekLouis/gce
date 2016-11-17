from __future__ import unicode_literals
from django.db import models
from UE.models import UniteE 
# Create your models here.

class Matiere(models.Model):
	intitule = models.CharField(max_length=30,null=False)
	code = models.CharField(max_length=30,null=False)
	coefficient = models.FloatField(default=1.0)
	unite = models.ForeignKey('UE.UniteE', null=True)	
	def __str__(self):
		return self.intitule
