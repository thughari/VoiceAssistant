import os
import pyttsx3
import datetime

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)
engine.say('''hello??
hii!! how are you
hope you are doing great''')
engine.runAndWait()

today = datetime.date.today()

a = "hari"

engine.say("Hello"+a)
engine.runAndWait()
engine.say("I am Jarvis")
engine.runAndWait()
engine.say("I am an AI Assistant and can perform a few tasks for you !")
engine.runAndWait()
engine.say("Today's Date is :")
engine.runAndWait()
engine.say(today)
engine.runAndWait()
