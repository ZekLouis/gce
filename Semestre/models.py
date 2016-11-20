from __future__ import unicode_literals

from django.db import models
from Diplome.models import Diplome
# Create your models here.


class Semestre(models.Model):
	code = models.CharField(max_length=30,null=False)
	diplome = models.ForeignKey(Diplome, null=True)
	def __str__(self):
		return self.code