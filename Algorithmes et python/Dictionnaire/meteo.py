# Créé par pierre.PELLEROT, le 02/02/2023 en Python 3.7
import csv
fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_horaire=[]
for ligne in lecture_fichier:
    liste_horaire.append(dict(ligne))
fichier.close()

for heure  in liste_horaire :
    print(heure['Durée'], heure["Altitude m"])