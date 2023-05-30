from machine import Pin, I2C
import usocket as socket
from neopixel import NeoPixel
from ssd1306 import SSD1306_I2C
from onewire import OneWire
from ds18x20 import DS18X20


led = Pin(0,Pin.OUT)
np = NeoPixel(Pin(14), 4)
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)



couleur_rgb=(255,255,255)
bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()

oled.fill(0)
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
                Afficher texte:
                <input type="texte" name="texte" id="couleur"/>
                <br>
                Envoi du texte sélectionnée
                <input type="submit" value="envoyer" />
            </form>
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
    texte = requete.find('/?texte')  #recherche l'indice de /?LED=ON dans  la requete client
    
    
    
    
   
   
        
    
    if texte==6:              #l'indice est en position 6 alors allume la led
        oled.fill(0)
        print("Texte reçu")
        fin_texte=requete.find('HTTP')
        phrase=requete[texte+8:fin_texte]
        for i in range(len(phrase)):
            if phrase[i]=="+":
                print(phrase)
                phrase=phrase[:i]+" "+phrase[i+1:]
                print(phrase)
            if phrase[i]=="%":
                print(phrase)
                code = int(phrase[i+1:i+3] ,16)
                
                phrase=phrase[:i]+chr(code)+phrase[i+2:]
                print(phrase)
                
        if len(phrase)<=5:
            x=40
        elif len(phrase)<=8:
            x=35
        elif len(phrase)<=12:
            x=30
        elif len(phrase)<=16:
            x=25
        elif len(phrase)<=20:
            x=20
        else:
            x=0
        oled.text(phrase, x, 30)
        oled.show()
        
        
        
        
    else:
        print("Pas de réponse")
    reponse = web_page()        #envoi de la page html
    connexion.send('HTTP/1.1 200 OK\n')
    connexion.send('Content-Type: text/html\n')
    connexion.send('Connection: close\n\n')
    connexion.sendall(reponse)
    connexion.close()
