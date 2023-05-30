"""from machine import Pin
from time import sleep_ms


led = Pin(0,Pin.OUT)

while(True):
    led.on()
    sleep_ms(100)
    led.off()
    sleep_ms(100)
"""
"""from machine import ADC
from time import sleep

adc = ADC(0)

while True:
    valeur=adc.read()
    print(valeur)
    sleep(1)
"""
"""from machine import ADC,Pin
from time import sleep

adc = ADC(0)
led = Pin(0,Pin.OUT)

while(True):
    valeur=adc.read()
    if valeur>=472.5:
        led.on()
    else:
        led.off()"""

"""
from neopixel import NeoPixel
from machine import Pin

np = NeoPixel(Pin(14), 4)


np[0] = (255, 0, 0)
np[1] = (0, 255, 0) 
np[2] = (0, 0, 255)
np[3] = (255, 255, 0)

np.write()"""

"""from neopixel import NeoPixel
from machine import Pin

np = NeoPixel(Pin(14), 4)

for i in range(4):
    np[i] = (0, 0, 0)


np.write()"""

"""NBPIXELS=4

from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

np = NeoPixel(Pin(14), NBPIXELS)


def defilement(color):
    for i in range(4):
        np[i]=color
        np.write()
        sleep_ms(750)
        np[i]=(0,0,0)


while(True):
    defilement((0,255,0))"""
"""NBPIXELS=4

from neopixel import NeoPixel
from machine import Pin,ADC
from time import sleep_ms

np = NeoPixel(Pin(14), NBPIXELS)
adc = ADC(0)

LUMIERE_MIN = 300

while True:
    valeur=adc.read()//4
    for i in range(4):
        np[i]=(0,0,valeur)
    np.write()"""
"""from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))

oled = SSD1306_I2C(128, 64, i2c, 0x3c)
oled.fill(0)
oled.text("Bonzour", 40, 30)
oled.show()"""
"""
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from time import sleep_ms
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)

y=True
while True:
    hauteur=0
    while hauteur<57:
        oled.fill(0)
        oled.text("Bonzour", 40, hauteur)
        oled.show()
        hauteur+=1
        sleep_ms(1)
    while hauteur>0:
        oled.fill(0)
        oled.text("Bonzour", 40, hauteur)
        oled.show()
        hauteur-=1
        sleep_ms(1)"""
"""
from onewire import OneWire
from ds18x20 import DS18X20
from machine import Pin
from time import sleep_ms
import sys

bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()
    
while True:
    try:
        ds.convert_temp()       
        sleep_ms(750)
        temp_celsius = ds.read_temp(capteur_temperature[0])
        print("Température : ",temp_celsius )        
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        sys.exit()



"""
"""
from onewire import OneWire
from ds18x20 import DS18X20
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from time import sleep_ms
import sys


i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()
    
while True:
    
        ds.convert_temp()       
        sleep_ms(750)
        temp_celsius = ds.read_temp(capteur_temperature[0])
        
        oled.fill(0)
        oled.text(str(temp_celsius), 40, 30)
        oled.show()"""
from machine import Pin,I2C,RTC
from time import sleep
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)

rtc = RTC()

#commentaire#(year, month, day, weekday, hours, minutes, seconds, subseconds)
rtc.datetime((2023,1, 5, 4, 15,33, 30,0)) 

while True:
    horloge=rtc.datetime()
    heures=horloge[4]
    minutes=horloge[5]
    secondes=horloge[6]
    print(heures,":",minutes,":",secondes)
    oled.fill(0)
    oled.text(str(heures)+":"+str(minutes)+":"+str(secondes), 40, 30)
    oled.show()
    sleep(1)

    
        

