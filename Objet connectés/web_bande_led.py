from machine import Pin
import usocket as socket
from neopixel import NeoPixel
from onewire import OneWire
from ds18x20 import DS18X20
from ssd1306 import SSD1306_I2C
led = Pin(0,Pin.OUT)
np = NeoPixel(Pin(14), 4)



couleur_rgb=(255,255,255)
bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()
def web_page():
  

  html="""<html>
            <head>
            <title>ESP neopixels Web Server</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
            <h1>ESP neopixels Web Server</h1> 
            <form>
                Choisir une couleur pour le ruban de leds:
                <input type="color" name="texte" id="couleur"/>
                <br>
                Envoi de la couleur sélectionnée
                <input type="submit" value="envoyer" />
            </form>
            <p><a href="/led_on"><button>ON</button></a><a href="/led_off"><button>OFF</button></a></p>
            </body>

            </html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crée une socket
s.bind(('', 80)) #liez le socket à une adresse et un port
s.listen(5) #ecoute le port 80

while True:
    
    connexion, adresse = s.accept() #le serveur accepte la connexion entrante sur le port 80
    
    print('Connection du client',adresse)
    requete = str(connexion.recv(1024)) #récupére la requete client
    print('Content = ',requete)
    couleur = requete.find('/?couleur')  #recherche l'indice de /?LED=ON dans  la requete client
    led_off = requete.find('/led_off')
    led_on = requete.find('/led_on')
    
    couleur_hexa=(requete[19:21],requete[21:23],requete[23:25])
    
   
    if led_off==6:
        for i in range(4):
            np[i]=(0,0,0)
        np.write()
    if led_on==6:
        for i in range(4):
            np[i]=couleur_rgb
        np.write()
        
    
    if couleur ==6:              #l'indice est en position 6 alors allume la led
        print("Couleur reçu")
        couleur_rgb=(int(couleur_hexa[0],16),int(couleur_hexa[1],16),int(couleur_hexa[2],16))
        for i in range(4):
            np[i]=couleur_rgb
        np.write()
    else:
        print("Pas de réponse")
    reponse = web_page()        #envoi de la page html
    connexion.send('HTTP/1.1 200 OK\n')
    connexion.send('Content-Type: text/html\n')
    connexion.send('Connection: close\n\n')
    connexion.sendall(reponse)
    connexion.close()
