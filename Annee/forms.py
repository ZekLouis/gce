#-*- coding: utf-8 -*-
from django import forms
from Annee.models import Annee



class AnneeForm(forms.ModelForm):
	class Meta : 
		model = Annee
		fields = '__all__'
