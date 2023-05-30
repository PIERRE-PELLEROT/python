"""Exercice 1
def afficheTuple(tuple):
    prenom, nom, adresse, code, ville = tuple
    print(prenom)
    print(nom)
    print(adresse)
    print(code)
    print(ville)

tuple=("Georges", "Weasley", "Terrier", "999", "Magicland")
afficheTuple(tuple)"""

"""Exercice 2
def calcul(x, coefficient):
    m,p=coefficient
    y=m*x+p
    return y

coefficients=(-2,1)

print("La valeur de y pour x=2 est: y=",calcul(2,coefficients))"""

"""Exercice 3
from math import sqrt
def calcul_distance(A,B):
    xA,yA=A
    xB,yB=B
    dist=sqrt((xA-xB)**2+(yA-yB)**2)
    return dist

pointA=(1,1)
pointB=(5,4)
print(calcul_distance(pointA,pointB))
"""

"""Exercice 4
def min(liste):
    min=liste[0]
    for i in range(len(liste)):

        if min>liste[i]:
            min=liste[i]

    return min

liste=[23,151,32,45,321,5,454,314]
print(min(liste))"""

"""Exercice 5
def max(liste):
    max=liste[0]
    for i in range(len(liste)):

        if max<liste[i]:
            max=liste[i]

    return max

liste=[23,151,32,45,321,5,454,314]
print(max(liste))"""

"""Exercice 6
def somme(liste):
    somme=0
    for i in range(len(liste)):
        somme+=liste[i]

    return somme

liste=[15,351,18,13,546,15]
print(somme(liste))"""

"""Exercice 7
def moyenne(liste):
    somme=0
    for i in range(len(liste)):
        somme+=liste[i]
    moyenne=float(somme)/len(liste)
    return moyenne

liste=[15,351,18,13,546,15]
print(moyenne(liste))"""

"""Exercice 8
def somme(liste):
    somme=0
    for i in range(len(liste)):
        somme+=liste[i]

    return somme

def moyenne(liste):

    moyenne=float(somme(liste))/len(liste)
    return moyenne

liste=[15,351,18,13,546,15]
print(moyenne(liste))"""

"""Exercice 9
def somme(liste):
    somme=0
    for i in range(len(liste)):
        somme+=liste[i]

    return somme

def moyenne(liste):

    moyenne=float(somme(liste))/len(liste)
    return moyenne

def max(liste):
    max=liste[0]
    for i in range(len(liste)):

        if max<liste[i]:
            max=liste[i]

    return max

def min(liste):
    min=liste[0]
    for i in range(len(liste)):

        if min>liste[i]:
            min=liste[i]

    return min

def rechercheMinMaxMoyenne(liste):
    MinMaxMoyenne=(min(liste),max(liste),moyenne(liste))
    return MinMaxMoyenne

liste=[1231,10215135,44,5,48,56,544,4,5,45,4,5,15,156,451,564,2,54,56,46,465,4,454,51,5,465,4,45,4,64,54,548,5,46,5,4,46,57,645,486,48]
print(rechercheMinMaxMoyenne(liste))"""
