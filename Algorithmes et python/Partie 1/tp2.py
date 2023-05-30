# Créé par pierre.PELLEROT, le 15/09/2022 en Python 3.7
"""Exercice 1
for i in range(0,16):
    print(i)
"""
"""Exercice 2
for i in range(15,-1,-1):
    print(i)
"""
"""Exercice 3

a=int(input("Nombre de départ ="))
b=int(input("Nombre de fin ="))
for i in range(a-1,b+1):
    print(i)
"""
"""Exercice 4
a=int(input("Nombre de départ ="))

for i in range(a+1,a+11):
    print(i)
"""
"""Exercice 5
a=int(input("Nombre de départ ="))

for i in range(1,11):
    print(a, " * ", i," = ", a*i)
"""
"""Exercice 6
nbr=[]
for i in range(0,5):
    nbr.append(int(input("Nombres ?")))

print("Le nombre le plus grand est :", max(nbr))
"""
"""Exercice 7

a=1
nbr=[]
while a>=0:
    a=int(input("Nombres ?"))
    nbr.append(a)

print("Le nombre le plus grand est :", max(nbr))
"""
"""Exercice 8
a=1
nbr=[]
while a>=0:
    a=int(input("Nombres ?"))
    nbr.append(a)


print("La somme des nombres est :", sum(nbr)-a)
"""
"""Exercice 9
menu="0"
while menu!="q":
    menu=input()
    print("1 : charger le fichier")
    print ("2 : sauvegarder le fichier")
    print ("3 : print les données")
    print ("4 : modifier les données")
    print ("q : quitter")
    print("votre choix ?")


    if menu=="1":
        print("Chargement")
    elif menu=="2":
        print("Sauvergarde")
    elif menu=="3":
        print("Affichage")
    elif menu=="4":
        print("Modification")
    elif menu=="q":
        print("Au revoir")
    else:
        print("Erreur")
"""
"""Exercice 10
from random import *
nb_aleatoir=randint(1,20)
valeur=0

while valeur!=nb_aleatoir:
    print("Votre chiffre:")
    valeur=int(input())
    if valeur>nb_aleatoir:
        print("Trop grand")

    elif valeur<nb_aleatoir:
        print("Trop petit")


    else :
        print("exact")
"""
"""Exercice 11
from random import *
nb_aleatoir=randint(1,20)
valeur=0
coups=0
while valeur!=nb_aleatoir:
    print("Votre chiffre:")
    valeur=int(input())
    coups+=1
    if valeur>nb_aleatoir:
        print("Trop grand")

    elif valeur<nb_aleatoir:
        print("Trop petit")


    else :
        print("exact")
        print("Vous avez trouvé en ",coups," coups!")
"""
"""Exercice 12
from random import *
nb_aleatoir=randint(1,20)
valeur=0
coups=0
boucle_jeu=True

while boucle_jeu:

    nb_aleatoir=randint(1,20)
    valeur=0
    coups=0
    while valeur!=nb_aleatoir:
        print("Votre chiffre:")
        valeur=int(input())
        coups+=1
        if valeur>nb_aleatoir:
            print("Trop grand")

        elif valeur<nb_aleatoir:
            print("Trop petit")


        else :
            print("exact")
            print("Vous avez trouvé en ",coups," coups!")


    reponse=False
    while not reponse:
        print("Rejouer ?" )
        x=input("O: Oui ; N: Non")
        if x=="O" or x=="o":
            boucle_jeu=True
            reponse=True

        elif x=="N" or x=="n":
            boucle_jeu=False
            reponse=True

"""
"""Exercice 13
from math import *

x_a=int(input("Xa = "))
y_a=int(input("ya = "))
x_b=int(input("Xb = "))
y_b=int(input("yb = "))
dist=sqrt((x_a-x_b)**2+(y_a-y_b)**2)
print(dist)
"""


