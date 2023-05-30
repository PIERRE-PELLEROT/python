# Créé par pierre.PELLEROT, le 02/02/2023 en Python 3.7
"""courses={
    "croissants":6,
    "pizza":2,
    "cafe (500g)":3,
    "riz (1kg)":1
}
courses["pizza"]+=1
for value, cle in courses.items():
    print(value, "->",cle)"""

def occurrences(chaine) :
   D = {}
   for caractere in chaine :
        if caractere in D.keys():
            D[caractere]+=1
        else:
            D[caractere]=1




   return D

def anagramme(chaine1, chaine2) :
    occurrenceChaine1 = occurrences(chaine1)
    occurrenceChaine2 = occurrences(chaine2)
    if ' ' in occurrenceChaine1.keys():

        del occurrenceChaine1[' ']

    if ' ' in occurrenceChaine2.keys():

        del occurrenceChaine2[' ']

    if occurrenceChaine1==occurrenceChaine2:
        return True
    else:
        return False
"""print(occurrences('le rechauffement climatique'))"""

print(anagramme('le rechauffement climatique', 'ce fuel qui tache le firmament' ))