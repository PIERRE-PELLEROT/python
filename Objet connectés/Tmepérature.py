from neopixel import NeoPixel
from machine import Pin,I2C
from time import sleep_ms, sleep
from onewire import OneWire
from ds18x20 import DS18X20
from ssd1306 import SSD1306_I2C
np = NeoPixel(Pin(14), 4)
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)


bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()
temp_min=35
temp_max=0
def afficher_ecran(temp,temp_min,temp_max):
    oled.fill(0)
    if temp_min>=temp:
        temp_min=temp
    if temp_max<=temp:
        temp_max=temp
    oled.text("Temp amb: "+str(temp), 0, 20)
    oled.text("Temp max: "+str(temp_max), 0, 40)
    oled.text("Temp min: "+str(temp_min), 0, 0)
    
    oled.show()
    return temp_min,temp_max

def afficher_lumiere(temp):
    
    if temp<=23.0:
        
        couleur=(255,0,0)
    elif temp<=23.25:
        couleur=(200,0,50)
    elif temp<=23.5:
        couleur=(150,0,100)
    elif temp<=23.75:
        couleur=(150,0,150)
    elif temp<=24:
        couleur=(75,0,200)
    else:
        couleur=(0,0,255)
    for i in range(4):
        np[i]=couleur
    np.write()
    
    
while True:
    ds.convert_temp()       
    sleep_ms(750)
    temp_celsius = ds.read_temp(capteur_temperature[0])
    afficher_lumiere(temp_celsius)
    temp_min,temp_max=afficher_ecran(temp_celsius,temp_min,temp_max)
    print(temp_celsius)
