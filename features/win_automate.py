import keyboard
from features.sense import speak
#--------------------- Automating Windows -----------------
def WindowAutomate(query):
    #for closing the tab
    if 'close this tab' in query:
        keyboard.press_and_release('ctrl + w')
        speak('Closed.')
        return 1
        
    #to open new tab
    elif 'open new tab' in query:
        keyboard.press_and_release('ctrl + t')
        speak('Opened a new tab.')
        return 1
        
    #to open new window
    elif 'open new window' in query:
        keyboard.press_and_release('ctrl + n')
        speak('Opened a new window.')
        return 1
        
    #to open history
    elif 'browsing history' in query:
        keyboard.press_and_release('ctrl + h')
        speak('Opened browsing history.')
        return 1
        
    #to open downloads
    elif 'open download' in query:
        keyboard.press_and_release('ctrl + j')
        speak('Opened')
        return 1
        
    #to open next page
    elif 'next page' in query or 'go next' in query:
        keyboard.press_and_release('Alt + Right arrow')
        speak('Moved to next page.')
        return 1
        
    #to open prev page
    elif 'previous page' in query or 'go back' in query:
        keyboard.press_and_release('Alt + Left arrow')
        speak('Moved back to previous page.')
        return 1
        
    elif 'show desktop' in query or 'maximize all' in query or 'minimise all' in query:
        keyboard.press_and_release('Windows + d')
        speak("Done sir!")
        return 1

    #minimize window
    elif 'minimise' in query:
        keyboard.press_and_release('Alt + space + n')
        speak('Minimized window')
        return 1

    elif "open file" in query:
        keyboard.press_and_release("Windows + e")
        speak("Opened Files Explorer.")
        return 1

    elif 'close window' in query:
        keyboard.press_and_release('Alt + f4')
        speak("Closed.")
        return 1

    elif 'show notification' in query or 'open notification' in query or 'close notification' in query:
        keyboard.press_and_release('Windows + a')
        speak('Done Sir!')
        return 1

    elif 'stop the video' in query:
        keyboard.press_and_release("Space")
        return 1

    #type with voice
    elif query == 'type my command':
        from features.sense import takecomand
        note = None
        speak("What should i write? ")
        while note != 'stop writing':
            note = takecomand()
            keyboard.write(note + '.', delay=0.1)
        return 1

    else:
        return 0