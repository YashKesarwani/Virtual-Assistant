import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import subprocess
import calendar
import time
import random
import smtplib
import platform

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
email={"david":"11kesarwaniyash@gmail.com","ruler":"krazzyruler@gmail.com","santosh":"sahu18456@gmail.com"}
your_name='Yash'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wakeWord(text):
    WAKE_WORDS = ['david', 'okay david','hey david'] 
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!"+your_name)
        #speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!"+your_name)
    else:
        speak("Good Evening!"+your_name)
    speak("Hey I am David! I am your assisstant. How may I help you?")    
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("User said:",query)
        
    except Exception as e:
        #print(e)
        print("Say that again please!")
        return "None"
    return query
    
def greeting(text):
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'wassup', 'hello']
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            greet=random.choice(GREETING_RESPONSES)
            speak(greet)
    
def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]  
    monthNum=now.month
    dayNum=now.day

    month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December']
    ordinalNumbers=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
                      '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1]

def getTime():
    now=datetime.datetime.now()
    meridiem = ''
    if now.hour>=12:
        meridiem = 'pm' 
        hour = now.hour - 12
        if hour==0:
            hour=12
    else:
        meridiem = 'am'
        hour = now.hour
    if now.minute < 10:
        minute = '0'+str(now.minute)
    else:
        minute = str(now.minute)
    return 'It is '+ str(hour)+ ':'+minute+' '+meridiem
            
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("krazzyruler@gmail.com","softyvar")
    server.sendmail('krazzyruler@gmail.com',to,content)
    server.close()
    
    
if __name__=="__main__":
    while True:
        text=takeCommand().lower()
        if wakeWord(text)==True:
            wishMe()
            while True:
                query=takeCommand().lower()
                firefox="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox))
                if ('hey' in query) or ('hi' in query) or ('hello' in query) or ('wassup' in query) or ('hola' in query):
                    greeting(query)    
                if "wikipedia" in query:
                    speak("Searching in Wikipedia...")
                    query=query.replace('wikipedia',"")
                    results=wikipedia.summary(query,sentences=2)
                    speak("According to Wikipedia: ")
                    speak(results)
                elif 'open youtube' in query:
                    #webbrowser.open("youtube.com")
                    url="youtube.com"
                    webbrowser.get('firefox').open(url)
                elif 'open google' in query:
                    #webbrowser.open("google.com")
                    url="google.com"
                    webbrowser.get(firefox).open(url)
                elif 'open stackoverflow' in query:
                    #webbrowser.open("stackoverflow.com")
                    url="stackoverflow.com"
                    webbrowser.get(firefox).open(url)    
                elif 'play music' in query:
                    music_dir="E:\\Music Galaxy\\Songs Planet (Bollywood)"
                    songs=os.listdir(music_dir)
                    #print(songs)
                    n=random.randint(0,len(songs)-1)
                    os.startfile(os.path.join(music_dir,songs[n]))                                   
                elif 'the date' in query:
                    date=getDate()
                    speak(f"Sir, {date}")                   
                elif 'the time' in query:
                    #strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    #speak(f"Sir, The time is {strTime}") 
                    time=getTime()
                    speak(f"Sir, {time}")                    
                elif 'open visual studio code' in query:
                    Path="C:\\Program Files\\Microsoft VS Code\\Code.exe"
                    os.startfile(Path)
                elif 'open notepad' in query:
                    Path="C:\\Program Files\\Notepad++\\notepad++.exe"
                    os.startfile(Path)    
                elif ('send email' in query) or ('send an email' in query):
                    try:
                        speak("To whom I should send the email?")
                        name=''
                        flag=True
                        while True:
                            name=takeCommand().lower()
                            if 'terminate' in name:
                                flag=False
                                break
                            if 'none' not in name:
                                break
                        if flag==True:
                            to=email[name]
                            speak("What should I say?")
                            content=takeCommand()
                            sendEmail(to,content)
                            speak("Email has been sent!")
                        else:
                            speak("Email sending terminated")
                    except Exception as e:
                        #print(e)
                        speak("Sorry! Email has not been sent")
                elif 'on bluetooth' in query:
                    #os.system('cmd /k PowerShell -NoProfile -ExecutionPolicy Unrestricted -Command D:\\PythonFiles\\bluetooth.ps1')
                    #-BluetoothStatus On
                    #subprocess.call([r'D:\Python Files\exon.bat'])
                    #speak("Turned On")
                    #p=subprocess.Popen("D:\\Python Files\\exon.bat",shell=True)
                    #stdout,stderr=p.communicate()
                    powershell64 = os.path.join(os.environ['SystemRoot'],'SysNative' if platform.architecture()[0] == '32bit' else 'System32','WindowsPowerShell', 'v1.0', 'powershell.exe')
                    #print(powershell64)
                    p = subprocess.Popen([powershell64,'-ExecutionPolicy','Unrestricted','D:\\PythonFiles\\bluetooth.ps1'])
                    speak("Turned On")
                    #powershell64.wait()
                    #os.system("rfkill unlock bluetooth")#subprocess.call(["rfkill", "unblock", "bluetooth"])
                    
                elif 'off bluetooth' in query:
                    powershell64 = os.path.join(os.environ['SystemRoot'],'SysNative' if platform.architecture()[0] == '32bit' else 'System32','WindowsPowerShell', 'v1.0', 'powershell.exe')
                    p = subprocess.Popen([powershell64,'-ExecutionPolicy','Unrestricted','D:\\PythonFiles\\bluetooth.ps1'])
                    speak("Turned Off")
                    # p=subprocess.Popen("D:\\Python Files\\exoff.bat",stdout)
                    #os.system("rfkill block bluetooth")
                elif 'shut down' in query or 'turn off' in query or 'shutdown' in query:
                    speak('Are you sure you want to shut down the pc')
                    shutdown=takeCommand().lower()
                    if 'no' in shutdown:
                        speak('Enjoy your pc working sir..!!')
                    else:
                        speak('Shutting down. Goodbye sir. See you soon.')
                        time.sleep(2)
                        os.system("shutdown /s /t 1")
                elif 'restart' in query:
                    speak('Are you sure you want to restart the pc')
                    restart=takeCommand().lower()
                    if 'no' in restart:
                        speak('Enjoy your pc working sir..!!')
                    else:
                        speak('Restarting the PC sir. See you on the other side sir.')
                        time.sleep(2)
                        os.system("shutdown /r /t 1")
                elif 'restart' in query:
                    speak('Are you sure you want to logout from the pc')
                    logout=takeCommand().lower()
                    if 'no' in logout:
                        speak('Enjoy your pc working sir..!!')
                    else:
                        speak('Logging out from the PC sir. See you soon sir.')
                        time.sleep(2)
                        os.system("shutdown -l")
                elif 'thank you' in query:
                    speak('Glad that I could help you. What would you like me to do next?')
                elif 'quit' in query:
                        speak("Goodbye sir!")
                        sys.exit()
                else:
                    speak("Say that again!")    
            
    #speak("Hey I am david")
    

