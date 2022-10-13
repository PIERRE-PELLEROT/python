# Créé par pierre.PELLEROT, le 04/10/2022 en Python 3.7
import pygame as pg



def event(touches):

    touches={                   #maj des touches claviers comme eteintes
    "n":False,
    "q":False,
    "quitter":False,
    "s":False,
    "e":False,
    "o":False
}






    for event in pg.event.get():
        if event.type==pg.KEYDOWN:
            if event.key== pg.K_n:
                touches["n"]=True
            elif event.key== pg.K_a:
                touches["q"]=True
            elif event.key== pg.K_s:
                touches["s"]=True
            elif event.key== pg.K_e:
                touches["e"]=True
            elif event.key== pg.K_o:
                touches["o"]=True



        if event.type==pg.QUIT:
            touches["quitter"]=True


    return touches
