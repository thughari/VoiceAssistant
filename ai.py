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
    engine.say(f'you said {txt}')
    engine.runAndWait()
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
        elif(i=='john' or i=='cena' or i=='johncena'):
            engine.setProperty('voice',voices[0].id)
            engine.say("AND his name is JOHN CENA, YOU can't see me")
            engine.runAndWait()
            os.system("johncena.mp3")
        elif(i=='phani' or i=='friend'):
            os.system("start chrome https://youtu.be/AE8eBai0lEk?t=6673")
        elif(i=='hi' or i=='hai' or i=='hello'):
            engine.say(" hii dude, How are you")
            engine.runAndWait()
        elif(i=='you'):
            engine.say('i am edith.............your personal assistant')
            engine.runAndWait()
        elif(i=='exit' or i=="don't" or i=='not' or i=='quit'):
            engine.say('okay i am exiting..... bye bye, have a good day')
            engine.runAndWait()
            exit()
        
        
        
        
        
        else:
            engine.say("oooooooooooh shit, i don't have that mannnnn!!!")
            engine.runAndWait()
    



except sr.UnknownValueError:
    engine.say('''you said nothing 
    or  i didn't heard you
    sooo
    i am quitting''')
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
