from machine import Pin
import usocket as socket

led = Pin(0,Pin.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crée une socket
s.bind(('', 23)) #liez le socket à une adresse et un port
s.listen(5) #ecoute le port 80

while True:
  connexion, adresse = s.accept() #le serveur accepte la connexion entrante sur le port 80
  print('Connection du client',adresse)
  connexion.send('connexion au serveur\n\r')
  print(connexion)
  cnx=True
  while cnx==True:
      requete = connexion.recv(1024).decode('ascii') #récupére la requete client
      print('Requete du client = ',requete)
      if requete =='a':              #l'indice est en position 6 alors allume la led
          print('LED ON')
          led.on()
          connexion.send('led allumée\n\r')
      elif requete =='e':
          print('LED OFF')
          led.off()
          connexion.send('led eteinte\n\r')
      elif requete =='q':
          print('Quit')
          led.off()            
          cnx=False
          connexion.close()