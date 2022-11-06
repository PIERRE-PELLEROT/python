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
    0:pg.image.load("porte-d-entree.jpg"),
    1:pg.image.load("piscine-1.jpg"),
    2:pg.image.load("garage.jpg"),
    3:pg.image.load("vestibule.jpg"),
    4:pg.image.load("salle-a-manger.jpg"),
    5:pg.image.load("salon.jpg"),
    6:pg.image.load("chambre-parentale.jpg"),
    7:pg.image.load("chambre-enfant.jpg"),
    8:pg.image.load("cuisine.jpg"),
    9:pg.image.load("salle-de-bain.jpg"),
    10:pg.image.load("salle-de-jeu.jpg"),
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
    "quitter":False,
    "s":False,
    "e":False,
    "o":False
}


def deplacement_impossible(screen):
    font=pg.font.Font("freesansbold.ttf", 20)

    text=font.render("Déplacement impossible", 1, (255,0,0))
    pg.draw.rect(screen,(255,255,255), pg.Rect(40,300,500,40))
    pg.draw.rect(screen,(0,0,0), pg.Rect(40,300,500,40),2)
    screen.blit(text,(50, 310))








def decrire_pièce(piece_actuel,screen):
    font=pg.font.Font("freesansbold.ttf", 20)
    if piece_actuel==0:
        text=font.render("Vous êtes devant la Maison", 1, (0,0,0))
    for i in range(1,11):
        if piece_actuel==i:
            nom_piece=piece[i]
            text=font.render("Vous êtes dans " + nom_piece, 1,(0,0,0) )
    pg.draw.rect(screen,(255,255,255), pg.Rect(40,260,500,40))
    pg.draw.rect(screen,(0,0,0), pg.Rect(40,260,500,40),2)
    screen.blit(text,(50, 270))



piece_actuel=0
cle=False

running=True
deplacement=False

while running:




    touches=event.event(touches)






    """print("Ou désirez-vous aller? -------------------------------------")
    print("n : Nord")
    print("s : Sud")
    print("e : Est")
    print("o : Ouest")
    print("q : quitter")
    print("------------------------------------------------------------")
    #menu=input("votre choix ?")"""
    if touches["n"]:
        if piece_actuel==0:
            piece_actuel=3
            deplacement=False
        elif  piece_actuel==3:
            piece_actuel=7
            deplacement=False
        elif  piece_actuel==7 and cle:
            piece_actuel=10
            deplacement=False
        elif  piece_actuel==2:
            piece_actuel=6
            deplacement=False
        elif  piece_actuel==1:
            piece_actuel=4
            deplacement=False
        elif  piece_actuel==4:
            piece_actuel=8
            deplacement=False
        elif  piece_actuel==5:
            piece_actuel=9
            deplacement=False
        else:
            deplacement=True

    elif touches["s"]:
        if piece_actuel==3:
            piece_actuel=0
            deplacement=False
        elif  piece_actuel==7:
            piece_actuel=3
            deplacement=False
        elif  piece_actuel==10:
            piece_actuel=7
            deplacement=False
        elif  piece_actuel==6:
            piece_actuel=2
            deplacement=False
        elif  piece_actuel==4:
            piece_actuel=1
            deplacement=False
        elif  piece_actuel==8:
            piece_actuel=4
            deplacement=False
        elif  piece_actuel==9:
            piece_actuel=5
            deplacement=False
        else:
            deplacement=True

    elif touches["e"]:
        if piece_actuel==0:
            piece_actuel=1
            deplacement=False
        elif  piece_actuel==2:
            piece_actuel=3
            deplacement=False
        elif  piece_actuel==3:
            piece_actuel=4
            deplacement=False
        elif  piece_actuel==4:
            piece_actuel=5
            deplacement=False
        elif  piece_actuel==6:
            piece_actuel=7
            deplacement=False
        elif  piece_actuel==7:
            piece_actuel=8
            deplacement=False
        elif  piece_actuel==8:
            piece_actuel=9
            deplacement=False
        else:
            deplacement=True


    elif touches["o"]:

        if piece_actuel==1:
            piece_actuel=0
            deplacement=False
        elif  piece_actuel==3:
            piece_actuel=2
            deplacement=False
        elif  piece_actuel==4:
            piece_actuel=3
            deplacement=False
        elif  piece_actuel==5:
            piece_actuel=4
            deplacement=False
        elif  piece_actuel==7:
            piece_actuel=6
            deplacement=False
        elif  piece_actuel==8:
            piece_actuel=7
            deplacement=False
        elif  piece_actuel==9:
            piece_actuel=8
            deplacement=False
        else:
            deplacement=True


    if touches["q"] or touches["quitter"]:
        print("Au revoir")

        running=False
    screen.blit(piece_image[piece_actuel], [0,0])
    decrire_pièce(piece_actuel,screen)
    if deplacement:
        deplacement_impossible(screen)


    if piece_actuel==6:

        cle=True

        font=pg.font.Font("freesansbold.ttf", 20)

        text=font.render("Vous venez de récupérer la clé pour accéder à la salle de jeu !", 1, (255,0,0))
        pg.draw.rect(screen,(255,255,255), pg.Rect(0,0,640,40))
        pg.draw.rect(screen,(0,0,0), pg.Rect(00,0,640,40),2)
        screen.blit(text,(10, 10))

    pg.display.flip()

pg.quit()






















