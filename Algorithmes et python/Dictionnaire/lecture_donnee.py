# Créé par pierre.PELLEROT, le 02/02/2023 en Python 3.7
import csv
fichier = open("donnees.csv", "r")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_personnes = []
for ligne in lecture_fichier:
    liste_personnes.append(dict(ligne))
fichier.close()

for personne in liste_personnes :
    print(personne)
