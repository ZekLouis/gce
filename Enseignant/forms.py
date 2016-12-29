#-*- coding: utf-8 -*-
from django import forms
from Enseignant.models import Enseignant
from Matiere.models import Matiere






class EnseignantForm(forms.ModelForm):
	class Meta : 
		model = Enseignant
		fields = '__all__'
		exclude = ['matiere']
		


class SelectMatiere(forms.Form):	
	def __init__(self,*args,**kwargs):
		mats = kwargs.pop('matieres')
		super(SelectMatiere,self).__init__(*args,**kwargs)
		MatChoices = [(mat.id,mat.intitule) for mat in mats]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=MatChoices)

