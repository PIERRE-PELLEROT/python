#import pygal   #question 8

coefficients=[5,5,5,5,5,5,10,10,8,10,16,16,100]
notes=[12,11,13,8,16,12,12.5,9,14,15,11,19]
matieres=["Enseignement scientifique",
            "Histoire/géographie",
            "Langue vivante A ",
            "Langue vivante B ",
            "EPS",
            "Enseignement spécialité 1ere",
            "Bulletins scolaires",
            "Français anticipé (écrit et oral)",
            "Philosophie ",
            "Grand oral de Terminale",
            "Enseignement spécialité 1",
            "Enseignement spécialité 2"]


def calculMoyenne(coefficients,notes):
    somme=0
    somme_coefficient=0
    for i in range(len(notes)):
        somme+=notes[i]*coefficients[i]
        somme_coefficient+=coefficients[i]

    return somme/somme_coefficient

def traitementBac(moyenne):
    print ("Votre moyenne est de",moyenne)
    if moyenne<8:
        print("Oups vous n'avez pas le bac !!")
    elif moyenne<10:
        print("Vous devez aller au rattrapage !")
    elif moyenne<12:
        print("Vous avez le BAC !!!")
    elif moyenne<14:
        print("Vous avez le bac avec la mention Assez Bien !")
    elif moyenne<16:
        print("Vous avez le bac avec la mention BIEN !!")
    else:
        print("Vous avez le bac avec la mention TRES BIEN")

def rechercheNoteMin(notes):
    min=notes[0]
    for i in range(1, len(notes)):
        if notes[i]<min:
            min=notes[i]
    print("La note minimale est de ", min)


def rechercheNoteMax(notes):
    max=notes[0]
    for i in range(1, len(notes)):
        if notes[i]>max:
            max=notes[i]
    print("La note maximale est de ", max)

def rechercheNote(notes,matieres,laNote):
    compteur=0
    for i in range(len(notes)):
        if notes[i]==laNote:
            compteur+=1
            print("Vous avez obtenu ",laNote, " dans la matière ",matieres[i])

    print("Vous avez obtenu ",laNote, " dans", compteur, "matière(s)")

def changeNote(notes, matieres):
    for i in range(len(matieres)):
        texte="Votre note en "+ matieres[i]
        notes[i]=int(input(texte))
        texte="Erreur !! Votre note en "+ matieres[i]
        while notes[i]>20 or notes[i]<0:
            notes[i]=int(input(texte))


def tableauBac(coefficients,notes,matieres):
    print("{0:50}{1:20}{2:20}".format("Matières","Notes", "Coefficients"))
    for i in range(len(notes)):
        print("{0:35}{1:20}{2:20}".format(matieres[i],notes[i], coefficients[i]))


changeNote(notes, matieres)
moyenne=calculMoyenne(coefficients,notes)
traitementBac(moyenne)
rechercheNoteMin(notes)
rechercheNoteMax(notes)
rechercheNote(notes,matieres,12)
tableauBac(coefficients,notes,matieres)


