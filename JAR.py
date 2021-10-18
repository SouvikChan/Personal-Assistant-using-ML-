from bs4 import BeautifulSoup
import pyttsx3
import requests #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import time
import os
import smtplib
import cv2
import random
import pywhatkit as kit
from requests import get
import pyjokes
import pyautogui
import instadownloader
import instaloader
from PIL import Image
from pywikihow import WikiHow, search_wikihow
import wolframalpha
from bs4 import BeautifulSoup
import PyPDF2
from PyDictionary import PyDictionary as Diction




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
#engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def computational_intelligence(question):
    try:
        client = wolframalpha.Client("A4AXYA-J3AAYEG2U3")
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None


def wishMe():
    #####
    #speak("Initializing Jarvis")
    #print("Initializing Jarvis")
    #speak("Starting all systems applications")
    #print("Starting all systems applications")
    #speak("Installing and checking all drivers")
    #print("Installing and checking all drivers")
    #speak("Caliberating and examining all the core processors")
   # #print("Caliberating and examining all the core processors")
    #speak("Checking the internet connection")
    #print("Checking the internet connection")
    #speak("Wait a moment sir")
    #print("Wait a moment sir")
    #speak("All drivers are up and running")
    #print("All drivers are up and running")
    #speak("All systems have been activated")
    #print("All systems have been activated")
    #speak("Now I am online")
    #print("Now I am online")
    ####
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
        print("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
        print("Good Afternoon sir")   

    else:
        speak("Good Evening sir!")
        print("good Evening sir")  
    c_time = datetime.datetime.now()
    speak(f"Currently it is {c_time}")
    print(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")
    print("I am Jarvis. Online and ready sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please sir...")
        speak("Say that again please sir")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('souvikchandra9454@gmail.com', 'bokulful')
    server.sendmail('souvikchandra9454@gmail.com', to, content)
    server.close()

def search_wikihow(query, max_results=10, lang="en"):
    return list(WikiHow.search(query, max_results, lang))

#def Dict():
    speak("Activated Dictionary mode")
    speak("tell me the problem")
    probl = takeCommand()
    
    if "meaning" in probl:
        probl = probl.replace("what is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of")
        probl = probl.replace("meaning of","")
        result = Diction.meaning(probl)
        speak(f"The meaning of {probl} is {result}")
        print(f"The meaning of {probl} is {result}")
                
    elif "synonym" in probl:
        probl = probl.replace("what is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of")
        probl = probl.replace("synonym of","")
        result = Diction.synonym(probl)
        speak(f"The synonym of {probl} is {result}")
        print(f"The synonym of {probl} is {result}")
                
    elif "antonym" in probl:
        probl = probl.replace("what is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of")
        probl = probl.replace("antonym of","")
        result = Diction.antonym(probl)
        speak(f"The antonym of {probl} is {result}")
        print(f"The antonym of {probl} is {result}")
    elif "close" in probl or "exit" in probl or "exit dictionary" in probl or "close dictionary" in probl:
        speak("Exited Dictionary")
    
    


    #book = open('DynamicProgramingForInterViews.pdf','rb')
    #pdfReader = PyPDF2.PdfFileReader(book)
    #pages = pdfReader.numPages
    #speak(f"Total numbers of pages in this book {pages} ")
    #speak("sir please enter the page number which i have to read")
    #pg = int(input("Please enter the page number:"))
    #page = pdfReader.getPage(pg)
    #text = page.extractText()
    #speak(text)
    

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube from web browser sir")


        elif 'open google' in query or "google search" in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("Opening google from web browser sir")  

        
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook from web browser sir")

        elif 'who is your owner' in query: 
            speak("souvik is my owner he is a genious")

        elif 'hello jarvis' in query or "hello" in query: 
            speak("Hello sir" or " Always for you sir" or "Hi Sir")

        elif 'how are you' in query: 
            speak("I am fine sir ")

        elif 'i am fine' in query: 
            speak("Okay sir that's great")

        elif 'i love you' in query: 
            speak("I love you 3000")

        elif 'i love you 4000' in query: 
            speak("I love you 5000")

        elif "fuck you" in query: 
            speak("Fuck off")

        elif 'say hello to mother' in query or 'say hello to my mother' in query: 
            speak("hello tanusree")    

        elif 'say hello to father' in query or 'say hello to my father' in query: 
            speak("hello nabakumar")

        elif "thank you" in query or "thanks" in query or "thank you jarvis" in query:
            speak("It's my pleasure sir")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("Opening instagram from web browser sir") 

        
        elif 'who is sucha' in query or 'who is suche' in query or 'suche' in query or 'sucha' in query:
            speak("she is my owners girl friend")  


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening stackoverflow from web browser sir")  

        #elif "where is" in query:
                #place = query.split('where is ', 1)[1]
                #current_loc, target_loc, distance = query.location(place)
                #city = target_loc.get('city', '')
                #state = target_loc.get('state', '')
                #country = target_loc.get('country', '')
                #time.sleep(1)
                #try:

                    #if city:
                        #res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        #print(res)
                        #speak(res)

                    #else:
                        #res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        #print(res)
                        #speak(res)

                #except:
                    #res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    #speak(res)

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)   
            os.startfile(os.path.join(music_dir, rd))
            speak("Enjoy sir")

        elif 'play iron man dialogue' in query or "iron man dialogue" in query or "ironman dialogue" in query or "tony stark dialogue" in query:
            music_dir = 'E:\\Iron Man'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)   
            os.startfile(os.path.join(music_dir, rd))
            speak("Enjoy sir")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif "read pdf" in query or "read PDF" in query:
            book = open('DynamicProgramingForInterViews.pdf','rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speak(f"Total numbers of pages in this book {pages} ")
            speak("sir please enter the page number which i have to read")
            pg = int(input("Please enter the page number:"))
            page = pdfReader.getPage(pg)
            text = page.extractText()
            speak(text)


        elif 'open code' in query:
            codePath = "F:\\Visual Studio Code\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening VS code sir")

        elif 'close code' in query:
            speak("Okay sir, closing vs code")
            os.system("taskkill /f /im Code.exe")

        elif "open dev" in query or "open deb" in query:
            codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
            speak("Opening Dev cpp sir")

        elif 'close dev' in query:
            speak("Okay sir, closing dev cpp")
            os.system("taskkill /f /im devcpp.exe")

        elif 'open spotify' in query:
            codePath = "C:\\Users\\SOUVIK\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
            speak("Opening spotify sir")

        elif 'close spotify' in query:
            speak("Okay sir, closing spotify")
            os.system("taskkill /f /im Spotify.exe")

        elif 'open telegram' in query:
            codePath = "C:\\Users\\SOUVIK\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(codePath)
            speak("Opening Telegram sir")

        elif 'close telegram' in query:
            speak("Okay sir, closing telegram")
            os.system("taskkill /f /im Telegram.exe")

        elif 'open notepad' in query:
            codePath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(codePath)
            speak("Opening notepad sir")

        elif 'close notepad' in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\SOUVIK\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
            speak("Opening whatsapp sir")

        elif 'close whatsapp' in query:
            speak("Okay sir, closing whatsapp")
            os.system("taskkill /f /im WhatsApp.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")
            speak("Opening command prompt sir")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(1)
                if k==1:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            speak("Opening camera sir")

        elif "dictionary" in query or "activate dictionary mode" in query:
            speak("Activated Dictionary mode")
            speak("Tell me the problem as meaning of: or synonym of: or antonym of:")
            print("Tell me the problem as meaning of: or synonym of: or antonym of:")
            probl = takeCommand()
            
            if "meaning" in probl:
                #probl = probl.replace("what is the","")
                #probl = probl.replace("jarvis","")
                #probl = probl.replace("of")
                probl = probl.replace("meaning of","")
                result = Diction.meaning(probl)
                speak(f"The meaning of {probl} is {result}")
                print(f"The meaning of {probl} is {result}")
                        
            elif "synonym" in probl:
                #probl = probl.replace("what is the","")
                #probl = probl.replace("jarvis","")
                #probl = probl.replace("of")
                probl = probl.replace("synonym of","")
                result = Diction.synonym(probl)
                speak(f"The synonym of {probl} is {result}")
                print(f"The synonym of {probl} is {result}")
                        
            elif "antonym" in probl:
                #probl = probl.replace("what is the","")
                #probl = probl.replace("jarvis","")
                #probl = probl.replace("of")
                probl = probl.replace("antonym of","")
                result = Diction.antonym(probl)
                speak(f"The antonym of {probl} is {result}")
                print(f"The antonym of {probl} is {result}")
            elif "close" in probl or "exit" in probl or "exit dictionary" in probl or "close dictionary" in probl:
                speak("Exited Dictionary")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f"Your IP address is {ip}")
            speak(f"Your IP address is {ip}")

        elif "send message"  in query or "send a message" in query:
            speak("Tell me the name of the Person")
            name = input("Enter username here: ")
            if "Maa Voda" in name:
                speak("Tell me the massage, sir")
                msg = takeCommand()
                speak("Tell me the time sir!")
                speak("time in hour")
                hour = int(takeCommand())
                speak("time in minutes")
                min = int(takeCommand())
                kit.sendwhatmsg("+919732958884",msg,hour,min,20)
                speak("Massage send sir")
            elif "Suchatana Airtel" in name:
                speak("Tell me the massage, sir")
                msg = takeCommand()
                speak("Tell me the time sir!")
                speak("time in hour")
                hour = int(takeCommand())
                speak("time in minutes")
                min = int(takeCommand())
                kit.sendwhatmsg("+917318647022",msg,hour,min,20)
                speak("Massage send sir")
            elif "Abhishek 2" in name:
                speak("Tell me the massage, sir")
                msg = takeCommand()
                speak("Tell me the time sir!")
                speak("time in hour")
                hour = int(takeCommand())
                speak("time in minutes")
                min = int(takeCommand())
                kit.sendwhatmsg("+917029565963",msg,hour,min,20)
                speak("Massage send sir")
            elif "Gourab Bhattacharyya Hetc Cse" in name:
                speak("Tell me the massage, sir")
                msg = takeCommand()
                speak("Tell me the time sir!")
                speak("time in hour")
                hour = int(takeCommand())
                speak("time in minutes")
                min = int(takeCommand())
                kit.sendwhatmsg("+917439482235",msg,hour,min,20)
                speak("Massage send sir")
            elif "Srijon Basu Ce Hetc" in name:
                speak("Tell me the massage, sir")
                msg = takeCommand()
                speak("Tell me the time sir!")
                speak("time in hour")
                hour = int(takeCommand())
                speak("time in minutes")
                min = int(takeCommand())
                kit.sendwhatmsg("+916295776177",msg,hour,min,20)
                speak("Massage send sir")

            else:
                speak("I am not able to send this")
          

        elif 'youtube' in query:
            video = query.split(' ')[1]
            speak(f"Okay sir, playing {video} on youtube")
            kit.playonyt(video)
            speak("Enjoy sir")

        #elif "youtube search" in query:
            #speak("ok sir , this is what i found for you")
            #query = query.replace("jarvis","")
            #query = query.replace("youtube search","")
            #web = 'https://www.youtube.com/results?search_query=' + query
            #speak("Done sir")

        elif "website" in query:
            speak("sir, what website should i search")
            mm = takeCommand().lower()
            webbrowser.open(f"{mm}")
            speak("Opening website from web browser sir")  


        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==6:
                music_dir = 'E:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir.songs[0]))

        elif 'open Chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            speak("Opening Chrome sir")

        elif 'activate how to do mode' in query:
            speak("How to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("Okay sir, how to mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry sir, i am not able to find this")

#to find location

        elif "where i am" in query or "show my location" in query:
            speak("wait sir let me check")
            #try:
            ip_add = requests.get('https://api.ipify.org').text
            print(ip_add)
            url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
            geo_q = requests.get(url)
            geo_d = geo_q.json()
            city= geo_d['city']
            country = geo_d['country']
            speak(f"Sir i am not sure, but i think we are in {city} city of {country} country.")
            print(f"Sir i am not sure, but i think we are in {city} city of {country} country.")
            #except Exception as e:
               # speak("sorry sir, Due to network issue i am not able to find where we are.")
               # pass

#To check a instagram profile......

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir, enter the user name correctly.")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            speak("sir would you like to download profile picture of this account.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir, profile picture is saved in our main folder. now i am ready")
            else:
                pass

#..............To take screenshot...........
        
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            print("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            print("please sir hold the screen for few seconds, i am taking screenshot")
            img = pyautogui.screenshot()
            name = f"{name}.png"
            img.save(name)
            speak(" I am dine sir, the screenshot is saved in our main folder.")
            print(" I am dine sir, the screenshot is saved in our main folder.")

        
        elif "show me the screenshot" in query:
                try:
                    img = Image.open('F://Python//' + name)
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")


        elif "calculate" in query:
            question = query
            answer = computational_intelligence(question)
            speak(answer)

        elif "what is" in query or "who is" in query or "do you know anything about" in query or "tell me about" in query:
            question = query
            answer = computational_intelligence(question)
            speak(answer)
    
        elif "hide all files" in query or "hide this folder" in query:
            os.system("attrib +h /s /d")
            speak("Sir, all the files in this folder are now hidden")

        elif "visible" in query or "make files visible" in query or "visible all files" in query:
            os.system("attrib -h /s /d")
            speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

        elif "today's temparature" in query or "today temparature" in query or "today temperature" in query:
            search = "temparature in Serampore"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")

        elif "today's weather" in query or "today weather" in query or "today weather" in query:
            search = "weather in Serampore"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")


        #elif 'weather' in query:
                #city = query.split(' ')[-1]
                #weather_res = query.weather(city=city)
                #print(weather_res)
                #speak(weather_res)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        elif 'quit' in query or 'bye' in query or 'you can sleep now' in query:
            speak("Quiting Sir. Thanks for your time , have a nice day")
            exit()

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "souvikchandra9454@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Souvik sir, I am not able to send this email")    
