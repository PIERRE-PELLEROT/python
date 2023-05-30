from neopixel import NeoPixel
from machine import Pin, ADC
from time import sleep_ms, sleep

np = NeoPixel(Pin(14), 4)


adc = ADC(0)
valeur=adc.read()
   
def defilement():
    changement_couleur=0
    for x in range(256):
        changement_couleur+=1
        couleur=(255,0+changement_couleur,0)
        for i in range(4):
            np[i]=couleur
        np.write()
            
    changement_couleur=0
    for x in range(256,512):
        changement_couleur+=1
        couleur=(255-changement_couleur,255,0)
        for i in range(4):
            np[i]=couleur
        np.write()
    changement_couleur=0
    for x in range(512,768):
        changement_couleur+=1
        couleur=(0,255,0+changement_couleur)
        for i in range(4):
            np[i]=couleur
        np.write()
    changement_couleur=0
    for x in range(768,1024):
        changement_couleur+=1
        couleur=(0,255-changement_couleur,255)
        for i in range(4):
            np[i]=couleur
        np.write()
    changement_couleur=0
    for x in range(1024,1280):
        changement_couleur+=1
        couleur=(0+changement_couleur,0,255)
        for i in range(4):
            np[i]=couleur
        np.write()
    changement_couleur=0
    
    
    
while True:
    valeur=adc.read()
    sleep(1)
    print(valeur)
    if valeur<=400:
        defilement()
    else:
        for i in range(4):
            np[i]=(0,0,0)
        np.write()

                
                