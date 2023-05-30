# Créé par PIERRE.PELLEROT, le 06/12/2022 en Python 3.7


def codage(phraseClair,cle):
     phraseCodee=''
     for i in range(len(phraseClair)):
        if phraseClair[i].isalpha():
            num_car=ord(phraseClair[i])
            num_nouv_car=num_car
            for j in range(1,cle+1):

                num_nouv_car+=1
                nouv_car=chr(num_nouv_car)
                if not nouv_car.isalpha():
                    num_nouv_car-=26
            print(num_car, num_nouv_car)
            nouv_car=chr(num_nouv_car)


            if nouv_car.isalpha():

                phraseCodee+=nouv_car




        else:
            phraseCodee+=phraseClair[i]

     return phraseCodee

def decodage(phraseClair,cle):
     phraseCodee=''
     for i in range(len(phraseClair)):
        if phraseClair[i].isalpha():
            num_car=ord(phraseClair[i])
            num_nouv_car=num_car
            for j in range(1,cle+1,):

                num_nouv_car-=1
                nouv_car=chr(num_nouv_car)
                if not nouv_car.isalpha():
                    num_nouv_car+=26
            print(num_car, num_nouv_car)
            nouv_car=chr(num_nouv_car)


            if nouv_car.isalpha():

                phraseCodee+=nouv_car




        else:
            phraseCodee+=phraseClair[i]

     return phraseCodee



cle=3
menu=''
while menu!='q':
     print("------------------------------------------------------------")
     print("1 : Codage d'une phrase")
     print("2 : Décodage d'une phrase")
     print("3 : Changement de la clé")
     print("q : quitter")
     print("------------------------------------------------------------")
     menu=input("votre choix ?")

     if menu=="1":
        phrase=input("Phrase ?")
        print(codage(phrase,cle))

     if menu=="3":
        cle=int(input("nouvelle clé ?"))

     if menu=="2":
        phrase=input("Phrase ?")
        print(decodage(phrase,cle))








