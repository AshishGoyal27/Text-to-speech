from win32com.client import Dispatch
import datetime

def speak(string):
    '''To speak the particular string '''
    speak = Dispatch('SAPI.spVoice')
    speak.speak(string)
    print(string)

speak("Hello, Ashish")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Computer Voice. Please tell me how may I help you")   

wishMe()
