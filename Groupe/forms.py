#-*- coding: utf-8 -*-
from django import forms
from Groupe.models import Groupe

class GroupeForm(forms.ModelForm):
	class Meta : 
		model = Groupe
		fields = '__all__'
