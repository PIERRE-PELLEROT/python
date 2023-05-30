# Créé par pierre.PELLEROT, le 09/02/2023 en Python 3.7
def remplirSac(objets,poidsMax):
    p=0
    n=len(objets)
    objetsChoisis=[0]*n
    for i in range(0,n):
        if p+objets[i][1]<=poidsMax:
            objetsChoisis[i]=1
            p = p + objets[i][1]
    return objetsChoisis



"""Test 1
#liste du matériel
objets=[[2,1],[5,0.5],[1,0.2],[3,4]]
objets=list(reversed(sorted(objets)))
print(objets)
poidsMax=4.7
print('Les objets choisis sont')
print(remplirSac(objets,poidsMax))"""

objets=[[6,5.0,'ch  aussures'],[5,5.0,'habits'],[4.5,2.0,'trousse de toilette'],[4,2.0,'crêmes'],[3,8.0,'livres'],[2,2.0,'palmes tuba'],[1,0.5,'guide touristique']]
print(objets)
poidsMax=23
print('Les objets choisis sont')
poids_embarque=0

obj=remplirSac(objets,poidsMax)

for i in range(len(objets)):
    poids_embarque+=obj[i]*objets[i][1]
print("poids max embarqué", poids_embarque)
for i in range(len(objets)):
    if obj[i]>0:
        print(objets[i][2])

