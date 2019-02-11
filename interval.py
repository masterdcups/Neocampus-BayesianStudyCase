def temperature(valeur):
    if(valeur < 23.2 and valeur > 20.8):
        return "[20.8;23.2]"
    elif(valeur < 24.5 and valeur >= 23.2):
        return "[23.2;24.5]"
    elif(valeur > 19.5 and valeur <= 20.8):
        return "[19.5;20.8]"
    elif(valeur < 26 and valeur >= 24.5):
        return "[24.5;26]"
    elif(valeur > 18 and valeur <= 19.5):
        return "[18;19.5]"
    elif(valeur < 27 and valeur >= 26):
        return "[26;27]"
    elif( valeur > 17 and valeur <= 18):
        return "[17;18]"
    elif(valeur < 28 and valeur >= 27):
        return "[27;28]"
    elif(valeur > 16 and valeur <= 17):
        return "[16;17]"
    elif(valeur < 16):
        return "[<16]"
    elif(valeur > 28):
        return "[>28]"

def luminosite(valeur):
	if(valeur > 1100 and valeur <= 1300):
    	return "[1100;1300]"
    elif(valeur > 1000 and valeur <= 1100):
    	return "[1000;1100]"
    elif(valeur > 950 and valeur <= 1000)
    	return "[950;1000]"
    elif(valeur > 900 and valeur <= 950):
    	return "[900;950]"
    elif(valeur > 600 and valeur <= 900):
        return "[600;900]"
    elif(valeur > 550 and valeur <= 600):
        return "[550;600]"
    elif(valeur > 500 and valeur <= 550):
        return "[500;550]"
    elif(valeur > 400 and valeur <= 500):
        return "[400;500]"
    elif(valeur > 200 and valeur <= 400):
        return "[200;400]"
    else:
        return 0

def co2(valeur):
	if(valeur > 0 and valeur <= 400):
        return "[0;400]"
    elif(valeur > 400 and valeur <= 600):
        return "[400;600]"
    elif(valeur > 600 and valeur <= 800):
        return "[600;800]"
    elif(valeur > 800 and valeur <= 1000):
        return "[800;1000]"
    elif(valeur > 1000 and valeur <= 1200):
        return "[1000;1200]"
    else:
        return 0

def humidite(valeur):
	if(valeur > 70 and valeur <= 80):
		return "[70;80]"
	elif(valeur > 63 and valeur <= 70):
		return "[63;70]"
	elif(valeur > 58 and valeur <= 63):
		return "[58;63]"
	elif(valeur > 55 and valeur <= 58):
		return "[55;58]"
    elif(valeur > 45 and valeur <= 55):
        return "[45;55]"
    elif(valeur > 42 and valeur <= 45):
        return "[42;45]"
    elif(valeur > 37 and valeur <= 42):
        return "[37;42]"
    elif(valeur > 30 and valeur <= 37):
        return "[30;37]"
    elif(valeur > 20 and valeur <= 30):
        return "[20;30]"
    else:
        return 0

# -*- coding: utf-8 -*-
"""
Annotation des données selon un seuil défini par les spécifications du Google doc suivant :
https://docs.google.com/document/d/1vtwxloreLhoaFz1Pv8dX8Ovy9aDcBi80iWPXRxZvmLY/edit

"""

# Annotation d'une situation globale pour un capteur, en regroupant les valeurs trouvées durant des périodes de deux minutes, pour les différentes mesures.
def annotationCapteur(valeurTemperature, valeurLuminosite, valeurCo2, valeurHumidite):
    annotationRetour = 0
    # Définition de poids, selon l'importance d'un critère pour l'humain
    # Poids définis ici après un vote entre les membres du groupe
    poidsTemperature = 0.3
    poidsLuminosite = 0.2
    poidsCo2 = 0.4
    poidsHumidite = 0.1
    annotationRetour += poidsTemperature * temperature(valeurTemperature)
    annotationRetour += poidsLuminosite * luminosite(valeurLuminosite)
    annotationRetour += poidsCo2 * co2(valeurCo2)
    annotationRetour += poidsHumidite * humidite(valeurHumidite)

    return str(annotationRetour);
