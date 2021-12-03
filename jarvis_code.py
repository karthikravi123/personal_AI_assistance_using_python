import os
import time
import subprocess
import json
import wolframalpha
import requests
import webbrowser
import datetime
import wikipedia

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
condvoice =  engine.getProperty('voice')
engine.setProperty('voice','voice[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishMe():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I AM LISTENING ...")
        audio = r.listen(source)
        
        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
            
        except Exception as e:
            speak("parden me please say again")
            return "None"
        return statement

speak('LOADING YOUR AI PERSONAL ASSISTANT JARVIS')
wishMe()


if __name__ == '__main__':
        
    while (True):
        speak("Tell me How can i help you")
        statement = takeCommand().lower()
        
        if statement == 0:
            continue
            
            
        if "Good bye" in statement or "ok bye" in statement or "stop" in statement or "Go Offline" in statement:
            speak("Your personal AI assistant Jarvis is shutdown,Good bye")
            print("Your personal AI assistant Jarvis is shutdown,Good bye")
            break

        elif 'wikipedia' in statement:
            speak("searching wikipidea ....")
            statement = statement.replace("wikipedia","")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to wikipedia ....")
            print(results)
            speak(results)
        
        elif 'date' in statement or'current date' in statement or 'today date' in statement:
            date()
            
        elif "search in chrome" in statement:
            speak("what should i search")
            chromepath = "C:\Program Files\Google\Chrome\Application\94.0.4606.71\chrome.exe.sig %s"
            search = takeCommand().lower()
            webbrowser.get(chromepath).open_new_tab
        
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open for you")
            time.sleep(5)
        
        elif "open Google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google search is open for you")
            time.sleep(5)
        
        elif "open gmail" in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("your gmail is open")
            time.sleep(5)
         
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid = "+ api_key + "&q"+city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature =  y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]['description']
                speak("the temparture in kelvin units is " + str(current_temperature) + "\n humidity in percentage is "+ str(current_humidity) +"\n weather decription" + str(weather_description))
                print("the temparture in kelvin units is " + str(current_temperature) + "\n humidity in percentage is "+ str(current_humidity) +"\n weather decription" + str(weather_description))
            
            else:
                speak("city not found")
                print("city not found")
        
        elif "time" in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is  {strTime}")
                  
        elif  "who are you" in statement  or "what can you do " in statement:
            speak("I'M  JARVIS YOUR PERSONAL AI ASSISTANT.IM PROGRAMMED TO DO FOLLPWING TASK SUCH AS OPENING GMAIL,read news,GOOGLE CHROME ,PREDICT TIME,WEATHER, open stack overflow,etc")                  

        elif "stack overflow" in statement:
            webbrowser.open_new_tab("https:///stackoverflow.com/login")
            time.sleep(5)
        
        elif "who made you" in statement:
            speak("I was built by Airobosoft")
            print("I was built by Airobosoft")
            
        elif "todays news" or "news" in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak("here are some headlines for you from times of india - Happy reading")

        elif "search" in statement:
                statement = statement.replace("search","")
                webbrowser.open_new_tab("statement")
            
        
        elif "ask" in statement:
            speak("I can answer to  computational and geographical too  just try  me!! ask me what you want")
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client("R2K75H-7ELALHR35X")
            res = client.query(question)
            answer = next(rs.results).text
            speak(answer)
            print(answer)
            
        elif "log off" in statement or "sign out" in statement or "shutdown" in statement:
            speak("ok,your PC will shutdown in 10 seconds-make sure you have saved and exited from all applications")
            subprocess.call(["shutdown","/l"])
         
time.sleep(3)
