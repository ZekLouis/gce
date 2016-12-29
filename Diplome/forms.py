#-*- coding: utf-8 -*-
from django import forms
from Diplome.models import Diplome

class DiplomeForm(forms.ModelForm):
	class Meta : 
		model = Diplome
		fields = '__all__'

class DiplomeFormCreation(forms.Form):
	def __init__(self,*args,**kwargs):
		self.MonAnnee = kwargs.pop('annee')
		super(DiplomeFormCreation,self).__init__(*args,**kwargs)
			self.fields['annee'] = forms.ChoiceField(label="Diplome", choices=[(x.plug_ip,x.nom) for x in Diplome.objects.filter(annee = MonAnnee)])
