import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import cv2
import random
from requests import get
import pywhatkit as kit
import pyjokes
import smtplib
import shutil
from urllib.request import urlopen
import json
import subprocess
import requests
# from clint import progress
import sys
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice[1].id)
engine.setProperty('voice',voice[1].id)


#test to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#to convert voice into test
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


#to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("assistant 2 point o")
    speak("I am your Assistant. how can i help you")
    speak(assname)

def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


    
while True:

    query = takeCommand().lower()

    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open command prompt' in query:
        os.system("start cmd")

    elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

    elif 'open facebook' in query:
            speak("Here you go to facebook\n")
            webbrowser.open("facebook.com")


    # elif 'play music' in query or "play song" in query:
    #     speak("Here you go with music")
    #     music_dir = "Music"
    #     songs = os.listdir(music_dir)
    #     print(songs)
    #     rd = random.choice(songs)
    #     random = os.startfile(os.path.join(music_dir, rd))
    
    elif 'open google' in query:
        speak("Here you go to google\n")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        speak("Here you go to stackoverflow\n")
        webbrowser.open("stackoverflow.com") 

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")  

    elif 'ip address' in query:
       ip = get("http://api.ipify.org").text
       speak(f"your ip address is {ip}")

    elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")  

    elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")            
    
    elif "send message" in query:
         kit.sendwhatmsg("+917999936509","this is testing protocal",23,47)

    elif "who made you" in query or "who created you" in query:
            speak("I have been created by Raju Shah.")

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif "who are you" in query:
        speak("I am your virtual assistant created by Raju Shah")
 
    elif 'what is the reason for making' in query:
        speak(" to inhance more knowledge in python ")

    elif "play song on youtube" in query:
        kit.playonyt("see you again") 


    elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))    

    elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

    elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

    # elif "weather" in query:

    #         # Google Open weather website
    #         # to get API of Open weather
    #         api_key = "Api key"
    #         # base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
    #         base_url = "https://api.openweathermap.org/data/2.5/weather?q=${searchValue}&units=metric&appid={WriteYourAPIKey}"
    #         speak(" City name ")
    #         print("City name : ")
    #         city_name = takeCommand()
    #         complete_url = base_url + "appid =" + api_key + "&q =" + city_name
    #         response = requests.get(complete_url)
    #         x = response.json()

    #         if x["cod"] != "404":
    #             y = x["main"]
    #             current_temperature = y["temp"]
    #             current_pressure = y["pressure"]
    #             current_humidiy = y["humidity"]
    #             z = x["weather"]
    #             weather_description = z[0]["description"]
    #             print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(
    #                 current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

    #         else:
    #             speak(" City Not Found ")


    elif " weather" in query:
         search = "temperature in bhopal"
         url = f"http://www.google.com/search?q={search}"
         r = requests.get(url)
         data = BeautifulSoup(r.text,"html.parser")
         temp = data.find("div",class_="BNeawe").text
         speak(f"current {search} is {temp}")
    
    

    # elif "send message " in query:
    #         # You need to create an account on Twilio to use this service
    #         account_sid = 'Account Sid key'
    #         auth_token = 'Auth token'
    #         client = Client(account_sid, auth_token)

    #         message = client.messages \
    #             .create(
    #                 body=takeCommand(),
    #                 from_='Sender No',
    #                 to='Receiver No'
    #             )

    #         print(message.sid)
    
    elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(usrname)


    elif " no thanks "or "no" in query:
        speak("thanks for using me sir , have a good day.")
        sys.exit()
    
    speak("sir ,do you have any other work")    
    
    
    elif 'open camera' in query:
     cap =cv2.VideoCapture(0)
        while True:
               ret, img = cap.read()
               cv2.imshow('webcom',img)  
               k = cv2.waitKey(58)
               if k == 27:
                 break;
                 cap.release()
 cv2.destroyAllWindows()