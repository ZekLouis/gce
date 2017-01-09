#-*- coding: utf-8 -*-
from django import forms
from Etudiant.models import Etu
from Matiere.models import Matiere
from Annee.models import Annee
from Semestre.models import Semestre
from UE.models import UniteE

class FileForm(forms.Form):
	fichier = forms.FileField()

class SelectNote(forms.Form):
	def __init__(self,*args,**kwargs):
		notes = kwargs.pop('notes')
		super(SelectNote,self).__init__(*args,**kwargs)
		NoteChoices = [(note.id,note.etudiant) for note in notes]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=NoteChoices)

class RenseignerNote(forms.Form):
	
	def __init__(self,*args,**kwargs):
		note = kwargs.pop('note')
		super(RenseignerNote,self).__init__(*args,**kwargs)

		if note.valeur is None:
			self.fields['valeur']  = forms.CharField(max_length=100,required=False)
		else:
			self.fields['valeur'] = forms.CharField(max_length=100,required=False ,widget=forms.TextInput(attrs={'value': note.valeur}))


	#	if note.etudiant is None:
	#		self.fields['etudiant'] = forms.ModelChoiceField(queryset=Etu.objects.all(),required=False)
	#	else:
	#		self.fields['etudiant']  = forms.ModelChoiceField(queryset=Etu.objects.all().exclude(id=note.etudiant.id), empty_label=note.etudiant,required=False)
#
#		if note.annee is None:
#			self.fields['annee'] = forms.ModelChoiceField(queryset=Annee.objects.all(),required=False)
#		else:
#			self.fields['annee']  = forms.ModelChoiceField(queryset=Annee.objects.all().exclude(id=note.annee.id), empty_label=note.annee,required=False)
#
#		if note.ue is None:
#			self.fields['ue'] = forms.ModelChoiceField(queryset=UniteE.objects.all(),required=False)
#		else:
#			self.fields['ue']  = forms.ModelChoiceField(queryset=UniteE.objects.all().exclude(id=note.ue.id), empty_label=note.ue,required=False)
#
#		if note.matiere is None:
#			self.fields['matiere'] = forms.ModelChoiceField(queryset=Matiere.objects.all(),required=False)
#		else:
#			self.fields['matiere']  = forms.ModelChoiceField(queryset=Matiere.objects.all().exclude(id=note.matiere.id), empty_label=note.matiere,required=False)