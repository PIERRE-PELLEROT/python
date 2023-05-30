"""import network

# user data
ssid = "PIERRE" # wifi router name
pw = "08022007" # wifi router password

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

# wait for connection
while not wifi.isconnected():
    pass

# wifi connected
print(wifi.ifconfig())"""

"""import network

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)

# wifi is connected ?
if wifi.isconnected():
    print ("connecté au réseau wifi")
    print(wifi.ifconfig())    
else:
    print (" NON connecté au réseau wifi")"""

"""import network
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
oled.fill(0)
if wifi.isconnected():
    print ("connecté au réseau wifi")
    print(wifi.ifconfig())
    oled.text(str(wifi.ifconfig()[0]),0,30)
    oled.show()"""

"""import network
import ubinascii

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)

# wifi is connected ?
if wifi.isconnected():
    ip=wifi.ifconfig()
    print(ip[0])
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print(mac)
else:
    print (" NON connecté au réseau wifi")"""
"""import network
import urequests
import ujson
import utime

# user data
url = "http://worldtimeapi.org/api/timezone/Europe/Paris" 

# initialization

response = urequests.get(url)
    
if response.status_code == 200:
    worldtime = ujson.loads(response.text)
    print(type(worldtime))
    print(worldtime.keys())
    print(worldtime)
  
else:
    print("Pas de réponse")"""
from machine import Pin
import usocket as socket

led = Pin(0,Pin.OUT)


def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
"""from machine import Pin,I2C,RTC
from time import sleep
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
import network
import urequests
import ujson
import utime

rtc = RTC()

#commentaire#(year, month, day, weekday, hours, minutes, seconds, subseconds)
rtc.datetime((2023,1, 5, 4, 15,33, 30,0)) 
# user data
url = "http://worldtimeapi.org/api/timezone/Europe/Paris"

# initialization
while True:
    response = urequests.get(url)
        
    if response.status_code == 200:    
        worldtime = ujson.loads(response.text)
        print(type(worldtime))
        print(worldtime.keys())
        print(worldtime)
        horloge = worldtime["datetime"]
        weekday=worldtime["week_number"]
        print(horloge)
        annee = int(horloge[0:4]) #debut,fin à completer
        mois = int(horloge[5:7])
        jour = int(horloge[8:10])
        heure = int(horloge[11:13])
        minute = int(horloge[14:16])
        seconde = int(horloge[17:19])
        subsecond = int(horloge[20:23])
        print(annee, mois, jour, heure, minute, seconde, subsecond)
        rtc.datetime((annee, mois, jour,weekday, heure, minute, seconde, subsecond))
        horloge=rtc.datetime()
        heures=horloge[4]
        minutes=horloge[5]
        secondes=horloge[6]
        print(heures,":",minutes,":",secondes)
        oled.fill(0)
        oled.text(str(heures)+":"+str(minutes)+":"+str(secondes), 40, 30)
        oled.show()
        

    else:
        print("Pas de réponse")"""
        
        
from machine import Pin
#import usocket as socket
import socket

led = Pin(0,Pin.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 5000))
print("A l'écoute du port 5000")
while True:
    
    data, addr = s.recvfrom(1024)
    print('received:',data,'from',addr)
    if (data.decode()=='o'):
        led.on()
    elif (data.decode()=='n'):
        led.off()

    
    




