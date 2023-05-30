# Créé par pierre.PELLEROT, le 02/02/2023 en Python 3.7
import csv
fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_donnee=[]
for ligne in lecture_fichier:
    liste_donnee.append(dict(ligne))
fichier.close()

liste_enregistrements=[]
for i in range(len(liste_donnee)):
    donne=liste_donnee[i]
    liste_enregistrements.append(float(donne["Temp Ext C"]))


horaire_tmp_min = ''
tmp_min = 100.
for enregistrement in range(len(liste_enregistrements)):

    if liste_enregistrements[enregistrement]<tmp_min :
        tmp_min = liste_enregistrements[enregistrement]
        horaire_tmp_min = liste_donnee[enregistrement]['Horaire']
print(horaire_tmp_min,tmp_min)
