# Créé par PIERRE.PELLEROT, le 06/12/2022 en Python 3.7
from string import ascii_uppercase as ascUp

vigenereTable = [ascUp[i:]+ascUp[:i] for i in range(len(ascUp))]
for ligne in range(0,len(vigenereTable)):
    print (ligne, vigenereTable[ligne])




def codage(phraseClair,cle):
     cle=cle.upper()

     decalage_cle=0
     phraseCodee=''
     for i in range(len(phraseClair)):
        num_lettre_cle=ord(cle[decalage_cle])-65


        if phraseClair[i].isalpha():
            if phraseClair[i].islower():
                car=phraseClair[i]
                num_car=ord(car)-97
                nouv_car=vigenereTable[num_lettre_cle][num_car]
                nouv_car=nouv_car.lower()


                if nouv_car.isalpha():
                    phraseCodee+=nouv_car

            elif phraseClair[i].isupper():
                car=phraseClair[i]
                num_car=ord(car)-65
                nouv_car=vigenereTable[num_lettre_cle][num_car]

                if nouv_car.isalpha():

                    phraseCodee+=nouv_car

            decalage_cle+=1
            if decalage_cle==len(cle):
                decalage_cle=0

        else:
            phraseCodee+=phraseClair[i]



     return phraseCodee

def decodage(phraseCodee,cle):
     cle=cle.upper()

     #decalage_cle=len(cle)-1
     decalage_cle=0
     phraseClair=''
     for i in range(len(phraseCodee)):
        num_lettre_cle=ord(cle[decalage_cle])-65


        if phraseCodee[i].isalpha():
            if phraseCodee[i].islower():
                car=phraseCodee[i]

                num_car_v=vigenereTable[num_lettre_cle].find(car.upper())

                nouv_car=vigenereTable[0][num_car_v]
                nouv_car=nouv_car.lower()
                if nouv_car.isalpha():
                    phraseClair+=nouv_car

            elif phraseCodee[i].isupper():
                car=phraseCodee[i]
                num_car_v=vigenereTable[num_lettre_cle].find(car)
                nouv_car=vigenereTable[0][num_car_v]

                if nouv_car.isalpha():

                    phraseClair+=nouv_car


            decalage_cle+=1
            if decalage_cle==len(cle):
                decalage_cle=0
        else:
            phraseClair+=phraseCodee[i]



     return phraseClair
cle=input("cle")
print(codage("Bonjour je m'appelle pierre",cle))
print(decodage("Qwrafyg ri d'rtempcv txmviv",cle))
