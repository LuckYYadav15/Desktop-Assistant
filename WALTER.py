from features import *

state = ""
chat = []
chat_prev = []

def chatWalter(query):
    global chat_prev
    chat_prev = chat.copy()
    chat.append("Walter: " + query)

def chatUser(query):
    global chat_prev
    chat_prev = chat.copy()
    chat.append("User: " + query)
    sleep(1)

def speak(audio):
    # defining the speak function so that our assistant can speak any string given as input
    engine = pyttsx3.init('sapi5')  # defining the engine to speak given string
    voice = engine.getProperty('voices')
    # seting voice of any inbuilt system voice like David/Zeera
    engine.setProperty('voice', voice[0].id)
    # print(voice[0])     # to know the no of voices in system
    engine.setProperty('rate', 188)  # set the speed of voice
    global state
    state = "Speaking..."
    engine.say(audio)
    print(audio)
    chatWalter(audio)
    # Runs an event loop until all commands queued up until this method call complete
    engine.runAndWait()

def wishMe():
    #function wishme will wish the user according to the time and weather
    # declaring the hour variable to  get the current hour
    hour = int(datetime.datetime.now().hour)
    # declaring the strTime variable to  get the current time according to mearidain
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak("Hello sir, Good Morning." )
    elif hour >= 12 and hour < 18:
        speak("Hello sir, Good Afternoon.")
    else:
        speak("Hello sir, Good Evening.")

class MainThread(QThread):
    def __init__(self) -> None:
        self.x = 1
        super(MainThread, self).__init__()

    def run(self):
        wishMe()
        self.task()
    
    def takecomand(self):
        #Defining function to take the voice as input and converting it to text
        take = sr.Recognizer()
        # It takes Speech as input from microphone
        with sr.Microphone() as source:
            take.adjust_for_ambient_noise(source)  # ignoring the background noise
            # seconds of non-speaking audio before a phrase is considered complete
            take.pause_threshold = 0.7
            take.energy_threshold = 500  # minimum audio energy to consider for recording
            global state        
            state = "Listening...."
            print(state)
            audio = take.listen(source)
        try:
            state = "Working...."
            print(state)
            query = take.recognize_google(audio, language='en-in')
            #Performs speech recognition on "audio_data", using the Google Speech Recognition API.
            print("User said :", query)
            
        except Exception as e:
            state = "Speak again..."
            print(state)
            return "None"
        chatUser(query)
        return query.lower()  # returning the query in lower alphabets

    def task(self):
        # running the while loop infinite times
        global chat
        while True:
            self.query = self.takecomand()

            #if user asks intro/greet
            if self.query in command_info:
                speak(listToString(random.choices(info)))
            
            elif self.query in command_greet:
                speak(listToString(random.choices(greet)))
            
            elif self.query in chat_1:
                speak(listToString(random.choices(chat_1_replay)))                                
            
            elif self.query in chat_2:
                speak(listToString(random.choices(chat_2_replay)))                            
            
            elif self.query in chat_3:
                speak(listToString(random.choices(chat_3_replay)))                                
            
            elif self.query in chat_4:
                speak(listToString(random.choices(chat_4_replay)))

            #greet and perform task simultaneously
            #eg- hello walter, what is the temperature?
            #eg- good morning walter, how is the weather?
            elif 'hello' in self.query or 'hi' in self.query or 'good morning' in self.query:
                wishMe()
                #replacing unnecessary key words from query
                self.query = self.query.replace("hello", "")
                self.query = self.query.replace("hi", "")
                self.query = self.query.replace("good morning", "")
                self.query = self.query.replace("walter", "")
                #correcting mispronounciations
                #sometimes it misunderstands 'Walter' as these: (due to indian accent)
                self.query = self.query.replace("water", "")
                self.query = self.query.replace("walton", "")
                self.query = self.query.replace("wallpaper", "")
            
            if 'open youtube' in self.query or 'launch youtube' in self.query:
                speak(listToString(random.choices(['Opening Youtube', 'Launching Youtube'])))
                # taking the link of youtube from the folder url.txt using access.py file
                # opening youtube in defult webbrowser 
                webbrowser.open_new_tab(access.url("youtube_url"))

            elif 'open google' in self.query:
                speak("Sir, are you looking for any website?")
                ans=self.takecomand()
                if 'yes' in ans:
                    speak("Sir, which website are you looking for?")
                    search=self.takecomand()
                    webbrowser.open_new_tab(search + ".com")
                else:
                    speak("Sir, what should i search for?")
                    search=self.takecomand()
                    webbrowser.open_new_tab(search)

            elif 'open classroom' in self.query:
                webbrowser.open_new_tab(access.url("classroom_url"))

            elif 'play music' in self.query or 'hit some music' in self.query:
                self.music_dir=access.path("music_dir_path")
                self.songs=os.listdir(self.music_dir)
                os.startfile(os.path.join(
                self.music_dir, random.choice(self.songs)))

            elif 'date' in self.query:
                self.today= datetime.date.today()
                self.d2 = self.today.strftime("%B %d, %Y")
                self.day=datetime.datetime.now().strftime("%A")
                speak("Today is " + self.day + '. ' + self.d2)

            elif 'the time' in self.query:
                self.strTime = datetime.datetime.now().strftime("%I %M %p")
                speak("Sir, The time is " + self.strTime)

            elif 'open notepad' in self.query or 'launch notepad' in self.query:
                speak(listToString(random.choices(['Opening Notpad', 'Launching Notpad'])))
                os.startfile(access.path("notepad_path"))

            elif 'open vs code' in self.query or 'launch vs code' in self.query:
                speak(listToString(random.choices(['Opening VS Code', 'Launching VS Code'])))
                self.codepath=access.path("vs_code_path")
                os.startfile(self.codepath)
                
            elif 'screenshot' in self.query or 'take a screenshot' in self.query:
                cwd = os.getcwd()
                pyautogui.screenshot(cwd + r'\Screenshots\image' + str(self.x)+'.png')
                self.x += 1

            elif 'temperature' in self.query:
                speak(GetTemperature(self.query))

            elif "weather" in self.query:
                speak(GetWeather(self.query))
                # chat.append("Walter: " + chatmsg2) #prints weather in chatbox

            elif "how to" in self.query:
                speak(howto(self.query))

            elif "search" in self.query:
                self.query = self.query.replace("search", "")
                self.query = self.query.replace(" for ", "")
                self.query = self.query.replace(" about ", "")
                self.query = self.query.replace(" on ", "")
                self.query = self.query.replace("google", "")
                speak("Showing the search results for" + self.query)
                googlesearch(self.query)
            elif "near" in self.query or 'nearby' in self.query:
                speak(nearby(self.query))
                # chat.append("Walter: "+ nearby(self.query))   #adding msg to chatbox

            elif "joke" in self.query or 'jokes' in self.query:
                speak(pyjokes.get_joke())
                self.query = self.takecomand()
                while 'one more' in self.query or 'another one' in self.query or 'once more' in self.query:
                    speak(pyjokes.get_joke())
                    self.query = self.takecomand()

            elif 'send mail' in self.query:
                try:
                    self.query=self.query.replace("send", "")
                    self.query=self.query.replace("mail", "")
                    self.query=self.query.replace("to", "")
                    self.query=self.query.replace(" ", "")
                    obj = mail()
                    obj.login()
                    speak("What subject should i add?")
                    self.subject = self.takecomand()
                    speak("Sir what should i say?")
                    self.content = self.takecomand()
                    self.to_email=access.mail_details(self.query)
                    obj.compose(self.subject,self.content,self.to_email)
                    obj.send()
                    speak("Sir, the mail is sent")
                except Exception as e:
                    speak("Sorry sir. I am not able to send right now")
            
            elif "my location" in self.query or "where am i" in self.query or "current location" in self.query:
                try:
                    ci, st, co = my_location()
                    speak(
                        f"Sir, your current location is {ci} city which is in {st} state and country {co}")

                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

            elif "where is" in self.query:
                self.query = self.query.replace("where","")
                self.query = self.query.replace("is","")
                self.query = self.query.replace("location", "")
                self.query = self.query.replace("from", "")
                self.query = self.query.replace("my", "")
                place = self.query
                current_loc, target_loc, distance = loc(place)
                city = target_loc["city"]
                state = target_loc["state"]
                country = target_loc["country"]
                sleep(1)
                try:
                    res = f"{place} is in {state} state of country {country}. It is {distance} km away from your current location"
                    speak(res)
                except:
                    res = "Sorry sir, I couldn't get the location. Please try again"
                    speak(res)

            elif self.query in command_quit:
                speak(listToString(random.choices(command_quit_replay)))
                speakonly("3")
                speakonly("2")
                speakonly("1")
                sys.exit()
    
startexecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Walter()
        self.ui.setupUi(self)
        self.ui.run_button.clicked.connect(self.starttask)
        self.ui.Terminate.clicked.connect(self.close)
        
    def showText(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate)
        self.ui.Date.setText(lable_date)
        self.ui.Time.setText(lable_time)
        self.ui.state_of_assistant.setText(state)
        for item in chat:
            global chat_prev
            if len(chat) != len(chat_prev):
                self.res = listToString(chat[len(chat) - 1])
                self.ui.Chat_box.append(self.res)
                chat_prev.append(self.res)
        
    def starttask(self):
        self.ui.movie = QtGui.QMovie("image/Walter bg.gif")
        self.ui.bg_lab.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("image/footer(line).gif")
        self.ui.footer_img.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showText)
        timer.start(1000) 
        startexecution.start()
        
    # def showquery()

app = QApplication(sys.argv)
friday = Main()
friday.show()
exit(app.exec_())
