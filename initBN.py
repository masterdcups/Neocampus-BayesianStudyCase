import csv
import interval as inter

def genererDataBN(fichierE,fichierS):

    #ouverture du fichier qui contiendra les données permettant d'apprendre le réseau bayésien
    fichier = open(fichierS,"w")

    #ouverture du fichier qui contient les données aggrégées
    with open(fichierE,encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=';')
        
        num_ligne = 0

        for line in reader:
            #première ligne du fichier qui contient la liste des champs
            if num_ligne == 0:
                new_line = line[1] + ";" + line[4] + ";" + line[5] + ";" + line[6] + ";" + line[7] + "\n"
                       
            else:
                if line[1] == "jour":
                    period = 1
                else:
                    period = 0
                new_line = str(period) + ";" + inter.temperature(float(line[4])) + ";" + inter.luminosite(float(line[5])) + ";" + inter.co2(float(line[6])) + ";" + inter.humidite(float(line[7])) + "\n"

            #ecriture dans le fichier de sortie    
            fichier.write(new_line)
            num_ligne += 1

    fichier.close()

genererDataBN("./dataAgregatAnnote.csv","./dataBN.csv")
