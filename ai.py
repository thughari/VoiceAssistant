import os
import random
import speech_recognition as sr
import pyttsx3
import datetime



engine=pyttsx3.init()
#change voice and rate
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)
r=sr.Recognizer()
#recognize with microphone
try:
    with sr.Microphone() as source:
        engine.say('i am listening now...speak anything')
        engine.runAndWait()
        print('i am listening now')
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

    #say what i said
    engine.say(f'you said {txt}')
    engine.runAndWait()

    #print what i said

    print(f'{txt}\n{ret}\n{chars}\n{nums}')
    
#need to add more conditions..........and switch case too
#find windows commands to open everything

    if('youtube' in chars):
        os.system('start chrome youtube.com')
    elif(i=='closer' or i=='song'):
        os.system('start chrome youtu.be/PT2_F-1esPk')
    elif('chrome' in chars):
        os.system('start chrome')
    elif('brave' in chars):
        os.system('start brave')
    elif('github' in chars):
        os.system('start github')
    elif('whatsapp' in chars):
        os.system('start chrome web.whatsapp.com')
    elif('spider' in chars or 'peter' in chars or 'parker' in chars or 'spiderman' in chars):
        os.system(r'C:\Users\harib\Downloads\spidy.jpg')
    elif('john' in chars or 'cena' in chars or 'johncena' in chars):
        engine.setProperty('voice',voices[0].id)
        engine.say("AND his name is JOHN CENA, YOU can't see me")
        engine.runAndWait()
        os.system(r"C:\Users\harib\Downloads\john.mp4")
    elif('phani' in chars or 'friend' in chars):
        os.system("start chrome https://youtu.be/AE8eBai0lEk?t=6673")
    elif('hi' in chars or 'hai' in chars or 'hello' in chars):
        engine.say(" hii dude, How are you")
        engine.runAndWait()
    elif('who' and 'are' and 'you' in chars):
        engine.say('i am edith.............your personal voice assistant')
        engine.runAndWait()
    elif('pick' in chars or 'random' in chars or 'number' in chars):
        try:
            rnd=random.randint(nums[-2],nums[-1])
            engine.say(f'i am picking {rnd}')
            engine.runAndWait()
        except IndexError:
            engine.say('you should mention a range here to pic a random number')
            engine.runAndWait()
    
    #need to work more on the complex math

    elif('sum' in chars or 'addition' in chars or 'add' in chars):
        s=sum(nums)
        engine.say(f'the sum is {s}')
        engine.runAndWait()
        print(s)
    elif('divide' in chars or 'division' in chars):
        try:
            div=nums[-2]/nums[-1]
            engine.say(f'the division is {div}')
            engine.runAndWait()
        except ZeroDivisionError:
            engine.say("you can't devide a number with 0")
            engine.runAndWait()
    elif('subtraction' in chars or 'subtract' in chars):
        sub=nums[-1]-nums[-2]
        engine.say(f'the result of subtraction is {sub}')
        engine.runAndWait()
    elif('difference' in chars):
        diff=abs(nums[-1]-nums[-2])
        engine.say(f'the difference of the numbers id {diff}')
        engine.runAndWait()
    elif('time' and 'date' in chars): #tells both date and time
        today=datetime.datetime.today()
        date=today.date()
        time=today.time()
        print(today,date,time)
        engine.say(f"today's date is {date} and time is {time.hour-12 if time.hour>12 else time.hour} hours {time.minute} minutes {'PM' if time.hour>12 else 'AM'}")
        engine.runAndWait()
    elif('today' in chars or 'date' in chars):
        today = datetime.date.today()
        engine.say(f"today's date is {today}")
        engine.runAndWait()
    elif('time' in chars):
        time=datetime.datetime.now()
        engine.say(f"the time is {time.hour-12 if time.hour>12 else time.hour} hours {time.minute}minutes {'PM' if time.hour>12 else 'AM'}")
        engine.runAndWait()
        engine.runAndWait()
    elif('mail' in chars or 'gmail' in chars):
        os.system('start chrome mail.google.com')
    elif('song' in chars):
        os.system('start chrome https://youtu.be/PT2_F-1esPk')
    elif('matlab' in chars):
        os.system('start matlab')
    
    elif('exit' in chars or "don't" in chars or 'not' in chars or 'quit' in chars):
        engine.say('okay i am exiting..... bye byee!!, have a good day!!!')
        engine.runAndWait()
        exit()



    else:
        engine.say("i don't have that feature right now!!")
        engine.runAndWait()
    
    
        
except sr.RequestError:
    print('you are not connected to network')
    engine.say('you are not connected to the nertwork')
    engine.runAndWait()


except sr.UnknownValueError:
    print('didnot heard')
    engine.say('''you said nothing 
    or  i didn't heard you
    sooo
    i am quitting''')
    engine.runAndWait()





    









"""
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
"""