#-*- coding: utf-8 -*-
from django import forms
from Etudiant.models import Etu
from Groupe.models import Groupe

class EtudiantForm(forms.Form):
	nom = forms.CharField(max_length=100)
	prenom = forms.CharField(max_length=100)
	apogee = forms.IntegerField()


class SelectEtu(forms.Form):
	def __init__(self,*args,**kwargs):
		etudiant = kwargs.pop('etus')
		super(SelectEtu,self).__init__(*args,**kwargs)
		EtuChoices = [(etu.id,etu.nom) for etu in etudiant]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=EtuChoices)

class RenseignerEtu(forms.Form):
	# class Meta : 
	# 	model = Etu
	# 	fields = '__all__'
	# 	exclude = ['nom','prenom']
	def __init__(self,*args,**kwargs):
		nom = kwargs.pop('nom')
		super(RenseignerEtu,self).__init__(*args,**kwargs)
		self.fields['adresse'].widget = forms.TextInput(attrs={'size':nom})
		
	#nom = forms.CharField()
	prenom = forms.CharField(max_length=30)
	age = forms.IntegerField()
	apogee = forms.IntegerField()
	date_naissance = forms.DateField()
	sexe = forms.CharField(max_length=1)
	#adresse = forms.CharField(max_length=100)
	adresse = forms.CharField()
	ine = forms.CharField(max_length=100)
	adresse_parents = forms.CharField(max_length=100)
	tel = forms.IntegerField()
	tel_par = forms.IntegerField()
	lieu_naissance = forms.CharField(max_length=100)
	nationalite = forms.CharField(max_length=100)
	situation_familiale = forms.CharField(max_length=100)
	situation_militaire = forms.CharField(max_length=100)
	cate_socio_pro_chef_famille = forms.CharField(max_length=100)
	cate_socio_pro_autre_parent = forms.CharField(max_length=100)
	aide_financiere = forms.CharField(max_length=100)
	bourse = forms.CharField(max_length=100)
	# groupe = forms.ForeignKey(Groupe, null=True)

