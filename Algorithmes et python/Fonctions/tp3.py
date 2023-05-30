# Créé par pierre.PELLEROT, le 27/09/2022 en Python 3.7
"""Exercice 1
def afficher_texte():
    print("Bonjour")

afficher_texte()
"""
"""Exercice 2

def afficher_texte(prenom):
    #prenom en chaine de caracteres
    print("Bonjour" ,prenom)

afficher_texte("Pierre")
"""
"""Exercice 3
def somme(nbA,nbB):

    return nbA+nbB

print(somme(3,5))
"""
"""Exercice 4
def calcul_surface(long ,larg):
    surface=long*larg
    return surface

print(calcul_surface(10.5,2))
"""
"""Exercice 5
def calcul_formule(x):
    y=2*x**2-4*x+3
    return y
print(calcul_formule(5))
"""
"""Exercice 6
from math import *
def conversion_angle(x):
    degre=degrees(x)
    return degre

print(conversion_angle(3*pi/2))
"""
"""Exercice 7
def table(operande, valmin=0, valmax=10):
    for i in range(valmin,valmax+1):
        print(operande,"*",i,"=", i*operande)

table(5,0,10)
"""
"""Exercice 8

def rectangle(hauteur,largeur,caractere="*"):
    for h in range(hauteur):
        for l in range(largeur):
            print(caractere, end="")

        print()

rectangle(5,10)
"""
"""Exercice 9
def triangle(hauteur):
    for h in range(hauteur):
        for l in range(h+1):
            print("*", end="")

        print()


triangle(5)
"""
"""Exercice 10
from math import pi
def volume(rayon):
    ""volume d'une sphère""
    return 4*pi*rayon**3/3

print(volume(10))
"""