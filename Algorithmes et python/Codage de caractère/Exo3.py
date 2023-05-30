# Créé par PIERRE.PELLEROT, le 09/03/2023 en Python 3.7
import os

fichier=open("texte.txt","r")
chaine=fichier.read()
print(chaine)
fichier.close()