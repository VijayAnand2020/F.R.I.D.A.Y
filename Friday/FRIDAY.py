import os
import pyttsx3
import webbrowser as wb
import speech_recognition as sr
import datetime
import wikipedia
import pytube

print("Initializing Friday...")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def WishMe():
    hour = datetime.datetime.now().hour
    if(hour >=0 and hour < 12):
        print("Good Morning")
        speak("Good Morning")
    elif(hour >= 12 and hour < 18):
        print("Good Afternoon")
        speak("Good Afternoon")    
    else:
        print("Good Evening")
        speak("Good Evening")      

def takeCommand():
    cognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        cognizer.pause_threshold = 1
        audio = cognizer.listen(source)
    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = cognizer.recognize_google(audio , language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Can you say that again please...")
        query = None
    return query


def main():  
    speak("Initializing Friday...")
    WishMe()
    while True:
        query = takeCommand()
        query = query.lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            print(results)
            speak(results)

        elif 'open google' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            url = "google.com"
            speak("Opening Google...")
            wb.get(chrome_path).open(url)

        elif 'open youtube' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            url = "youtube.com"
            speak("Opening Youtube...")
            wb.get(chrome_path).open(url)

        elif 'open maps' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            url = "maps.google.com"
            speak("opening google maps...")
            wb.get(chrome_path).open(url)

        elif 'play music' in query:
            song_dir = "D:\\VIJAY\\songs"
            songs = os.listdir(song_dir)
            print(songs)
            speak("Sure  I just did")
            print("Sure  I just did")

            os.startfile(os.path.join(song_dir,songs[6]))

        elif 'open code' in query:
            code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            speak("In a moment...")
            print("In a moment...")
            os.startfile(code_path)

        elif 'open url' in query:
           chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
           speak('Sure.Will you just tell me the url?')
           print('Sure.Will you just tell me the url?')
           url = takeCommand()
           wb.get(chrome_path).open(url)

        elif 'download video' in query:


        elif 'play games' in query:
            game_path = "D:/VIJAY/Games"
            speak("sure,Opening games..")
            os.startfile(game_path)   

        elif 'san andreas' in query:
            print("Sure,opening san andreas")
            speak("Sure,opening san andreas")
            os.startfile("D:/VIJAY/Games/GTA San Andreas/GTA_SA.exe")
            os.startfile("D:/VIJAY/Games/GTA San Andreas/GTA_SA.exe")

        elif 'shattered dimensions' in query:
            print("Sure, I will get it started")
            speak("Sure, I will get it started")
            os.startfile()

        
        elif 'bye' in query:
            print('Bye,Nice to work for you')
            speak('Bye,Nice to work for you')
            break  
        

        elif None in query:
            print("Waiting for your command")
            speak("Waiting for your command")

main()
        