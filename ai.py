import os
import speech_recognition as sr
import pyttsx3
import datetime

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)
r=sr.Recognizer()
try:
    with sr.Microphone() as source:
        engine.say('speak anything')
        engine.runAndWait()
        audio=r.listen(source)
    engine.say(audio)
    txt=r.recognize_google(audio)
    print(txt)

    ret=txt.lower()
    print(ret)
    text=(ret.split())

    print(text)
    for i in text:
        if(i=='youtube'):
            os.system('start chrome youtube.com')
        elif(i=='closer'):
            os.system('start chrome youtu.be/PT2_F-1esPk')
        elif(i=='chrome'):
            os.system('start chrome')
        elif(i=='brave'):
            os.system('start brave')
        elif(i=='github'):
            os.system('start github')
        elif(i=='whatsapp'):
            os.system('start whatsapp')
        elif(i=='spider' or i=='peter'):
            os.system(r'C:\Users\harib\Downloads\spidy.jpg')
        elif(i=='john'):
            engine.setProperty('voice',voices[0].id)
            engine.say("AND his name is JOHN CENA, YOU can't see me")
            engine.runAndWait()
            os.system("johncena.mp3")
    



except:
    engine.say("you said nothing or i didn't heard you")
    engine.runAndWait()





    









exit()
os.system('start github')
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
