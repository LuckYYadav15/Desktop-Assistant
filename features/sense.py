import pyttsx3
#The pyttsx3 module is used here to set the output voice for your desktop assistant
#The speech recognition module is used to get any voice input from the user
import speech_recognition as sr
from features.basic import state,chatWalter,chatUser,listToString
engine = pyttsx3.init('sapi5')  # defining the engine to speak given string
voice = engine.getProperty('voices')
# seting voice of any inbuilt system voice like David/Zeera
engine.setProperty('voice', voice[0].id)

def speak(audio):
    try:
        # print(voice[0])     # to know the no of voices in system
        global state
        state.pop()
        state.append("Speaking...")
        print(listToString(state))
        engine.say(audio)
        engine.setProperty('rate', 210)  # set the speed of voice
        print(audio)
        chatWalter(audio)
        # Runs an event loop until all commands queued up until this method call complete
        engine.runAndWait()
    except Exception as e:
        print(e)

def takecomand():
    #Defining function to take the voice as input and converting it to text
    take = sr.Recognizer()
    # It takes Speech as input from microphone
    with sr.Microphone() as source:
        # ignoring the background noise
        take.adjust_for_ambient_noise(source)
        # seconds of non-speaking audio before a phrase is considered complete
        take.pause_threshold = 0.6
        take.energy_threshold = 800  # minimum audio energy to consider for recording
        take.dynamic_energy_threshold = True  # adjusts background noise
        global state
        state.pop()
        state.append("Listening...")
        print(listToString(state))
        audio = take.listen(source)
    try:
        state.pop()
        state.append("Working...") 
        print(listToString(state))
        query = take.recognize_google(audio, language='en-in')
        #Performs speech recognition on "audio_data", using the Google Speech Recognition API.
        print("User said :", query)

    except Exception as e:
        state.pop()
        state.append("Speak again...")
        print(listToString(state))
        return "None"
    chatUser(query)
    return query.lower()  # returning the query in lower alphabets
    