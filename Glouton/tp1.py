def renduMonnaie(somme,pieces):
    n=len(pieces)
    choisies=[0]*n
    for i in range(0,n):
        while somme>=pieces[i]:
            somme=somme-pieces[i]
            choisies[i]=choisies[i]+1
    return choisies

"""Test 1
pieces=[500,200,100,50,20,10,5,2,1]
somme=780
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))"""

"""Test 2
pieces=[4,3,1]
somme=6
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))"""
"""Test3
pieces=[10,5,2]
somme=31
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))"""

print("Les pièces choisies sont")
somme=99
pieces=[50,20,10,5,2,1]
print(renduMonnaie(somme,pieces))


