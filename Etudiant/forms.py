#-*- coding: utf-8 -*-
from django import forms
from Etudiant.models import Etu
from Groupe.models import Groupe

class EtudiantForm(forms.Form):
	nom = forms.CharField(max_length=100)
	prenom = forms.CharField(max_length=100)
	apogee = forms.IntegerField()


class SelectEtu(forms.Form):
	def __init__(self,*args,**kwargs):
		etudiant = kwargs.pop('etus')
		super(SelectEtu,self).__init__(*args,**kwargs)
		EtuChoices = [(etu.id,etu.nom) for etu in etudiant]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=EtuChoices)

class RenseignerEtu(forms.ModelForm):
	class Meta : 
		model = Etu
		fields = '__all__'
		exclude = ['nom','prenom']
