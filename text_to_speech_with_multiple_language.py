#google text to speech module
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
    
# Language in which you want to convert 
language = input(" en - for english, hi - for hindi")

while language!='en' and language!='hi':
    print("please choose english or hindi ")
    language = input(" en - for english, hi - for hindi")
    print(language)
else:
    # The text that you want to convert to audio 
    mytext = input('''Type message which you want to hear:
    like in english-How are you?
    in hindi-Tum kaise ho?''')
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 
      
    # Playing the converted file 
    os.system("welcome.mp3") 
