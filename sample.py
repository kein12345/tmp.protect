import time
import serial.tools.list_ports


try:
    ser = serial.Serial(port="COM6",baudrate=9600)
    print("success")
except:
    print("cant not open port")

def sendcommand(cmd):
    ser.write(cmd.encode())


# while True:           #nếu k loại n ra thì ra nút thì tự chạy
#     sendcommand("0");
#     time.sleep(5)
#     sendcommand("1");
#     time.sleep(5)
#     sendcommand("2");
#     time.sleep(5)
#     sendcommand("3");
#     time.sleep(5)

mess = ""
def processData(data, splitdata=None):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(data)
    print(splitData)
    if splitData[1] == "T":   #tempurature  #<<=  []:vi tri do
        client.publish("sensor1",splitdata[2])
    elif splitData[1] == "H":  #wet
        client.publish("sensor2",splitdata[2])



def readSerial(a, b):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1],a = "value1", b="value2")
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

# while True:           #de cai nay thi lap vo tan
#     readSerial(client)
#     time.sleep(1)
