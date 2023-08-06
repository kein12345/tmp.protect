import sys
import time
import random
from image_detect import *  # * dùng để cho import tất cả
from Adafruit_IO import MQTTClient
import time
from physical import *

AIO_FEED_ID = ["button1","button2"]
AIO_USERNAME = "dat_luong"
AIO_KEY = "aio_HNQC59CbSW2Cup3aCWghZZHvspCv"

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
    if feed_id == "button1":
        if payload == "1":
            sendcommand("0")
        else:
            sendcommand("1")
    if feed_id == "button2":              #import sample vô
        if payload == "1":
            sendcommand("2")
        else:
            sendcommand("3")




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
# while True:  #chú ý đừng để lặp k ngừng vì nó sẽ block (ddio)
#     print("starting....counter",counter)
#     counter =counter - 1
#     counter_ai = counter_ai - 1
#     if counter_ai <=5:
#         counter_ai = 5
#         previous_ai = ai_result
#         ai_result = get_detection()  ##??
#         if previous_ai != ai_result:       #cái này dùng để gửi ít lại
#             client.publish("ai",ai_result)
#         client.publish("ai", ai_result)
#     if counter <= 0:
#         counter = 10
#         client.publish("sensor1",random.randint(-15,100)) #hàm publish() dùng để gửi dữ liệu
#     if counter == 4:
#         client.publish("sensor2", random.randint(0, 5000))
#     if counter == 8:
#         client.publish("sensor3", random.randint(0, 100))
#     time.sleep(5)    #sleep dùng để ngắt quảng
while True:
    counter_sensor1 -= 1
    if counter_sensor1 <= 0:
        counter_sensor1 = 10
        # client.publish("sensor2",readTemperature())
        # lebel...["text"] = str(randomValue(2))
    counter_sensor2 -= 1
    if counter_sensor2 <= 0:
        counter_sensor2 = 10

    counter_sensor3 -= 1
    if counter_sensor3 <= 0:
        counter_sensor3 = 10
        # client.publish("sensor3",readMoisture())









