from features import sense, basic
import sys, random
from features import weather
import datetime
from features.walter_chat import *

def chat_bot(query):
    if query in command_info:
        sense.speak(basic.listToString(random.choices(info)))

    elif query in command_greet:
        sense.speak(basic.listToString(random.choices(greet)))

    elif query in chat_1:
        sense.speak(basic.listToString(random.choices(chat_1_replay)))

    elif query in chat_2:
        sense.speak(basic.listToString(random.choices(chat_2_replay)))

    elif query in chat_3:
        sense.speak(basic.listToString(random.choices(chat_3_replay)))

    elif query in chat_4:
        sense.speak(basic.listToString(random.choices(chat_4_replay)))

    elif query in chat_5:
        sense.speak(basic.listToString(random.choices(chat_5_replay)))

    elif query in chat_6:
        sense.speak(basic.listToString(random.choices(chat_6_replay)))

    elif query in chat_7:
        sense.speak(basic.listToString(random.choices(chat_7_replay)))

    elif query in chat_8:
        sense.speak(basic.listToString(random.choices(chat_8_replay)))

    elif query in chat_9:
        sense.speak(basic.listToString(random.choices(chat_9_replay)))

    elif query in chat_10:
        sense.speak(basic.listToString(random.choices(chat_10_replay)))

    elif query in chat_11:
        sense.speak(basic.listToString(random.choices(chat_11_replay)))
        
    elif query in command_quit:
        sense.speak(basic.listToString(random.choices(command_quit_replay)))
        sys.exit()
    else:
        return 0

def greetAndWork(query):
    #greet and perform task simultaneously
    #eg- hello walter, what is the temperature?
    #eg- good morning walter, how is the weather?
    if 'hello' in query or 'good morning' in query:
        sense.speak("Hello sir !")  # greets user
        #replacing unnecessary key words from query
        query = query.replace("hello", "")
        query = query.replace("hi", "")
        query = query.replace("good morning", "")
        query = query.replace("walter", "")
        #correcting mispronounciations
        #sometimes it misunderstands 'Walter' as these: (due to indian accent)
        query = query.replace("water", "")
        query = query.replace("walton", "")
        query = query.replace("wallpaper", "")

    return query

def wishMe():
    #function wishme will wish the user according to the time and weather
   # declaring the hour variable to  get the current hour
    temp, sky = weather.GetTemperature("weather")
    temp = temp.replace("The current temperature at your location is ","Temperature is ")
    val = f"\n{temp} and the sky is {sky}."
    try:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            sense.speak("Hello sir, Good Morning." + val)
        elif hour >= 12 and hour < 18:
            sense.speak("Hello sir, Good Afternoon." + val)
        else:
            sense.speak("Hello sir, Good Evening." + val)
                
    except Exception as e:
        print(e)
