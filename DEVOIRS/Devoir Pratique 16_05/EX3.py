# Créé par PIERRE.PELLEROT, le 16/05/2023 en Python 3.7

def recherche(car,chaine):
    compteur=0

    for i in range(len(chaine)):

        if chaine[i]==car:
            compteur+=1

    return compteur

print(recherche('e','sciences'))
print(recherche('a','mississippi'))
print(recherche('i','mississippi'))
