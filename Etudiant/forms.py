#-*- coding: utf-8 -*-
from django import forms
from Etudiant.models import Etu
from Groupe.models import Groupe
from Semestre.models import Semestre

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
	#  	model = Etu
	# 	fields = '__all__'
	#  	exclude = ['nom','prenom']
	def __init__(self,*args,**kwargs):
		etu = kwargs.pop('etudiant')
		super(RenseignerEtu,self).__init__(*args,**kwargs)

		if etu.nom is None:
			self.fields['nom']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['nom'] = forms.CharField(max_length=100,required=False ,widget=forms.TextInput(attrs={'value': etu.nom}))


		if etu.prenom is None:
			self.fields['prenom']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['prenom'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.prenom}))


		if etu.age is None:
			self.fields['age']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['age'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.age}))

		if etu.apogee is None:
			self.fields['apogee']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['apogee'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.apogee}))


		if etu.date_naissance is None:
			self.fields['date_naissance']  = forms.DateField(required=False)
		else:
			self.fields['date_naissance'] = forms.DateField(required=False, widget=forms.TextInput(attrs={'value': etu.date_naissance}))

		if etu.sexe is None:
			self.fields['sexe']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['sexe'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.sexe}))


		if etu.adresse is None:
			self.fields['adresse']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['adresse'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.adresse}))

		if etu.ine is None:
			self.fields['ine']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['ine'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.ine}))
		
		if etu.adresse_parents is None:
			self.fields['adresse_parents']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['adresse_parents'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.adresse_parents}))
		
		if etu.tel is None:
			self.fields['tel']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['tel'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.tel}))
		
		if etu.tel_par is None:
			self.fields['tel_par']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['tel_par'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.tel_par}))
		
		if etu.lieu_naissance is None:
			self.fields['lieu_naissance']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['lieu_naissance'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.lieu_naissance}))
		
		if etu.nationalite is None:
			self.fields['nationalite']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['nationalite'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.nationalite}))
		
		if etu.situation_familiale is None:
			self.fields['situation_familiale']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['situation_familiale'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.situation_familiale}))
		
		if etu.situation_militaire is None:
			self.fields['situation_militaire']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['situation_militaire'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.situation_militaire}))
		
		if etu.cate_socio_pro_chef_famille is None:
			self.fields['cate_socio_pro_chef_famille']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['cate_socio_pro_chef_famille'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.cate_socio_pro_chef_famille}))
		
		if etu.cate_socio_pro_autre_parent is None:
			self.fields['cate_socio_pro_autre_parent']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['cate_socio_pro_autre_parent'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.cate_socio_pro_autre_parent}))

		if etu.aide_financiere is None:
			self.fields['aide_financiere']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['aide_financiere'] = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.aide_financiere}))

		if etu.bourse is None:
			self.fields['bourse']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['bourse']  = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'value': etu.bourse}))

		if etu.groupe is None:
			self.fields['groupe'] = forms.ModelChoiceField(queryset=Groupe.objects.all(),required=False)
		else:
			self.fields['groupe']  = forms.ModelChoiceField(queryset=Groupe.objects.all().exclude(id=etu.groupe.id), empty_label=etu.groupe,required=False)
