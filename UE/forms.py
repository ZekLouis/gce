#-*- coding: utf-8 -*-
from django import forms
from UE.models import UniteE
from Semestre.models import Semestre


class UEForm(forms.ModelForm):
	class Meta : 
		model = UniteE
		fields = '__all__'
		exclude = ['semestre']


class SelectSemestre(forms.Form):
	
	def __init__(self,*args,**kwargs):
		semestre = kwargs.pop('semestres')
		super(SelectSemestre,self).__init__(*args,**kwargs)
		SemChoices = [(sem.id,sem.code) for sem in semestre]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=SemChoices)

