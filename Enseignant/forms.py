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

class SelectEns(forms.Form):
	def __init__(self,*args,**kwargs):
		enseignants = kwargs.pop('enseignants')
		super(SelectEns,self).__init__(*args,**kwargs)
		EnsChoices = [(ens.id,ens.nom) for ens in enseignants]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=EnsChoices)

class RenseignerEns(forms.Form):
	
	def __init__(self,*args,**kwargs):
		ens = kwargs.pop('enseignant')
		super(RenseignerEns,self).__init__(*args,**kwargs)

		if ens.nom is None:
			self.fields['nom']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['nom'] = forms.CharField(max_length=100,required=False ,widget=forms.TextInput(attrs={'value': ens.nom}))

		if ens.prenom is None:
			self.fields['prenom']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['prenom'] = forms.CharField(max_length=100,required=False ,widget=forms.TextInput(attrs={'value': ens.prenom}))

		if ens.matiere is None:
			self.fields['matiere'] = forms.ModelChoiceField(queryset=Matiere.objects.all(),required=False)
		else:
			self.fields['matiere']  = forms.ModelChoiceField(queryset=Matiere.objects.all().exclude(id=ens.matiere.id), empty_label=ens.matiere,required=False)