

import openai
import os
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()
#change voice and rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

openai.api_key = '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'


def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(response.choices[0].text.strip())
    return response.choices[0].text.strip()

def get_user_input():
    return input()

def respond_to_user(response):
    engine.say(response)
    engine.runAndWait()

while True:
    user_input = get_user_input() # get user input from microphone
    if user_input:
        openai_response = get_openai_response(user_input) # generate response using OpenAI API
        respond_to_user(openai_response) # respond to user using text-to-speech
