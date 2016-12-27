#-*- coding: utf-8 -*-
from django import forms
from Semestre.models import Semestre



class SemestreForm(forms.ModelForm):
	class Meta : 
		model = Semestre
		fields = '__all__'




