import pyttsx3
import datetime

#sapi5 is Speech API developed by Microsoft.
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice
print(voices)#to get no. of voice my computer have
print(voices[0].id)#name of this voice
print(voices[1].id)#name of this voice

#voice[0].id = Male voice, voice[1].id = Female voice
engine.setProperty('voice', voices[1].id)

#convert our text to speech
def speak(text):
    engine.say(text)
    
    engine.runAndWait() #Without this command, speech will not be audible to us.
    print(text)

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
