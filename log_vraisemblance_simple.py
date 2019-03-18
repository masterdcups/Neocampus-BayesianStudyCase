import passageStringEntierPourMatrice as conv
import sys
import numpy as np
import csv
import math

def appelle_fonction(fonction,valTemp,valLum,valCo2,valHum):
	if fonction == "temperature":
		return conv.temperature(valTemp)
	if fonction == "luminosite":
		return conv.luminosite(valLum)
	if fonction == "co2":
		return conv.co2(valCo2)
	if fonction == "humidite":
		return conv.humidite(valHum)

	

def nb_valeur_fonction(fonction):
	if fonction == "co2":
		return 6
	else:
		return 11




def calcul_score_log_vraissemblance(fp,fd,fonction1):
	matrice_proba = np.zeros((nb_valeur_fonction(fonction1),nb_valeur_fonction(fonction1)))
	val_vraisemblance = 0
	with open(fp,encoding='utf-8') as f1:
		reader = csv.reader(f1,delimiter=';')
		for num_ligne,line in enumerate(reader):
			if num_ligne != 0:
				for num_colonne,case in enumerate(line):
					if num_colonne > 0:
						matrice_proba[num_ligne - 1,num_colonne - 1] = float(case)
	
	with open(fd,encoding='utf-8') as f2:
		reader = csv.reader(f2,delimiter=';')
		valTemp = ""
		valLum = ""
		valCo2 = ""
		valHum = ""
	    linge1 = ""
	    ligne2 = ""
		for num_ligne,line in enumerate(reader):
			#première ligne du fichier qui contient la liste des champs
        	
			if(num_ligne == 1):
				ligne1 = line

			if(num_ligne > 1):
				ligne2 = line
				if (float(matrice_proba[appelle_fonction(fonction1,ligne1[1],ligne1[2],ligne1[3],ligne1[4])][appelle_fonction(fonction1,ligne2[1],ligne2[2],ligne2[3],ligne2[4])]) != 0):
					val_vraisemblance = val_vraisemblance + math.log(float(matrice_proba[appelle_fonction(fonction1,ligne1[1],ligne1[2],ligne1[3],ligne1[4])][appelle_fonction(fonction1,ligne2[1],ligne2[2],ligne2[3],ligne2[4])])) / math.log(10)
				ligne1 = ligne2
	print(val_vraisemblance)


fichier_proba = ""
fichier_donnees = ""
fonction1 = ""
fonction2 = ""

fichier_proba = sys.argv[1]
fichier_donnees = sys.argv[2]
fonction1 = sys.argv[3]
fonction2 = sys.argv[4]

calcul_score_log_vraissemblance(fichier_proba,fichier_donnees,fonction)