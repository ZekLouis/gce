from __future__ import unicode_literals

from django.db import models
from Semestre.models import Semestre 

# Create your models here.


class UniteE(models.Model):
	intitule = models.CharField(max_length=30,null=False)
	code = models.CharField(max_length=30,null=False)
	semestre = models.ForeignKey(Semestre, null=True)
	coefficient = models.FloatField(null=True)
	def __str__(self):
		return self.code
    

