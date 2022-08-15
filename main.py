import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("agent spidy 1 21 reporting sir")

    elif hour>=12 and hour<=18:
        speak("agent spidy 1 21 reporting sir!")

    else:
        speak("agent spidy 1 21 reporting sir")
    speak("Hi I am agent spidy 1 21. I am created by Harshit and Rounak. I am a spider robot")
def takeCommand():
    # it takes microphone as input

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
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kumarisuchi569@gmail.com', 'Suchi@145')
    server.sendmail('kvinod03896@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\kumar\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(1, 13)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'explain yourself' in query:
            speak("I am a spider robot which can walk, dance, or controlled by a smart phone. I have 4 components.")
            speak("First component is arduino nano, The Arduino Nano is one type of microcontroller board")
            speak("and it is designed by Arduino.cc")
            speak("Arduino board designs use a variety of microprocessors and controllers.")
            speak("The microcontrollers can be programmed using the C and C++ programming languages")
            speak("using a standard API which is also known as the Arduino language")
            speak("The second thing was servo motor, the servo motor is a a motor that can be controlled by arduino.")
            speak("A typical servo consists of a small electric motor driving a train of reduction gears.")
            speak("A potentiometer is connected to the output shaft.")
            speak("Some simple electronics provide a closed-loop servomechanism.")
            speak("the third component is a bluetooth module, HC-05 Bluetooth Module is a low-cost,")
            speak("easy-to-operate and small-sized module used for wireless communication in the Bluetooth spectrum.")
            speak("It supports Serial Port Protocol (SPP),")
            speak("which helps in sending/receiving data to/from a microcontroller (i.e. Arduino UNO).")
            speak("and the last thing is my structure, my structure is inspired by spider and is made of sun board.")
            speak("I can be used as a pet, transfer objects, search operation etc.")
            speak("I have also negative results that any thief can misuse me")
            speak("ok thank you. bye bye")

        elif 'email to rounak' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "suchiyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend hp 35 bhai. I am not able to send this email")

