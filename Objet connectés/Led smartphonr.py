from umqtt.robust import MQTTClient
import network
import sys
from machine import Pin

led = Pin(0,Pin.OUT)
def cb(topic, msg):
     print((topic, msg))
     valeur=int(msg.decode("ascii"))
     if valeur==1:
         led.on()
     elif valeur==0:
         led.off()
sta_if = network.WLAN(network.STA_IF)
print(sta_if.active())
print(sta_if.ifconfig())
myMqttClient = b"Oscaritio"
URL = b"touchard.cloud.shiftr.io"
USER_ID = b'touchard'
MQTT_API_KEY = b'MFmD747BIp8YIJYI'
client = MQTTClient(client_id=myMqttClient,
     server=URL,
    user=USER_ID,
    password=MQTT_API_KEY,
    ssl=False)
client.set_callback(cb)
try:
    client.connect()
    print("connection ok");
    client.subscribe("/actionneurs/led")
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()
    
while True:
    try:
        client.check_msg()
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()
    print("exit")
