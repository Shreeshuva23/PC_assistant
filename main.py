import pyttsx3
import wikipedia
import speech_recognition as sr
import os
import datetime
import webbrowser
import pythoncom
#import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Mr.Shreeshuva sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-np')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'google' in query:
            webbrowser.open("google.com")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")

        elif 'stack overflow' in query:
            webbrowser.open("stacksoverflow.com")

        elif 'stack overflow' in query:
            webbrowser.open("stacksoverflow.com")

        elif 'facebook' in query:
            webbrowser.open("facebook.com")


