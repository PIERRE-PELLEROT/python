# Créé par pierre.PELLEROT, le 10/11/2022 en Python 3.7
"""Exercice 1
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    for i in range(1,nbDroites+1):
        draw.line((ecart*i, 0, ecart*i, hauteur), fill=(0,255,0))



traceDroite(10,20)

img.show()"""

"""Exercice 2
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)

def tracecible():
    cercle(largeur/2,hauteur/2,80,(0,0,255))
    cercle(largeur/2,hauteur/2,55,(255,0,0))
    cercle(largeur/2,hauteur/2,30,(255,255,0))


tracecible()
img.show()"""

"""Exercice 3
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(255,255,255))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def rectangle(x,y,largeur,hauteur,couleur):
    draw.rectangle((x,y,x+largeur, y+hauteur),fill=couleur)

def traceEffetVisuel():
    x=0
    y=0
    for i in range(13):
        for j in range(13):
            print(y)
            rectangle(x,y,10,10,(0,0,0))
            x+=20
        y+=20
        x=0


traceEffetVisuel()
img.show()
img.save("effet.png")"""

"""Exercice 4


from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size

for x in range(hauteur):
    for y in range(largeur):
         img.putpixel((x,y),(0,255-x,0))

img.show()
img.save("degrade_vert.jpg")"""


"""Exercice 5
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size

for x in range(hauteur):
    for y in range(largeur):
         img.putpixel((x,y),(255-x,0+y,255-x))

img.show()
img.save("degrade_bicolor.jpg")"""

"""Exercice 6

from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(1536,256),(0,0,0))
largeur,hauteur=img.size

changement_couleur=0
for x in range(256):
    changement_couleur+=1
    couleur=(255,0+changement_couleur,0)
    for y in range(hauteur):

        img.putpixel((x,y),couleur)
changement_couleur=0
for x in range(256,512):
    changement_couleur+=1
    couleur=(255-changement_couleur,255,0)
    for y in range(hauteur):

        img.putpixel((x,y),couleur)
changement_couleur=0
for x in range(512,768):
    changement_couleur+=1
    couleur=(0,255,0+changement_couleur)
    for y in range(hauteur):


        img.putpixel((x,y),couleur)
changement_couleur=0
for x in range(768,1024):
    changement_couleur+=1
    couleur=(0,255-changement_couleur,255)
    for y in range(hauteur):


        img.putpixel((x,y),couleur)
changement_couleur=0
for x in range(1024,1280):
    changement_couleur+=1
    couleur=(0+changement_couleur,0,255)
    for y in range(hauteur):


        img.putpixel((x,y),couleur)
changement_couleur=0
for x in range(1280,largeur):
    changement_couleur+=1
    couleur=(255,0,255-changement_couleur)
    for y in range(hauteur):


        img.putpixel((x,y),couleur)









img.show()
img.save("degradex6.jpg")"""

"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(512,512),(0,0,0))
largeur,hauteur=img.size

title=[]
for n in range(0,12):
    print('{:02d}.png'.format(n))
    title.append(Image.open('{:02d}.png'.format(n)))


map=[[1,5,5,5,5,5,5,5,10,5,5,5,5,5,2],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [6,0,0,0,0,0,0,0,6,0,0,0,0,0,6],
     [3,5,5,5,5,5,5,5,8,5,5,5,5,5,4]]

for ligne in range(0,15):
    for colonne in range(0,15):
        print("col",ligne)
        numero=map[ligne][colonne]
        print(map[ligne][colonne],end=' ')
        img.paste(title[numero], (colonne*32,ligne*32))
    print()


img.show()
img.save("map.png")"""





