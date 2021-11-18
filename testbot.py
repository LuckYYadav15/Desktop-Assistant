from os import close
import pyttsx3  #set the output voice for your desktop assistant
import speech_recognition as sr
from time import sleep
from selenium import webdriver
# access file contain the function to find an path/details/urls in the respective file
# import access
PATH = 'C:\Program Files (x86)\chromedriver.exe'
import sys
#GUI linking
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie #for playing gifs
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from testbotUI import Ui_desktop_ui

state = "Hello !"
chat = ["Walter: Hello Sir !"]
chatlist = "-------\n"

def speak(audio):
    # defining the speak function so that our assistant can speak any string given as input
    engine = pyttsx3.init('sapi5') #defining the engine to speak given string
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id) #seting voice of any inbuilt system voice like David/Zeera
    # print(voice)     # to know the no of voices in system
    engine.setProperty('rate', 188) #set the speed of voice 
    engine.say(audio) 
    print(audio)
    global chat
    chat.append("Walter: " + audio)
    engine.runAndWait() #Runs an event loop until all commands queued up until this method call complete

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.taskExecution()

    def takecomand(self):
        #Defining function to take the voice as input and converting it to text 
        take = sr.Recognizer()
        # It takes Speech as input from microphone
        with sr.Microphone() as source:
            take.adjust_for_ambient_noise(source) #ignoring the background noise
            take.pause_threshold = 0.6 # seconds of non-speaking audio before a phrase is considered complete
            take.energy_threshold = 200  # minimum audio energy to consider for recording
            global state
            state = "Listening..."
            print("Listning....")
            audio = take.listen(source)
        try:
            state = "Recognizing..."
            print("Recognizing...")
            query = take.recognize_google(audio, language='en-in') 
            #Performs speech recognition on "audio_data", using the Google Speech Recognition API.
            print("User said :", query)
            global chat
            chat.append("You: " + query)
        except Exception as e:
            print("Say that again please....")
            state = "Say Again please !"
            return "None"
        return query.lower() # returning the query in lower alphabets

    def taskExecution(self):
        speak("Hello sir, Welcome to Desktop Assistant. Please Give a Command")
        while(True):
            self.query = self.takecomand()
        
            if "twitter" in self.query:
                speak("Opening twitter")
                speak("Opening twitter")
                driver = webdriver.Chrome(PATH)
                driver.get("https://twitter.com/")

            elif "close" in self.query:
                speak("Closing Window")
                driver.quit()

#object for mainthread class
startExecution = MainThread()

#new class
#used for run UI of prev class
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_desktop_ui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        #to perform task - run Gif
        self.ui.movie = QtGui.QMovie("img/bgimg.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        #copy same code for other gifs (if present in UI)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime) #showtime is  a function
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        #fun to show timme
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        self.ui.textBrowser_3.setText(state)
        global chatlist
        for item in chat:
            if item not in chatlist:
                chatlist = chatlist + item + " \n"
            
        self.ui.textBrowser_4.setText(chatlist)

app = QApplication(sys.argv)
assistant = Main()
assistant.show()
exit(app.exec_())