from machine import Pin
import usocket as socket

led = Pin(0,Pin.OUT)


def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html>
            
            <head>
            <title>ESP LED Web Server</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
            html {
            font-family: Helvetica;
            display:inline-block;
            margin: 0px auto;
            text-align: center;
            }
            h1{
            color: #0F3376;
            padding: 2vh;
            }
            p{
            font-size: 1.5rem;
            }

            .button1{
            display: inline-block;
            background-color: #ff00ff;
            border: none; 
            border-radius: 4px;
            color: black;
            padding: 16px 40px;
            text-decoration: none;
            font-size: 30px;
            margin: 2px;
            cursor: pointer;
            }
            .button2{
            background-color: #00ff00;
            }
            </style>

            
            </head>
            <body>
            <h1>ESP Web Server</h1> 
            <p>GPIO state: """ + gpio_state + """</p>
            <p><a href="/?led=on"><button class="button1">ON</button></a></p>
             <p><a href="/?led=off"><button class="button1 button2">OFF</button></a></p>
             </body></html>"""
    


  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crée une socket
s.bind(('', 80)) #liez le socket à une adresse et un port
s.listen(5) #ecoute le port 80

while True:
    
    connexion, adresse = s.accept() #le serveur accepte la connexion entrante sur le port 80
    
    print('Connection du client',adresse)
    requete = str(connexion.recv(1024)) #récupére la requete client
    print('Content = ',requete)
    led_on = requete.find('/?led=on')  #recherche l'indice de /?LED=ON dans  la requete client
    led_off = requete.find('/?led=off')
    print(led_on,led_off)
    #led_on=6
    if led_on ==6:              #l'indice est en position 6 alors allume la led
        print('LED ON')
        led.on()
    if led_off ==6:
        print('LED OFF')
        led.off()
    reponse = web_page()        #envoi de la page html
    connexion.send('HTTP/1.1 200 OK\n')
    connexion.send('Content-Type: text/html\n')
    connexion.send('Connection: close\n\n')
    connexion.sendall(reponse)
    connexion.close()
