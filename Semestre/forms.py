#-*- coding: utf-8 -*-
from django import forms
from Semestre.models import Semestre
from Diplome.models import Diplome



class SemestreForm(forms.ModelForm):
	class Meta : 
		model = Semestre
		fields = '__all__'

class SelectSem(forms.Form):
	def __init__(self,*args,**kwargs):
		semestres = kwargs.pop('semestres')
		super(SelectSem,self).__init__(*args,**kwargs)
		SemChoices = [(sem.id,sem.code) for sem in semestres]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=SemChoices)

class RenseignerSem(forms.Form):
	
	def __init__(self,*args,**kwargs):
		sem = kwargs.pop('semestre')
		super(RenseignerSem,self).__init__(*args,**kwargs)

		if sem.intitule is None:
			self.fields['intitule']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['intitule'] = forms.CharField(max_length=100,required=False ,widget=forms.TextInput(attrs={'value': sem.intitule}))

		if sem.code is None:
			self.fields['code']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['code'] = forms.CharField(max_length=100,required=False ,widget=forms.TextInput(attrs={'value': sem.code}))

		if sem.diplome is None:
			self.fields['diplome'] = forms.ModelChoiceField(queryset=Diplome.objects.all(),required=False)
		else:
			self.fields['diplome']  = forms.ModelChoiceField(queryset=Diplome.objects.all().exclude(id=sem.diplome.id), empty_label=sem.diplome,required=False)