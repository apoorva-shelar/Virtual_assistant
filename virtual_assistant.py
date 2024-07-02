import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import time

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

#programName = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=2)
        print('Ask me anything')
        recordedaudio=recognizer.listen(source,timeout=15)
    try:
        text_heard=recognizer.recognize_google(recordedaudio,language='en_US')
        text_heard=text_heard.lower()
        print('Your message:',format(text_heard))

    except Exception as ex:
        
        print('Please run the program again and try to ask before 20 seconds after you see "Ask me anything" on screen.')
     

    if 'chrome'in text_heard:
        a='Opening chrome'
        engine.say(a)
        engine.runAndWait()
       # programName = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
    if 'time' in text_heard:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text_heard:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text_heard)
    if 'youtube' in text_heard:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    if 'instagram' in text_heard:
        i='opening in sta gram'
        engine.say(i)
        engine.runAndWait()
        webbrowser.open('https://www.instagram.com')        

    if 'instagram' in text_heard and 'reels' in text_heard:
        ir='opening in sta gram reels'
        engine.say(ir)
        engine.runAndWait()
        webbrowser.open('https://www.instagram.com/reels') 
    
    if 'notepad' in text_heard:
        nt = 'Opening notepad'
        engine.say(nt)
        engine.runAndWait()
       # fileName = r"D:\Python Projects\test.txt"
        subprocess.Popen([r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2405.13.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe",r"D:\Python Projects\test.txt"])
while True:
    cmd()


