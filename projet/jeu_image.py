# Créé par pierre.PELLEROT, le 04/10/2022 en Python 3.7
"""
    Créé par pierre.PELLEROT 1G1, le 27/09/2022 en Python 3.7
"""

import pygame as pg
import event

pg.init()
screen=pg.display.set_mode((640,360))
pg.display.set_caption("Jeu aventure")

piece_image={
    0:"devant la Maison",
    1:"le Jardin",
    2:"le Garage",
    3:"l'Entrée",
    4:"la Salle à manger",
    5:"le Salon",
    6:"la Chambre des Parents",
    7:"la Chambre des Enfants",
    8:pg.image.load("cuisine.jpg"),
    9:"la Salle de bains",
    10:"la Salle de jeux"
}
piece={
    0:"devant la Maison",
    1:"le Jardin",
    2:"le Garage",
    3:"l'Entrée",
    4:"la Salle à manger",
    5:"le Salon",
    6:"la Chambre des Parents",
    7:"la Chambre des Enfants",
    8:"la Cuisine",
    9:"la Salle de bains",
    10:"la Salle de jeux"
}






touches={                   #enregistrement des touches claviers
    "n":False,
    "q":False,
    "quitter":False
}











def decrire_pièce(piece_actuel,screen):
    font=pg.font.Font("freesansbold.ttf", 20)
    if piece_actuel==0:
        text=font.render("Vous êtes devant la Maison", 1, (0,0,0))
    for i in range(1,11):
        if piece_actuel==i:
            nom_piece=piece[i]
            text=font.render("Vous êtes dans " + nom_piece, 1,(0,0,0) )

    screen.blit(text,(310, 300))



piece_actuel=8
cle=False

running=True


while running:




    event.event(touches)




    decrire_pièce(piece_actuel,screen)
    """if piece_actuel==6:
        print("Vous venez de récupérer la clé pour accéder à la Salle de Jeux")
        cle=True
    print("Ou désirez-vous aller? -------------------------------------")
    print("n : Nord")
    print("s : Sud")
    print("e : Est")
    print("o : Ouest")
    print("q : quitter")
    print("------------------------------------------------------------")
    #menu=input("votre choix ?")
    if menu=="n" or menu=="N":
        if piece_actuel==0:
            piece_actuel=3
        elif  piece_actuel==3:
            piece_actuel=7
        elif  piece_actuel==7 and cle:
            piece_actuel=10
        elif  piece_actuel==2:
            piece_actuel=6
        elif  piece_actuel==1:
            piece_actuel=4
        elif  piece_actuel==4:
            piece_actuel=8
        elif  piece_actuel==5:
            piece_actuel=9
        else:
            print("Déplacement impossible!")

    elif menu=="s" or menu=="S":
        if piece_actuel==3:
            piece_actuel=0
        elif  piece_actuel==7:
            piece_actuel=3
        elif  piece_actuel==10:
            piece_actuel=7
        elif  piece_actuel==6:
            piece_actuel=2
        elif  piece_actuel==4:
            piece_actuel=1
        elif  piece_actuel==8:
            piece_actuel=4
        elif  piece_actuel==9:
            piece_actuel=5
        else:
            print("Déplacement impossible!")

    elif menu=="e" or menu=="E":
        if piece_actuel==0:
            piece_actuel=1
        elif  piece_actuel==2:
            piece_actuel=3
        elif  piece_actuel==3:
            piece_actuel=4
        elif  piece_actuel==4:
            piece_actuel=5
        elif  piece_actuel==6:
            piece_actuel=7
        elif  piece_actuel==7:
            piece_actuel=8
        elif  piece_actuel==8:
            piece_actuel=9
        else:
            print("Déplacement impossible!")


    elif menu=="o" or menu=="O":
        if piece_actuel==1:
            piece_actuel=0
        elif  piece_actuel==3:
            piece_actuel=2
        elif  piece_actuel==4:
            piece_actuel=3
        elif  piece_actuel==5:
            piece_actuel=4
        elif  piece_actuel==7:
            piece_actuel=6
        elif  piece_actuel==8:
            piece_actuel=7
        elif  piece_actuel==9:
            piece_actuel=8
        else:
            print("Déplacement impossible!")"""
    print(touches["q"])

    if touches["q"] or touches["quitter"]:
        print("ok")

        running=False
    screen.blit(piece_image[8], [0,0])
    pg.display.flip()

pg.quit()






















