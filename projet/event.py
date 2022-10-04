# Créé par pierre.PELLEROT, le 04/10/2022 en Python 3.7
import pygame as pg



def event(touches):

    main.touches={                   #maj des touches claviers comme eteintes
    "n":False,
    "q":False,
    "quitter":False
}






    for event in pg.event.get():
        if event.type==pg.KEYDOWN:
            if event.key== pg.K_n:
                main.touches["n"]=True
            elif event.key== pg.K_q:
                main.touches["q"]=True

        if event.type==pg.QUIT:
            main.touches["quitter"]=True

