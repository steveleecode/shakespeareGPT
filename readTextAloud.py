# import the module
import pyttsx3 

# initialise the pyttsx3 engine 
engine = pyttsx3.init() 
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)


file_path = 'more.txt'

with open(file_path, 'r') as file:
    file_content = file.read()


# convert text to speech 
engine.say(file_content) 
engine.runAndWait() 