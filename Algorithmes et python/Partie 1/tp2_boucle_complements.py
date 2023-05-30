# Créé par pierre.PELLEROT, le 20/09/2022 en Python 3.7
"""Execice 1
for i in range(15,4,-1):
    print(i)
"""
"""Exercice 2
a=int(input("Valeur début:"))
b=int(input("Valeur fin:"))

for i in range(a,b-1,-1):
    print(i)
"""
"""Exercice 3
a=int(input("Coefficient directeur"))
b=int(input("Ordonnée à l'origine:"))
for i in range(-10, 11):
    print("x=",i," --> y=", i*a+b)
"""
"""Exercice 4
nbr=[0]*5
for i in range(0,5):
    a=-1

    while a<0:
        nbr[i]=(int(input("Nombres ?")))
        a=nbr[i]
print("Le nombre le plus petit est :", min(nbr))
"""
"""Exercice 5
nbr=[]
a=1

while a>0:
    a=int(input("Nombres ?"))
    if a>0:
        nbr.append(a)

print("Le nombre le plus petit est :", min(nbr))
"""
"""Exercice 6
nbr=[]
a=1

while a>0:
    a=int(input("Nombres ?"))
    if a>0:
        nbr.append(a)

print("La moyenne des nombres est :", sum(nbr)/len(nbr))
"""
"""Exercice 7
for i in range(46,150,2):
    print(i)
"""
"""Exercice 8
from sympy import isprime

for i in range(1,150):
    if isprime(i):
        print(i)
"""












