import datetime
#The pyttsx3 module is used here to set the output voice for your desktop assistant
import pyttsx3
#The speech recognition module is used to get any voice input from the user
import speech_recognition as sr
#Sleep function is used to stop any process for a while
from time import sleep
# Module webbrowser is used to browse any website/query or open a new tab
import webbrowser
# This os module is used to find/open any folder/application in your system
import os
# ramdom module used to give any random num
import random
# webdriver is used to open the chrome driver
from selenium import webdriver
# access file contain the function to find an path/details/urls in the respective file
import access
import sys
from chatbot import *
#for GUI
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Walter_UI import Ui_Walter
import subprocess
import pyautogui
from selenium.webdriver.common.keys import Keys
#for web scrapping
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
import pyttsx3

#for jokes
import pyjokes

def speakonly(audio):
    #only speaks, without printing
    engine = pyttsx3.init('sapi5')  # defining the engine to speak given string
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.setProperty('rate', 188)  # set the speed of voice
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecomand(self):
        #Defining function to take the voice as input and converting it to text
        take = sr.Recognizer()
        # It takes Speech as input from microphone
        with sr.Microphone() as source:
            take.adjust_for_ambient_noise(source)  # ignoring the background noise
            # seconds of non-speaking audio before a phrase is considered complete
            take.pause_threshold = 0.7
            take.energy_threshold = 300  # minimum audio energy to consider for recording
            global state        
            state = "Listening...."
            print(state)
            audio = take.listen(source)
        try:
            state = "Recognizing...."
            print(state)
            query = take.recognize_google(audio, language='en-in')
            #Performs speech recognition on "audio_data", using the Google Speech Recognition API.
            print("User said :", query)
            # global chat
            # chat.append("User said: " + query)
        except Exception as e:
            state = "Speak again..."
            print(state)
            return "None"
        return query.lower()  # returning the query in lower alphabets

# tells the temp
def GetTemperature(query):
    if "temperature in" in query:
        url = "https://www.google.com/search?q=" + query
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        temp = "The current temperature there" + " is " + temp

    else:
        url = "https://www.google.com/search?q=" + "temperature"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        temp = "The current temperature at your location is " + temp

    return temp

def GetWeather(query):
    
    chromedriver_path = access.path("chromedriver_path")
    driver = webdriver.Chrome(chromedriver_path)
    driver.minimize_window()
    driver.get("https://www.google.com/search?q=" + query)

    # identify element
    temp = driver.find_element_by_xpath('//*[@id="wob_tm"]')
    sky = driver.find_element_by_xpath('//*[@id="wob_dc"]')
    city = driver.find_element_by_xpath('//*[@id="wob_loc"]')
    ppt = driver.find_element_by_xpath('//*[@id="wob_wc"]/div[1]/div[2]/div[1]')
    humidity =  driver.find_element_by_xpath('//*[@id="wob_wc"]/div[1]/div[2]/div[2]')
    Wind =  driver.find_element_by_xpath('//*[@id="wob_wc"]/div[1]/div[2]/div[3]')

    #tells weathe in details - like ppt, wind etc
    if 'detail' in query or 'details' in query:
        # get text and print
        res = "The current temperature in "+ city.text + " is "+ temp.text + "°C," + " and the sky is " + sky.text +". " + "Some other details are. "+ ppt.text +', ' + humidity.text + ', and ' + Wind.text
        return res

    # tells overall weather only, not in details
    else:
        # get text and print
        res = "The current temperature in "+ city.text + " is "+ temp.text + "°C," + " and the sky is " + sky.text +". "
        return res
    
    driver.close()


def howto(query):
    from pywikihow import search_wikihow
    try:
        max_results = 1  # one result from web
        how_to = search_wikihow(query, max_results)
        assert len(how_to) == 1
        how_to[0].print()           # first result
        res = how_to[0].summary  # summary of 1st result

    except Exception as e:
        res = "Sorry sir, I am not able to find this"

    return res
#google search
def googlesearch(query):    
    import pywhatkit as kt
    kt.search(query) #perform search

def nearby(query):
    #remove unimportant words from query
    if "show me" in query:
        query = query.replace("show me", "")
    temp = query
    if "me" in query:
        temp = query.replace("me", " you")

    speakonly("Showing " + temp)
    googlesearch(query)     #search google for nearby
    return "Showing " + temp    #return string to print in chatbox

# Python program to convert a list to string 
def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    # return string  
    return str1 

def loc(place):
    # webbrowser.open("http://www.google.com/maps/place/" + place + "")
    geolocator = Nominatim(user_agent="Walter")
    location = geolocator.geocode(place, addressdetails=True)
    target_latlng = location.latitude, location.longitude
    location = location.raw['address']
    target_loc = {'city': location.get('city', ''),
                  'state': location.get('state', ''),
                  'country': location.get('country', '')}

    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng

    distance = str(great_circle(current_latlng, target_latlng))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance), 2)

    return current_loc, target_loc, distance

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    webbrowser.open("http://www.google.com/maps/place/" + city + "")

    return city, state, country

class log():
    def __init__(self):
        # accessing the chromedriver path from path.txt
        self.chromedriver_path = access.path("chromedriver_path")
        # accessing the sign in url from url.txt
        self.sign_in = access.url("sign_in_url")
        # Defining a driver to open chrome driver
        self.driver = webdriver.Chrome(self.chromedriver_path)
        self.driver.get(self.sign_in)  # feeding the sign in link to the driver

    def login(self):
        """
        This is a login function used to login your personal gmail account
        by accessing data directli from the files
        """
        self.user_mail, self.user_password = access.personal_details("your_name")
        #accessing the password and email details of owner
        self.enter_mail = self.driver.find_element_by_id("identifierId")
        self.enter_mail.send_keys(self.user_mail)
        #identifing the textbox using id of element and typing user mail with the help of send_keys() function
        self.enter_mail.send_keys(Keys.RETURN)
        #pressing Enter key using Keys function
        # sleep time is given so that the time is given to code whlie next page is loded
        sleep(3)
        self.enter_pass = self.driver.find_element_by_name("password")
        self.enter_pass.send_keys(self.user_password)
        #identifing the textbox using name of element and typing user password with the help of send_keys() function
        self.enter_pass.send_keys(Keys.RETURN)
        sleep(5)

class mail(log):    
    def compose(self, subject, content, reciver_mail):
        """
        In this function the email will be composed by adding 
        subject, sender mail and content to the email
        """
        self.driver.get(access.url("gmail_url"))
        self.subject = subject
        self.content = content
        self.reciver_mail = reciver_mail
        self.driver.find_element_by_css_selector(".aic .z0 div").click()
        #identifing the compose button using css_selector of element and clicking on it with the help of click() function
        sleep(3)
        self.driver.find_element_by_name("to").send_keys(self.reciver_mail)
        #identifing the textbox of to(text box where sender mail) using name of element and typing mail with the help of send_keys() function
        self.driver.find_element_by_name("subjectbox").send_keys(self.subject)
        #identifing the textbox of subject using name of element and typing subject with the help of send_keys() function
        sleep(3)
        self.driver.find_element_by_css_selector(
            ".Ar.Au div").send_keys(self.content)
        #identifing the content textbox using css_selector of element and typing content with the help of send_keys() function
        sleep(3)

    def send(self):
        # The send functions just sends the message
    	self.driver.find_element_by_css_selector(
    	    "tr.btC td:nth-of-type(1) div div:nth-of-type(2) div").click()
        #identifing the send button using css_selector of element and clicking on it with the help of click() function
    	sleep(5)
    	self.driver.close()  # closing the driver
