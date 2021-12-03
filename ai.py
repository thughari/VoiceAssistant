import os
import random
import speech_recognition as sr
import pyttsx3
import datetime

engine=pyttsx3.init()
voices=engine.getProperty('voices')
print(voices)
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
    res=txt.lower()
    ret=res.split()
    nums=[]
    chars=[]
    for i in range(len(ret)):
        if(ret[i].isdigit()):
            nums.append(int(ret[i]))
        else:
            chars.append(ret[i])

    
    engine.say(f'you said {txt}')
    engine.runAndWait()
    
    print(f'{txt}\n{ret}\n{chars}\n{nums}')
    

    for i in chars:
        if(i=='youtube'):
            os.system('start chrome youtube.com')
        elif(i=='closer' or i=='song'):
            os.system('start chrome youtu.be/PT2_F-1esPk')
        elif(i=='chrome'):
            os.system('start chrome')
        elif(i=='brave'):
            os.system('start brave')
        elif(i=='github'):
            os.system('start github')
        elif(i=='whatsapp'):
            os.system('start chrome web.whatsapp.com')
        elif(i=='spider' or i=='peter' or i=='parker'):
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
            engine.say('i am edith.............your personal voice assistant')
            engine.runAndWait()
        elif(i=='pick' or i=='random' or i=='number'):
            try:
                rnd=random.randint(nums[-2],nums[-1])
                engine.say(f'i am picking {rnd}')
                engine.runAndWait()
                break
            except IndexError:
                engine.say('you should mention a range here to pic a random number')
                engine.runAndWait()
                break
        elif(i=='sum'):
            s=sum(nums)
            engine.say(f'the sum is {s}')
            engine.runAndWait()
        elif(i=='divide' or i=='division'):
            try:
                div=nums[-2]/nums[-1]
                engine.say(f'the division is {div}')
                engine.runAndWait()
            except ZeroDivisionError:
                engine.say("you can't devide a number with 0")
                engine.runAndWait()
        elif(i=='subtraction' or i=='subtract'):
            sub=nums[-1]-nums[-2]
            engine.say(f'the result of subtraction is {sub}')
            engine.runAndWait()
        elif(i=='difference'):
            diff=abs(nums[-1]-nums[-2])
            engine.say(f'the difference of the numbers id {diff}')
            engine.runAndWait()
        elif(i=='exit' or i=="don't" or i=='not' or i=='quit'):
            engine.say('okay i am exiting..... bye bye, have a good day')
            engine.runAndWait()
            exit()
    
        
    


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
