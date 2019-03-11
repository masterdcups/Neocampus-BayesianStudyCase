# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:11:35 2019

@author: Elmander46
"""

def temperature(valeur):
    if(valeur == "[20.8-23.2]"):
        return 5
    elif(valeur == "[23.2-24.5]"):
        return 6
    elif(valeur == "[19.5-20.8]"):
        return 4
    elif(valeur == "[24.5-26]"):
        return 7
    elif(valeur == "[18-19.5]"):
        return 3
    elif(valeur == "[26-27]"):
        return 8
    elif( valeur == "[17-18]"):
        return 2
    elif(valeur == "[27-28]"):
        return 9
    elif(valeur == "[16-17]"):
        return 1
    elif(valeur == "[<16]"):
        return 0
    elif(valeur == "[>28]"):
        return 10

def luminosite(valeur):
    if(valeur == "[1100-1300]"):
        return 9
    elif(valeur == "[1000-1100]"):
        return 8
    elif(valeur == "[950-1000]"):
        return 7
    elif(valeur == "[900-950]"):
        return 6
    elif(valeur == "[600-900]"):
        return 5
    elif(valeur == "[550-600]"):
        return 4
    elif(valeur == "[500-550]"):
        return 3
    elif(valeur == "[400-500]"):
        return 2
    elif(valeur == "[200-400]"):
        return 1
    elif(valeur == "[>1300]"):
        return 10
    elif(valeur == "[<200]"):
        return 0

def co2(valeur):
    if(valeur == "[0-400]"):
        return 0
    elif(valeur == "[400-600]"):
        return 1
    elif(valeur == "[600-800]"):
        return 2
    elif(valeur == "[800-1000]"):
        return 3
    elif(valeur == "[1000-1200]"):
        return 4
    else:
        return 5

def humidite(valeur):
    if(valeur == "[70-80]"):
        return 9
    elif(valeur == "[63-70]"):
        return 8
    elif(valeur == "[58-63]"):
        return 7
    elif(valeur == "[55-58]"):
        return 6
    elif(valeur == "[45-55]"):
        return 5
    elif(valeur == "[42-45]"):
        return 4
    elif(valeur == "[37-42]"):
        return 3
    elif(valeur == "[30-37]"):
        return 2
    elif(valeur == "[20-30]"):
        return 1
    elif(valeur == "[<20]"):
        return 0
    else:
        return 10
