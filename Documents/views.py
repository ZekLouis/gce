from django.shortcuts import render, get_object_or_404

from xlwt import Workbook
from Etudiant.models import Etu
from Etudiant.models import Etu
from Matiere.models import Matiere
from Note.models import Note
from Etudiant.forms import SelectEtu
# Create your views here.


def genererDocuments(request):
	if request.method == 'POST':  
		if not request.session['etu']:
			Etudiants = Etu.objects.all()
			form = SelectEtu(request.POST, etus=Etudiants)
			if form.is_valid() :
				id_etu = form.cleaned_data['select']
				request.session['id_etu'] = id_etu
				request.session['etu'] = True
			book = Workbook()
			for etu in Etudiants:
    			# creation de la feuille 
				feuil = book.add_sheet(etu.nom)

				feuil.write(0,0,etu.prenom)
				feuil.write(1,0,etu.nom)
	
				# ajout des en-tetes
				feuil.write(3,0,'Matieres')
				feuil.write(3,1,'Moyenne')
				feuil.write(3,2,'Coefficient')

				matieres = Matiere.objects.all()
				i=4
				for mat in matieres:
    				
					# ajout des valeurs dans la ligne suivante
					ligne = feuil.row(i)
					matiere=mat.intitule
					ligne.write(0,matiere)
					notes=Note.objects.filter(etudiant=etu, matiere=mat)
					for nt in notes:
						ligne.write(1,nt.valeur)
					coeff=mat.coefficient
					ligne.write(2,coeff)
					i+=1
				# ajustement eventuel de la largeur d'une colonne
				feuil.col(0).width = 5000
				book.save('monsimple.xls')
				res = True
			e = get_object_or_404(Etu, id=request.session['id_etu'])   
	else :
		Etudiants = Etu.objects.all()
		request.session['etu'] = False
		form = SelectEtu(etus=Etudiants)
	return render(request, 'contenu_html/genererDocuments.html', locals())

