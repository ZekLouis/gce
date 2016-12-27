#-*- coding: utf-8 -*-
from django import forms
from UE.models import UniteE
from Matiere.models import Matiere



class MatiereForm(forms.ModelForm):
	class Meta : 
		model = Matiere
		fields = '__all__'
		exclude = ['unite']


class SelectUE(forms.Form):
	
	def __init__(self,*args,**kwargs):
		unites = kwargs.pop('ues')
		super(SelectUE,self).__init__(*args,**kwargs)
		UeChoices = [(ue.id,ue.code) for ue in unites]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=UeChoices)



