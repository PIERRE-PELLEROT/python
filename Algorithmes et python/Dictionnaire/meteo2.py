# Créé par pierre.PELLEROT, le 02/02/2023 en Python 3.7
import csv
fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_horaire=[]
for ligne in lecture_fichier:
    liste_horaire.append(dict(ligne))
fichier.close()

temp_moy=0
compteur=0
for heure  in liste_horaire :
    temp_moy*=compteur
    temp=((float(heure['Temp Int C'])+float(heure["Temp Ext C"]))/2)
    temp_moy+=temp
    compteur+=1
    temp_moy/=compteur

print(temp_moy)