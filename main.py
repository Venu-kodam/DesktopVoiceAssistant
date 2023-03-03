import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import random
import pyjokes

engine = pyttsx3.init('sapi5')      #sapi5 is speechApi by Microsoft
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Iam siri, Please tell me how can i help you")

def takecommand():
    #it takes input from microphone and return str
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 600
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            print(results)
            speak(f"According to wikipedia {results}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = "C:\\Users\\venuk\\Documents\\music\\mymusic"  #select your music dir
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'the time' in query:   #for current time
            strTime = datetime.datetime.now().strftime("%H:%M:S")
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'open brave' in query:
            bravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravePath)

        elif 'joke' in query:  #program to say random jokes
            joke = pyjokes.get_joke(language= 'en',category= 'all')
            print(joke)
            speak(f'here is the joke {joke}')

        elif 'shutdown system' in query:  #program to shutdown system
            shutdown = speak('Do you want to shutdown?')
            os.system("shutdown /s")

        elif 'quit' in query:
            speak('Thank you for using siri')
            exit()



