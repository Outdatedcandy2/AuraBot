import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywintypes
from src.win10toast.win10toast import ToastNotifier
from bs4 import BeautifulSoup
import requests
import win10toast_click


toast = ToastNotifier()

 
firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>= 12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evening")

    speak("I am Project Auro , Made By Rudraksh")        


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        print("User said", query)  

    except Exception as e:
        print(e)

        print("say that again please") 

        return "None"   

    return query     

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('auro.bot.outdatedcandy92@gmail.com','YourPassHere')
    server.sendmail('auro.bot.outdatedcandy92@gmail.com', to, content)
    server.close()

def wordoftheday():
    try:
        firefox.open("https://www.merriam-webster.com/word-of-the-day")
    except:
        print('failed')    
if __name__ == "__main__":
    
    while True:
        query = takeCommand().lower()
            
        if 'search' in query:
            
            query = query.replace("search","")
            speak(f'Searching {query}')
            search = f"https://www.google.com/search?q={query}"
            firefox.open(search)
            print(query)

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            firefox.open("youtube.com")

        elif 'open google' in query:
            firefox.open("google.com")    

        elif 'open github' in query:
            firefox.open("github.com")   

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {strTime}")

        elif 'vs code' in query:
            vspath = "C:\\Users\\imbue\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)

        elif 'task manager' in query:
            taskmanager = "C:\\Windows\\system32\\Taskmgr.exe"
            os.startfile(taskmanager)
        elif 'word of the day' in query:
            url = "https://www.merriam-webster.com/word-of-the-day"
            result = requests.get(url)

            doc = BeautifulSoup(result.text, "html.parser")


            word = doc.h1
            wd = (word.string)
            meaning = doc.find('p')
            cl = str(meaning.text)
            wod = (wd.capitalize())
            speak(f"Word Of The Day Is {wod}")    
            speak(cl)

    
            toast.show_toast(wod, f"Click To Learn More About {wod}", callback_on_click=wordoftheday)   
             

        elif 'email to rudraksh' in query:
            try:
                speak("What Should I say?")
                content = takeCommand()
                to = "imbue.rudraksh2008@gmail.com"
                sendEmail(to,content)
                speak("Email Has Been Sent") 
            except Exception as e:
                print(e)
                speak("Sorry The Mail Was Not Sent. Try Again")       
            


