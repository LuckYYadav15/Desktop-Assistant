from features import weather
from features import location
from features import get
from features import search_web
from features import open_close
from features import login
from features import basic
from features import sense
from features import chatbot
from features import date_time
#---------------------------------------------------
import threading
#---------------------------------------------------
class walter:
    def __init__(self):
        pass
    
    def open(self,query):
        query = query.replace("open", "")
        query = query.replace("launch", "")
        query = query.replace("my", "")
        query = query.replace("account", "")
        query = query.replace("application", "")
        query = query.replace(" ", "")
        if query in list(open_close.dict_app.keys()):
            open_close.open_app(query)
            sense.speak("Opened " + query)
        else:
            open_close.open_website(query)
            sense.speak("Opened " + query)

    def close(self,query):
        query = query.replace("close", "")
        query = query.replace("exit", "")
        query = query.replace("terminate", "")
        query = query.replace(" ", "")
        if query in list(open_close.dict_app.keys()):
            open_close.close_app(query)
            sense.speak("Closed ")
        else:
            open_close.close_website()
            sense.speak("Closed ")

    def battery_status(self):
        try:    
            val = str(basic.battery())
            val = str("Battery remaining is: " + val + "%")
        except Exception as e:
            val = "Sorry sir, I can't get it right now."         
        return val

    def weather(self,query):
        query = query.replace('weather','')
        query = query.replace('how is','')
        query = query.replace('what is','')
        query = query.replace('the','')
        query = query.replace('tell','')
        query = query.replace('me','')
        
        query = query.replace('details','')
        query = query.replace(' ','')
        try:
            val = weather.GetWeather(query)
        except Exception as e:
            val = "Sorry sir, I can't get it right now."
        return val
    
    def temperature(self, query):
        try:
            val,sky = weather.GetTemperature(query)
        except Exception as e:
            val = "Sorry sir, I can't get it right now."

        return val

    def howto(self,query):
        try:
            val = search_web.how_to(query)
        except Exception as e:
            val = "Sorry sir, I can't get it right now."

        return val
       
    def web_search(self,query):
        try:
            val = search_web.googlesearch(query)
        except Exception as e:
            val = "Sorry sir, I can't get it right now."
        return val

    def near(self, query):
        try:
            val = search_web.nearby(query)
        except Exception as e:
            val = "Sorry sir, I can't get it right now."

        return val
    
    def location(self, query):
        target_loc, distance, place = location.loc(query)
        return target_loc, distance,place

    def my_location(self):
        city, state, country = location.my_location()
        return city, state, country
    
    def send_mail(self,query):
        query = query.replace("send", "")
        query = query.replace("mail", "")
        query = query.replace("to", "")
        query = query.replace(" ", "")
        obj = login.mail()
        obj.login()
        obj.compose(get.access().mail_details(query))
        obj.send()

    def join_meet(self,query):
        obj = login.meet()
        if 'new meet' in query or 'create a meet' in query:
            obj.login()
            obj.creat_meet()
        else:
            a = obj.check_class()
            if a == 0:
                obj.close()
            else:
                obj.login()
                obj.join_link()
                if a == 1:
                    obj.join()
        
    def set_alarm(self,timing):
        timing = timing.replace("set alarm to ", "")
        timing = timing.replace(".", "")
        timing = timing.upper()
        sense.speak("Alarm is set for "+timing)
        t1 = threading.Thread(target=basic.alarm, args=(timing,))
        t1.start()

    def chatwalter(self,query):
        try:
            val = chatbot.chat_bot(query)
        except Exception as e:
            pass
        return val
            
    def wishuser(self):
        try:
            chatbot.wishMe()
        except Exception as e:
            pass
    
    def efficient(self, query):
        try:
            val = chatbot.greetAndWork(query)
        except Exception as e:
            pass
        return val
    
    def date(self):
        try:
            return date_time.date()
        except Exception as e:
            pass

    def day(self):
        try:
            return date_time.day()
        except Exception as e:
            pass

    def time(self):
        try:
            return date_time.time()
        except Exception as e:
            pass