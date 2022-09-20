# Créé par pierre.PELLEROT, le 13/09/2022 en Python 3.7
""" Exercice 1

a=4
carre=a**2

print(" La valeur de a=",a,"au carré est de ", carre)
"""
"""
"Exercice 2

kilometre=100
miles=kilometre/1.609

print("La distance de ", kilometre, "kilomètre(s) est de ", miles, 'miles')

"""
"""
#Exercice 3:
a=2
b=3

print("Avant échange a=",a," et b=",b)

temp=a
a=b
b=temp

print("Après échange, a=",a," b=",b)
"""
"""

#Exercice 4:
valeur_tva=20

prix_ht=40
tva=prix_ht*valeur_tva/100;
prix_ttc=prix_ht+tva;

print("Prix HT du produit: ",prix_ht," €")
print("Indice de la TVA en 2015: ",valeur_tva," %")
print("Valeur de la TVA: ",tva," €")
print("Prix TTC: ",prix_ttc," €")
"""

"""
#Exercice 5:
a=3
b=-15

if a*b<0:
    print('Le produit est négatif')
else:
    print('Le produit est positif')
"""
"""Exercice 6

age=14

if age>=6 and age<=7:
    print("Poussin")
elif age>=8 and age<=9:
    print("Pupille")
elif age>=10 and age<=11:
    print("Minime")
elif age>=12 and age<=15:
    print("Cadet")
else :
    print("Hors catégorie")
"""
"""Exercice 7

nb_valeur=10
result=0

for i in range(1,nb_valeur+1):
    result+=i

print("Somme des ", nb_valeur, " premiers nombres entiers est: ", result)

"""
"""exercice 8

for i in range(0,101):
    for j in range(0,101):
        print(i*j, end=" ")

    print()
"""




