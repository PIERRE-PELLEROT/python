# Créé par pierre.PELLEROT, le 02/02/2023 en Python 3.7
"""def renduMonnaie(somme,pieces):
    choisies={}
    for i in range(len(pieces)):
        choisies[pieces[i]]=0

    for i in range(len(pieces)):
        while pieces[i]<=somme:
            somme-=pieces[i]
            choisies[pieces[i]]+=1

    return choisies

pieces=[500,200,100,50,20,10,5,2,1]
somme=780
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))"""


    def renduMonnaie(somme,pieces):
       choisies = {}
       for i in range(len(pieces)):
            choisies[pieces[i]]=0
       for p in pieces:
            nb= somme//p
            choisies[p]=nb
            somme-=nb*p



       return choisies
    pieces=[500,200,100,50,20,10,5,2,1]
    somme=780
    print('Les pièces choisies sont')
    print(renduMonnaie(somme,pieces))

