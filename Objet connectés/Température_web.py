from machine import Pin
import usocket as socket
from time import sleep_ms, sleep
from onewire import OneWire
from ds18x20 import DS18X20
from ssd1306 import SSD1306_I2C

bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()

temp_celsius=0

def web_page():
  html = """<html>
            <head>
            <title>ESP neopixels Web Server</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
            <h1>Température de la pièce: """+str(temp_celsius)+""" °C
            </h1> 
            </body>
            </html>"""

  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    
    ds.convert_temp()       
    sleep_ms(750)
    temp_celsius = ds.read_temp(capteur_temperature[0])

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
