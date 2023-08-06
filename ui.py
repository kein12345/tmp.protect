print("dsd")
import time
import tkinter as tk
import random
from tkinter import *

AIO_FEED_ID = ["button1","button2"]
AIO_USERNAME = "dat_luong"
AIO_KEY = "aio_HNQC59CbSW2Cup3aCWghZZHvspCv"

window = tk.Tk()
window.title("iot project")
window.attributes('-fullscreen', False)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)
Qhead = ['NH3', 'TDS', 'HD']

for i in range(0,3):
    head = tk.Label(window,text=(Qhead[0+i]),bg='#680',justify=CENTER,font="Helvetica 60 bold")
    head.place(x=100 + i * 600, y=10,width=300, height=100)

labelAMONIAValue = tk.Label(text="5.12",
                                    fg="#0000ff",
                                    justify=CENTER,
                                    font="Helvetica 60 bold")
labelAMONIAValue.place(x=0, y=200, width=screen_width / 3, height=100)


labelTDSValue = tk.Label(text="20",
                                 fg="#0000ff",
                                 justify=CENTER,
                                 # bg = "#333",
                                 font="Helvetica 60 bold")
labelTDSValue.place(x=screen_width / 3, y=200, width=screen_width / 3, height=100)


labelPHValue = tk.Label(text="7.11",
                                fg="#0000ff",
                                justify=CENTER,
                                font="Helvetica 60 bold")
labelPHValue.place(x=2 * screen_width / 3, y=200, width=screen_width / 3, height=100)



buttonON= tk.Button(text="ON",fg="#34ebb7",justify=CENTER, bg="#FFF",font="Helvetica 60 bold")
buttonON.place(x=0, y=400, width=screen_width / 3, height=100)

buttonOFF = tk.Button(text="OFF",fg="#34ebb7",justify=CENTER, bg="#FFF",font="Helvetica 60 bold")
buttonOFF.place(x=screen_width /1.5, y=400, width=screen_width / 3, height=100)




# while True:
#     window.update()
#     time.sleep(0.1)

