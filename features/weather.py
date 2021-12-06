from features import location
from bs4 import BeautifulSoup

# Getting weather details via API of openweather.org
def GetWeather(query):
    import urllib.request
    import json
    
    # If weather for current location is asked
    if "in" not in query:
        # from features.location import my_location
        city = location.my_location()[0]            # index=0 of function my_location returns current city
    else:
        city = query.replace("in","")

    # Private API key
    API_key = "011a08b1a827b75f091695b652b119ca"
    API_data = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&APPID=" + API_key

    # #opening URL with API key
    json_obj = urllib.request.urlopen(API_data)

    #reading data
    data = json.load(json_obj)

    # Data is stored in the form of dictionary inside a list which is again inside a dictionary on API, 
    # so getting them via Key->Index->Key
    sky = data['weather'][0]['description']
    humid = data['main']['humidity']
    wind = data['wind']['speed']
    temp = data['main']['temp']
    maxtemp = data['main']['temp_max']
    mintemp = data['main']['temp_min']
    details = "The weather in " + city + ": \n" + "Sky: " + sky + ",\nTemperature: " + str(temp) + "°C, \nMinimum Temperature: " + str(mintemp) + "°C, \nMaximum Temperature: " + str(maxtemp) + "°C\n"
    otherdetails = "Some other details are: " + "Humidity: " + str(humid) + "%, and Wind: " + str(wind) + "km/h."

    return details + otherdetails

def GetTemperature(query):
    if "temperature in" in query:
        url = "https://www.google.com/search?q=" + query
        r = location.requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
        temp = "The current temperature there" + " is " + temp
        time_sky = data.find(
            'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        sky = time_sky.split('\n')[1]

    else:
        url = "https://www.google.com/search?q=" + "temperature"
        r = location.requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
        temp = "The current temperature at your location is " + temp
        time_sky = data.find(
            'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        sky = time_sky.split('\n')[1]

    return temp,sky
