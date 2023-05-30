# Créé par pierre.PELLEROT, le 02/02/2023 en Python 3.7
import csv
from pylab import *

def listePourUneCle(liste_dico, cle):
    resultat=[]
    for i in range(len(liste_dico)):
        resultat.append(float(liste_dico[i][cle]))
    return resultat


fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')
liste_enregistrements = []
for ligne in lecture_fichier:
    liste_enregistrements.append(dict(ligne))
fichier.close()

liste_altitude = listePourUneCle(liste_enregistrements,'Altitude m')
liste_temp_ext= listePourUneCle(liste_enregistrements,'Temp Ext C')
liste_pression=listePourUneCle(liste_enregistrements,'Pression mb')
plot(liste_altitude,liste_pression)
show()
