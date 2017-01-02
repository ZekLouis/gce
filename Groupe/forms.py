#-*- coding: utf-8 -*-
from django import forms
from Groupe.models import Groupe

class GroupeForm(forms.ModelForm):
	class Meta : 
		model = Groupe
		fields = '__all__'

class SelectGrp(forms.Form):
	def __init__(self,*args,**kwargs):
		groupes = kwargs.pop('groupes')
		super(SelectGrp,self).__init__(*args,**kwargs)
		GrpChoices = [(grp.id,grp.nom) for grp in groupes]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=GrpChoices)

class RenseignerGrp(forms.Form):
	# class Meta : 
	#  	model = Etu
	# 	fields = '__all__'
	#  	exclude = ['nom','prenom']
	def __init__(self,*args,**kwargs):
		grp = kwargs.pop('groupe')
		super(RenseignerGrp,self).__init__(*args,**kwargs)

		if grp.nom is None:
			self.fields['nom']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['nom'] = forms.CharField(max_length=100,required=False ,widget=forms.TextInput(attrs={'value': grp.nom}))


		if grp.numero is None:
			self.fields['numero']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['numero'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': grp.numero}))