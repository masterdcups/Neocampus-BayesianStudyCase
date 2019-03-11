# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:43:44 2019

@author: Elmander46
"""
import numpy as np
import passageStringEntierPourMatrice as conv
import csv

def creerTables(fichierE):
    #ouverture du fichier qui contient les données
    nbLignes=0
    matriceHumidite = np.zeros((11,11))
    matriceLuminosite = np.zeros((11,11))
    matriceCo2 = np.zeros((6,6))
    matriceTemperature = np.zeros((121,11))
    
    with open(fichierE,encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=';')
        valTemp = ""
        valLum = ""
        valCo2 = ""
        valHum = ""
        for line in reader:
            #première ligne du fichier qui contient la liste des champs
            if(nbLignes > 1):
                matriceHumidite[conv.humidite(valHum)][conv.humidite(line[4])] += 1.0
                matriceLuminosite[conv.luminosite(valLum)][conv.luminosite(line[2])] += 1.0
                matriceCo2[conv.co2(valCo2)][conv.co2(line[3])] += 1.0
                matriceTemperature[conv.temperature(valTemp)*11 + conv.luminosite(valLum)][conv.temperature(line[1])] += 1.0
            valTemp = line[1]
            valLum = line[2]
            valCo2 = line[3]
            valHum = line[4]   
            nbLignes += 1
    matriceHumidite = np.round(np.divide(matriceHumidite,nbLignes),decimals=3)
    matriceLuminosite = np.round(np.divide(matriceLuminosite,nbLignes),decimals=3)
    matriceCo2 = np.round(np.divide(matriceCo2,nbLignes),decimals=3)
    matriceTemperature = np.round(np.divide(matriceTemperature,nbLignes),decimals=3)
    print(matriceTemperature)
    

creerTables("./dataBNDynamique.csv")
