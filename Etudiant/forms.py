#-*- coding: utf-8 -*-
from django import forms
from Etudiant.models import Etu, Groupe

class GroupeForm(forms.Form):
	nom = forms.CharField(max_length=100, error_messages={'required': 'Please enter a name'}, widget=forms.TextInput(attrs={'class': 'special'}))
	numero = forms.IntegerField(error_messages={'required': 'Please enter a number'}, widget=forms.TextInput(attrs={'class': 'special'}))


class EtudiantForm(forms.Form):
	nom = forms.CharField(max_length=100)
	prenom = forms.CharField(max_length=100)
	apogee = forms.IntegerField()


class SelectEtu(forms.Form):
	etus = Etu.objects.all()
	OPTIONS = ()
	for etu in etus:
		OPTIONS = OPTIONS + (
						(etu.id,etu.nom),
			)
	select = forms.ChoiceField(widget=forms.Select(), choices=OPTIONS)

class RenseignerEtu(forms.ModelForm):
	class Meta : 
		model = Etu
		fields = '__all__'
		exclude = ['nom','prenom']
