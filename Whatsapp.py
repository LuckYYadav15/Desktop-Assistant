from contextlib import nullcontext
from os import startfile
from re import S
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
import array as ar
whatsapp_path = "C:\\Users\\Utkarsh Yadav\\AppData\\Local\\WhatsApp\\WhatsApp.exe"

def openWhatsapp():
    startfile(whatsapp_path)

def minimizeWhatsapp():
    click(x=1765, y=9)

def closeWhatsapp():
    startfile(whatsapp_path)
    sleep(1)
    click(x=1862, y=21)

def WhatsappMessage(name,message):
     
    startfile(whatsapp_path)
    # test.py used
    sleep(2)
    #search button
    click(x=500, y=170)
    sleep(2)
    #writes name
    write(name)

    sleep(1)
    #selects the search result
    click(x = 500, y = 340)

    sleep(1)
    write(message)

    sleep(0.2)
    click(x=1853, y=1028)
    
    sleep(0.1)
    click(x=1738, y=7)



def WhatsappCall(name):
    startfile(whatsapp_path)
    # test.py used
    sleep(1)
    click(x=500, y=170)

    sleep(0.5)
    write(name)

    sleep(1)
    click(x = 500, y = 340)
    click(x = 60, y = 170)
    click(x=1679, y=80)

    #to end the call
    sleep(5)
    click(x=1854, y=110)

    # to minimize whatsapp
    click(x=1765, y=9)


def WhatsappVideo(name):
    startfile(whatsapp_path)
    # test.py used
    sleep(1)
    click(x=500, y=170)

    sleep(0.5)
    write(name)

    sleep(1)
    click(x = 500, y = 340)
    click(x = 60, y = 170)
    click(x=1616, y=94)
    click(x=38, y=153)

    #to end the call
    sleep(5)
    click(x=1750, y=427)
    

    # to minimize whatsapp
    click(x=1765, y=9)

#WhatsappVideo('mom')

def WhatsappGroup(members, grpname):
    startfile(whatsapp_path)
    # test.py used
    sleep(1)
    #group create
    click(x=627, y=83)
    sleep(0.1)
    #search
    click(x=540, y=164) 
    #u = 50
    indexlist = [355, 400, 450, 500, 550, 600, 650, 700, 750, 800]
    for i in range(len(members)):
        write(members[i])
        sleep(0.5)
        #add member
        click(x=160, y=indexlist[i])
    click(x=328, y=986)
    sleep(0.2)
    write(grpname)
    sleep(0.5)
    #enter button
    click(x=338, y=841)
    sleep(0.2)
    #minimize whatsapp
    click(x=1750, y=12)
#list = ['keshav', 'brij']
#hatsappGroup(list, "Walter Group")


def WhatsappOpenChat(name):
    startfile(whatsapp_path)
    # test.py used
    sleep(1)
    click(x=500, y=170)

    write(name)

    sleep(1)
    click(x = 500, y = 340)
    click(x = 60, y = 170)
#WhatsappOpenChat('mom')