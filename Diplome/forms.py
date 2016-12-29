#-*- coding: utf-8 -*-
from django import forms
from Diplome.models import Diplome

class DiplomeForm(forms.ModelForm):
	class Meta : 
		model = Diplome
		fields = '__all__'

class DiplomeFormCreation(forms.Form):
	def __init__(self,*args,**kwargs):
		monAnnee = kwargs.pop('monAnnee')
		super(DiplomeFormCreation,self).__init__(*args,**kwargs)
		self.fields['monAnnee'] = forms.ChoiceField(label="Diplome",choices=[(x.plug_ip, x.nom) for x in Diplome.objects.filter(annee = monAnnee)])

