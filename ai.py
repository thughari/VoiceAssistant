from os import system
from random import randint
import speech_recognition as sr
import pyttsx3
import datetime





def recognise():
    with sr.Microphone() as source:
        audio=r.listen(source)
    txt=r.recognize_google(audio)
    st=txt.lower()
    ret=st.split()
    for i in ret:
        if('/' in i):
            ret.append('/')
            ret.extend(i.split('/'))
            ret.remove(i)
    nums=[]
    chars=[]
    for i in range(len(ret)):
        if(ret[i].isdigit()):
            nums.append(int(ret[i]))
        else:
            chars.append(ret[i])
    return [ret,st,chars,nums]



engine=pyttsx3.init()
#change voice and rate
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)
r=sr.Recognizer()
def say(a):
    engine.say(a)
    engine.runAndWait()
#recognize with microphone
try:
    say('talk something when i finish saying this')
    ret,txt,chars,nums=recognise()

    #say what i said
    say(f'you said {txt}')

    #print what i said

    print(f'{txt}\n{ret}\n{chars}\n{nums}')
    
#need to add more conditions..........and switch case too
#find windows commands to open everything

    if('youtube' in chars):
        system('start chrome youtube.com')
    elif('closer' in chars or 'song' in chars):
        system('start chrome youtu.be/PT2_F-1esPk')
    elif('chrome' in chars or 'browser' in chars):
        system('start chrome')
    elif('brave' in chars):
        system('start brave')
    elif('github' in chars):
        system('start github')
    elif('whatsapp' in chars):
        system('start chrome web.whatsapp.com')
    elif(('all' in chars and 'peter' in chars) or ('all' in chars and 'spider-man' in chars)):
        system(r'peters.jpg')
    elif('spider' in chars or 'spiderman' in chars or 'spider-man' in chars):
        system(r'tasm2.mp4')
    elif('peter' in chars or 'parker' in chars):
        system(r'peter.mp4')
    elif('john' in chars or 'cena' in chars or 'johncena' in chars):
        engine.setProperty('voice',voices[0].id)
        engine.say("AND his name is JOHN CENA, YOU can't see me")
        engine.runAndWait()
        system(r"C:\Users\harib\Downloads\john.mp4")
    elif('phani' in chars or 'friend' in chars):
        system("start chrome https://youtu.be/dDWCCHbb3zs?t=362")
    elif('hi' in chars or 'hai' in chars or 'hello' in chars):
        engine.say(" hii dude, what's your name?")
        engine.runAndWait()
        ch=recognise()[-2]
        if 'i' in ch:
            ch.remove('i')
        if 'am' in ch:
            ch.remove('am')
        if 'my' in ch:
            ch.remove('my')
        if 'name' in ch:
            ch.remove('name')
        if 'is' in ch:
            ch.remove('is')
        name=' '.join(ch)
        say(f'hiii   {name}, how are you doing?')
        print(f'hii {name} how are you doing?')
    elif('birthday' in chars):
        if('me' in chars):
            say("what do you mean by me, I don't know your name, tell me your name")
            ch=recognise()[-2]
            if 'i' in ch:
                ch.remove('i')
            if 'am' in ch:
                ch.remove('am')
            if 'my' in ch:
                ch.remove('my')
            if 'name' in ch:
                ch.remove('name')
            if 'is' in ch:
                ch.remove('is')
            name=' '.join(ch)
        else:
            if 'happy' in chars:
                chars.remove('happy')
                chars.remove('birthday')
            if 'to' in chars:
                chars.remove('to')
            if 'you' in chars:
                chars.remove('you')
            if 'say' in chars:
                chars.remove('say')
            name=' '.join(chars)
        
        say(f'wish you a many more happy returns of the day {name}')
        
    elif(('who' in chars and 'are' in chars and 'you' in chars)or('what' in chars and 'can' in chars and 'you' in chars and 'do' in chars)):
        engine.say('i am edith.............your personal voice assistant...i can do some daily tasks for you')
        engine.runAndWait()
    elif('pick' in chars or 'random' in chars or 'number' in chars):
        try:
            rnd=randint(nums[-2],nums[-1])
            engine.say(f'i am picking {rnd}')
            engine.runAndWait()
        except IndexError:
            engine.say('you should mention a range here to pick a random number')
            engine.runAndWait()
    
    #need to work more on the complex math

    elif('sum' in chars or 'addition' in chars or 'add' in chars or '+' in chars):
        s=sum(nums)
        engine.say(f'the sum is {s}')
        engine.runAndWait()
        print(s)
    elif('divide' in chars or 'division' in chars or '/' in chars or 'divided' in chars):
        try:
            div=nums[-2]/nums[-1]
            say(f'the division is {div}')

        except ZeroDivisionError:
            say("it's infinite")

        except IndexError:
            say('at leas two numbers required to perform division')

    elif('subtraction' in chars or 'subtract' in chars or '-' in chars):
        sub=nums[-2]-nums[-1]
        engine.say(f'the result of subtraction is {sub}')
        engine.runAndWait()
    elif('difference' in chars):
        try:
            diff=abs(nums[-1]-nums[-2])
            engine.say(f'the difference of the numbers is {diff}')
            engine.runAndWait()
        except IndexError:
            say('two numbers required to find difference')
    elif('time'in chars and 'date' in chars): #tells both date and time
        today=datetime.datetime.today()
        date=today.date()
        time=today.time()
        print(today,date,time)
        engine.say(f"today's date is {date} and time is {time.hour-12 if time.hour>12 else time.hour} hours {time.minute} minutes {'PM' if time.hour>12 else 'AM'}")
        engine.runAndWait()
    elif('today' in chars or 'date' in chars or 'day' in chars):
        today = datetime.date.today()
        engine.say(f"today's date is {today}")
        engine.runAndWait()
    elif('time' in chars):
        time=datetime.datetime.now()
        engine.say(f"the time is {time.hour-12 if time.hour>12 else time.hour} hours {time.minute}minutes {'PM' if time.hour>12 else 'AM'}")
        engine.runAndWait()
        engine.runAndWait()
    elif('mail' in chars or 'gmail' in chars):
        system('start chrome mail.google.com')
    elif('song' in chars):
        system('start chrome https://youtu.be/PT2_F-1esPk')
    elif('matlab' in chars):
        system('start matlab')
    elif('shut' and 'down' in chars or 'shutdown' in chars):
        ###############################################################################################
        try:

            if(('in' and 'seconds' in chars)or('in' and 'second' in chars)):
                if('a' in chars):
                    t=1
                else:
                    t=nums[-1]
                say(f'shutting down your computer in {t} seconds..')
                st='shutdown /s /t '+str(t)
                system(st)
                exit()
            elif(('in' and 'minutes' in chars)or('in' and 'minute' in chars)):
                if('a' in chars):
                    t=1*60
                else:
                    t=nums[-1]*60
                say(f'shutting down your computer in {t} seconds..')
                st='shutdown /s /t '+str(t)
                system(st)
                exit()
            say('are you sure you want to shut down your system?')
            ch=recognise()[-2]
            if('yes' in ch or 'y' in ch or 'ok' in ch or 'why' in ch):
                system('shutdown /s /t 1')
            else:
                say("okay, i won't shutdown")
        except IndexError:
            say('you have to say some, time here')
    elif('restart' in chars or 'repair' in chars or 'reboot' in chars):
        ################################################################################################
        try:

            if(('in' and 'seconds' in chars)or('in' and 'second' in chars)):
                if('a' in chars):
                    t=1
                else:
                    t=nums[-1]
                say(f'restarting your computer in {t} seconds..')
                st='shutdown /r /t '+str(t)
                system(st)
                exit()
            elif(('in' in chars and 'minutes' in chars)or('in' in chars and 'minute' in chars)):
                if('a' in chars):
                    t=1*60
                else:
                    t=nums[-1]*60
                say(f'restarting your computer in {t} seconds..')
                st='shutdown /r /t '+str(t)
                system(st)
                exit()
            say('are you sure you want to restart your system?')
            ch=recognise()[-2]
            if('yes' in ch or 'y' in ch or 'ok' in ch or 'why' in ch):
                system('shutdown /r /t 1')
            else:
                say("okay, i won't restart")
        except IndexError:
            say('you have to say some, time here')

    #going to add google search

    elif('what'in chars or 'play' in chars):
        ######################################################error here focus here########################
        txt=txt.replace(' ','+')
        print(txt)
        system(f'start chrome https://www.google.com/search?q={txt}')
    elif('translate' in chars):
        a=chars.index('translate')
        if(chars[a+1]=='this'):
            chars.remove('translate')
            chars.remove('this')
        else:
            chars.remove('translate')
        se='%20'.join(chars)
        print(se)
        c='https://translate.google.co.in/?sl=auto&tl=te&text='+se+'%0A&op=translate'
        system(f'start chrome "{c}"')



    elif('exit' in chars or "don't" in chars or 'not' in chars or 'quit' in chars):
        engine.say('okay i am exiting..... bye byee!!, have a good day!!!')
        engine.runAndWait()
        exit()



    else:
        txt=txt.replace(' ','+')
        txt='start chrome https://www.google.com/search?q='+txt
        print(txt)
        system(txt)
        say("Here are the results from web")
    
        
except sr.RequestError:
    print('you are not connected to Network')
    engine.say('you are not connected to the nertwork')
    engine.runAndWait()


except sr.UnknownValueError:
    print('didnot heard')
    engine.say("you said nothing or  i didn't heard you so i am quitting")
    engine.runAndWait()
