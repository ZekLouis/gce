#-*- coding: utf-8 -*-
from django import forms
from Matiere.models import Matiere, UE, Semestre, Enseignant


class MatiereForm(forms.ModelForm):
	class Meta : 
		model = Matiere
		fields = '__all__'



class UEForm(forms.ModelForm):
	class Meta : 
		model = UE
		fields = '__all__'
		exclude = ['Semestre']


class SemestreForm(forms.ModelForm):
	class Meta : 
		model = Semestre
		fields = '__all__'


class EnseignantForm(forms.ModelForm):
	class Meta : 
		model = Enseignant
		fields = '__all__'

class SelectSemestre(forms.Form):
	semestres = Semestre.objects.all()
	OPTIONS = ()
	for semestre in semestres:
		OPTIONS = OPTIONS + (
						(semestre.id,semestre.code ),
			)	
	select = forms.ChoiceField(widget=forms.Select(), choices=OPTIONS)
	


