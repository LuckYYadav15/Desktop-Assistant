import datetime

def time():
    # declaring the strTime variable to  get the current time according to mearidain
    return datetime.datetime.now().strftime("%I %M %p")
     
def date():
    today =  datetime.date.today()
    return today.strftime("%B %d, %Y")
    
def day():
    return datetime.datetime.now().strftime("%A")
