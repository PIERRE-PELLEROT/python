# Créé par pierre.PELLEROT, le 09/02/2023 en Python 3.7
def remplirCamion(meubles,volumeMax):
    v=0
    p=0
    n=len(meubles)
    meublesChoisis=[]
    for i in range(n):
        if meubles[i][1]+p<=volumeMax:
            p+=meubles[i][1]
            meublesChoisis.append(meubles[i][0])
    print("Volume max embarqué",p)
    return meublesChoisis


#liste des objets

meubles=[['armoire',3],['fauteuil',1.1],['lave vaisselle',1.0],['lit',0.9],['ordinateur',0.2]]
print(meubles)
volumeMax=5

print('Les meubles choisis sont')
meublesChoisis=remplirCamion(meubles,volumeMax)
print(meublesChoisis)

