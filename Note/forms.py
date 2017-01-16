#-*- coding: utf-8 -*-
from django import forms
from Etudiant.models import Etu
from Matiere.models import Matiere
from Annee.models import Annee
from Semestre.models import Semestre
from UE.models import UE

class FileForm(forms.Form):
	fichier = forms.FileField()

class SelectNote(forms.Form):
	def __init__(self,*args,**kwargs):
		notes = kwargs.pop('notes')
		super(SelectNote,self).__init__(*args,**kwargs)
		NoteChoices = [(note[0],note[1]) for note in notes]
		self.fields['select'] = forms.ChoiceField(widget=forms.Select(), choices=NoteChoices)

class RenseignerNote(forms.Form):
	def __init__(self,*args,**kwargs):
		notes = kwargs.pop('notes')
		super(RenseignerNote,self).__init__(*args,**kwargs)

		for note in notes:
			print(note)
			if note.valeur is None:
				self.fields[note.matiere.code]  = forms.CharField(max_length=100,required=False)
			else:
				self.fields[note.matiere.code] = forms.CharField(max_length=100,required=False ,widget=forms.TextInput(attrs={'value': note.valeur}))
		