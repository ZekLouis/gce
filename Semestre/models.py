from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Semestre(models.Model):
	code = models.CharField(max_length=30,null=False)
	def __str__(self):
		return self.code