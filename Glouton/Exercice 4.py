# Créé par pierre.PELLEROT, le 09/02/2023 en Python 3.7
def journee(activites,dureeMax):
    d=0
    n=len(activites)
    activitesChoisies=[]
    for i in range(len(activites)):
        if activites[i][0]+d<=dureeMax:
            activitesChoisies.append(activites[i][1])
            d+=activites[i][0]

    print("nb heures activités", d)
    return activitesChoisies


#liste des objets
activites=[[1,"faire la vaisselle"],[2,"passer l'aspirateur"],[3,"terminer le tp NSI"],[4,"vernir l'escalier"]]
print(activites)
dureeMax=6
print('Les activités choisies sont')
activitesChoisies=journee(activites,dureeMax)
print(activitesChoisies)
