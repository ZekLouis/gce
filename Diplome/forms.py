#-*- coding: utf-8 -*-
from django import forms
from Diplome.models import Diplome

class DiplomeForm(forms.ModelForm):
	class Meta : 
		model = Diplome
		fields = '__all__'

class DiplomeFormCreation(forms.Form):
	def __init__(self,*args,**kwargs):
		self.annee = kwargs.pop('annee')
		super(DiplomeFormCreation,self).__init__(*args,**kwargs)
		nom = forms.CharField(max_length=100)