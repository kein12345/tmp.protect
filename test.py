import random
import time
from Adafruit_IO import MQTTClient
import sys
from ui import*

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)
def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed :  " + feed_id)




AIO_FEED_ID = ["button1","button2"]
AIO_USERNAME = "dat_luong"
AIO_KEY = "aio_HNQC59CbSW2Cup3aCWghZZHvspCv"
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background() ##?
counter = 10 #state machine
counter_ai=5
previous_ai = ""
ai_result = ""
time.sleep(1)
counter_sensor1= 5
counter_sensor2= 5
counter_sensor3= 5
def randomValue(type):
    value = 0
    if type == 0:
        value = round(random.randint(20, 80)/30, 2)
    elif type == 1:
        value = round(random.randint(1, 1500), 0)
    else:
        value = round(random.randint(100, 1400) / 100, 2)
    return value

counter_sensor = 10
sensor_type = 0

def button_1():
    print("turn on")
    client.publish("button2", "1")

def button_2():
    print("turn off")
    client.publish("button2", "0")

buttonON.config(command=button_1)
buttonOFF.config(command=button_2)

while True:

    counter_sensor = counter_sensor - 1
    if counter_sensor <= 0:
        counter_sensor = 10
        if sensor_type == 0:
            labelAMONIAValue.config(text=str(randomValue(0)))
            sensor_type = 1
        elif sensor_type == 1:
            labelTDSValue["text"] = str(randomValue(1))
            sensor_type = 2
        else:
            labelPHValue.config(text=str(randomValue(2)))
            sensor_type = 0
    window.update()
    time.sleep(0.1)







