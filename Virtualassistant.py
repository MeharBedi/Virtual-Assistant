import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('email',to,content) #enable 3rd party authorization to the gmail account to be used
    server.close()
#at line 123 enter the recipient email address.



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
    speak("I am Jarvis,How may I help you")

def takeCommand():
    # it takes microphone input from user and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please....")
        return "None"
    return query



if __name__=="__main__":
    wishMe()

    while True:
        query = takeCommand().lower()


        # logic for executing task based query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Users//hp//AppData//Local//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("youtube.com")
            # webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.register('chrome',
                               None,
                               webbrowser.BackgroundBrowser(
                                   "C://Users//hp//AppData//Local//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("google.com")
            # webbrowser.open("google.com")
        elif 'open hackerrank' in query:
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Users//hp//AppData//Local//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("hackerrank.com")
            # webbrowser.open("hackerrank.com")
        elif 'anime' in query:
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Users//hp//AppData//Local//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("animesuge.io")

        elif 'play music' in query:
            music_dir = 'H:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open chrome' in query:
            cpath="C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)
        elif 'send email' in  query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Mail not sent!")










