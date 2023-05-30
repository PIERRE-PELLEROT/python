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
oled.fill(0)
def abscisse():
    for i in range(128):
        oled.pixel(i,60,1)
        print('ok')
def ordonnee():
    for i in range(64):
        oled.pixel(5,i,1)
def graphique(temp,temps):
    y=10+(temp-20)*6
    y=int(y)
    oled.pixel(temps+5,64-y,1)
    print(temps,y ,temp)
    
temps=0
abscisse()
ordonnee()

while True:
    ds.convert_temp()       
    sleep_ms(1000)
    temp_celsius = ds.read_temp(capteur_temperature[0])
    temps+=1
    graphique(temp_celsius,temps)
    oled.show()