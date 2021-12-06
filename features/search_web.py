from pywikihow import search_wikihow
import pywhatkit
import wikipedia
from features.get import access
#---------------------For Selenium-----------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#----------------------------------------------------------------

def how_to(query):
    try:
        max_results = 1                                 # one result from web
        how_to = search_wikihow(query, max_results)
        assert len(how_to) == 1
        val = how_to[0].summary                          # summary of 1st result

    except Exception as e:
        val = "Sorry sir, I am not able to find this"

    return val

#google search
def googlesearch(query):
    query = query.replace("search", "")
    query = query.replace(" for ", "")
    query = query.replace(" about ", "")
    query = query.replace(" on ", "")
    query = query.replace("google", "")
    
    pywhatkit.search(query)  # perform search
    return "Showing search results for " + query

def nearby(query):
    #remove unimportant words from query
    query = query.replace("show", "")

    googlesearch(query)  # search google for nearby

    query = query.replace(" me", " you")
    return "Showing " + query  # return string to print in chatbox

#------------------------------------------------------------------

# fetch from wikipedia
def findWikipedia(query):
    results=wikipedia.summary(query,sentences=2) #fetch summary
    return results

# used to shorten the given paragraph
def shorterpara(para, Maxlines):
    letterindex = 0
    linescount = 0
    for letter in para:
        letterindex = letterindex+1
        #if found a full stop, => linescount++
        if letter == '.':
            linescount = linescount+1

        if linescount == Maxlines:
            return para[0:letterindex]      #return upto calculated letter index (i.e maxlines)

# To search via DuckDuckGo(search engine) API Key
def searchVia_API(query):
    #to extract required data from API
    import urllib.request
    import json

    query = query.replace(' ', '+')

    #opening URL with API key
    API_key_url = "https://api.duckduckgo.com/?q=" + query +"&format=json&pretty=1"
    json_obj = urllib.request.urlopen(API_key_url)

    #reading data
    data = json.load(json_obj)

    #data is stored in the form of dictionary, so getting them via key value
    ans = data['Abstract']

    #shortening the answer to 2 lines
    ans = shorterpara(ans, 2)
    return ans

#finding answers from API/web/wikipedia
def findAns(query):

    query = query.replace(' ', '+')
    
    # search on API----------------
    ans = searchVia_API(query)
   
   # if answer not found  => do web scrapping on google -------------
    if ans == None or len(ans) == 0:
        
        #tools for web scrapping
        chromedriver_path = access().path("chromedriver_path")

        chrome_options = Options()
        chrome_options.add_argument("--window-size=1024x768")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chromedriver_path)
        driver.minimize_window()

        driver.get('http://www.google.com/search?q=' + query)

        # Get text from Google answer box    
        ans = driver.execute_script(
            "return document.elementFromPoint(arguments[0], arguments[1]);",
            350, 230).text
        driver.close()

    # Still if correct answer is not found => try fetching from wikipedia
    if ans == None or len(ans) == 0 or 'http' in ans or len(ans)<4:
        try:
            ans = findWikipedia(query)
        #if not found, show web results in browser
        except Exception as e:
            pywhatkit.search(query)
            ans = "Sorry, I can't find that. Here are some results from google"

    return ans
#-------------------------------------------------------------