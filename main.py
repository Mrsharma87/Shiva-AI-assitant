import requests
import os
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad
from functions.os_ops import open_chrome,open_control_panel,open_edge,open_excel,open_file_explorer,open_powerpoint,open_vscode,open_windows_media_player,open_word
from random import choice
from utils import opening_text
from pprint import pprint

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QTime,QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisSuperUI import Ui_Form


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 200)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(audio):
    """Used to speak whatever text is passed to it"""

    engine.say(audio)
    engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExection()

    def commands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source , duration=1)
            audio=r.listen(source)
        try:
            print("Wait for few moments...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Just Said: {query}\n")
              
        except Exception as e:
            print(e)
            speak('Sorry, I could not understand. Could you please say that again?')
            query="none"
        
        return query

    def wishings(self):
        hour = int(datetime.now().hour)
        if (hour >= 6) and (hour < 12):
            speak(f"Good Morning {USERNAME}")
        elif (hour >= 12) and (hour < 16):
            speak(f"Good afternoon {USERNAME}")
        elif (hour >= 16) and (hour < 19):
            speak(f"Good Evening {USERNAME}")
        speak(f"I am {BOTNAME}. How may I assist you?")
        print(f"I am {BOTNAME}. How may I assist you?")
        
    def TaskExection(self):
        self.wishings()
        while True:
            self.query = self.commands().lower()

            if 'open notepad' in self.query:
                open_notepad()

            elif 'close notepad' in self.query:
                speak('closing notepad sir')
                os.system('taskkill /f /im notepad.exe')    

            elif 'open command prompt' in self.query or 'open cmd' in self.query:
                open_cmd()

            elif 'close command prompt' in self.query or 'close cmd' in self.query:
                speak('closing Sir')
                os.system('taskkill /f /im cmd.exe ')    

            elif 'open camera' in self.query:
                open_camera()

            elif 'close camera' in self.query:
                os.system('taskkill /f /im WindowsCamera.exe')

            elif 'open calculator' in self.query:
                open_calculator()

            elif 'close calculator' in self.query:
                os.system('taskkill /f /im CalculatorApp.exe')

            elif 'open file explorer' in self.query:
                open_file_explorer()  

            elif 'close file explorer' in self.query:
                speak('closing  sir')
                os.system('taskkill /f /im explorer.exe')

            elif 'open edge ' in self.query:
                speak('opening Edge')
                open_edge()

            elif 'close edge ' in self.query:
                speak('closing sir')
                os.system('taskkill /f /im msedge.exe')  

            elif 'open chrome' in self.query:
                open_chrome()

            elif 'close chrome ' in self.query:
                speak('closing sir')
                os.system('taskkill /f /im chrome.exe')

            elif 'open word' in self.query:
                open_word()

            elif 'close word ' in self.query:
                speak('closing sir')
                os.system('taskkill /f /im WINWORD.exe')

            elif 'open excel' in self.query:
                open_excel()

            elif 'close excel ' in self.query:
                speak('closing sir')
                os.system('taskkill /f /im EXCEL.exe')    

            elif 'open powerpoint' in self.query:
                open_powerpoint()

            elif 'close powerpoint ' in self.query:
                speak('closing sir')
                os.system('taskkill /f /im POWERPNT.exe')    

            elif 'open vs code' in self.query:
                open_vscode()
    

            elif 'open window media player' in self.query:
                open_windows_media_player()

            elif 'close window media player ' in self.query:
                speak('closing sir')
                os.system('taskkill /f /im wmplayer.exe')     

            elif 'open control pannel' in self.query:
                open_control_panel()

            elif 'close control pannel ' in self.query:
                speak('closing sir')
                os.system('taskkill /f /im control .exe')    

            elif 'ip address' in self.query:
                ip_address = find_my_ip()
                speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

            elif 'wikipedia' in self.query:
                speak('What do you want to search on Wikipedia, sir?')
                search_query = self.commands().lower()
                results = search_on_wikipedia(search_query)
                speak(f"According to Wikipedia, {results}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(results)

            elif 'youtube' in self.query:
                speak('What do you want to play on Youtube, sir?')
                print('What do you want to play on Youtube, sir?')
                video = self.commands().lower()
                play_on_youtube(video)

            elif 'search on google' in self.query:
                speak('What do you want to search on Google, sir?')
                print('What do you want to search on Google, sir?')
                query = self.commands().lower()
                search_on_google(query)

            elif "send whatsapp message" in self.query:
                speak(
                    'On what number should I send the message sir? Please enter in the console: ')
                number = input("Enter the number: ")
                speak("What is the message sir?")
                message = self.commands().lower()
                send_whatsapp_message(number, message)
                speak("I've sent the message sir.")

            elif "send an email" in self.query:
                speak("On what email address do I send sir? Please enter in the console: ")
                receiver_address = input("Enter email address: ")
                speak("What should be the subject sir?")
                subject = self.commands().capitalize()
                speak("What is the message sir?")
                message = self.commands().capitalize()
                if send_email(receiver_address, subject, message):
                    speak("I've sent the email sir.")
                else:
                    speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

            elif 'joke' in self.query:
                speak(f"Hope you like this one sir")
                joke = get_random_joke()
                speak(joke)
                speak("For your convenience, I am printing it on the screen sir.")
                pprint(joke)

            elif "advice" in self.query:
                speak(f"Here's an advice for you, sir")
                advice = get_random_advice()
                speak(advice)
                speak("For your convenience, I am printing it on the screen sir.")
                pprint(advice)

            elif "trending movies" in self.query:
                speak(f"Some of the trending movies are: {get_trending_movies()}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(*get_trending_movies(), sep='\n')

            elif 'news' in self.query:
                speak(f"I'm reading out the latest news headlines, sir")
                speak(get_latest_news())
                speak("For your convenience, I am printing it on the screen sir.")
                print(*get_latest_news(), sep='\n')

            elif 'weather' in self.query:
                ip_address = find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                speak(f"Getting weather report for your city {city}")
                weather, temperature, feels_like = get_weather_report(city)
                speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.startPushButton.clicked.connect(self.startTask)
        self.ui.quitPushButton.clicked.connect(self.close)

    def startTask(self):
        # Jarvis GUI
        self.ui.movie = QtGui.QMovie("C:\\Users\\sanuj\\OneDrive\\Documents\\Project\\GUI files\\Jarvis_Gui (1).gif")
        self.ui.jarvisGUI.setMovie(self.ui.movie)
        self.ui.movie.start()
        # ironManBackground
        self.ui.movie = QtGui.QMovie("C:\\Users\\sanuj\\OneDrive\\Documents\\Project\\GUI files\\Iron_Template.jpg")
        self.ui.ironManBackground.setMovie(self.ui.movie)
        self.ui.movie.start()
        # ironmanGIF
        self.ui.movie = QtGui.QMovie("C:\\Users\\sanuj\\OneDrive\\Documents\\Project\\GUI files\\Iron_Template_1.gif")
        self.ui.ironManGIF.setMovie(self.ui.movie)
        self.ui.movie.start()
        # dateLabel
        self.ui.movie = QtGui.QMovie("C:\\Users\\sanuj\\OneDrive\\Documents\\Project\\GUI files\\gggf.jpg")
        self.ui.dateLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        # timeLabel
        self.ui.movie = QtGui.QMovie("C:\\Users\\sanuj\\OneDrive\\Documents\\Project\\GUI files\\gggf.jpg")
        self.ui.timeLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        # startLabelNotButton
        self.ui.movie = QtGui.QMovie("C:\\Users\\sanuj\\OneDrive\\Documents\\Project\\GUI files\\Start.png")
        self.ui.startLabelNotButton.setMovie(self.ui.movie)
        self.ui.movie.start()
        # quitLabelNotButton
        self.ui.movie = QtGui.QMovie("C:\\Users\\sanuj\\OneDrive\\Documents\\Project\\GUI files\\Quit.png")
        self.ui.quitLabelNotButton.setMovie(self.ui.movie)
        self.ui.movie.start()
        # earthGIF
        self.ui.movie = QtGui.QMovie("C:\\Users\\sanuj\\OneDrive\\Documents\\Project\\GUI files\\Earth.gif")
        self.ui.earthGIF.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        currentTime = QTime.currentTime()
        currentDate = QDate.currentDate()
        labelTime = currentTime.toString('hh:mm:ss')
        labelDate = currentDate.toString(Qt.ISODate)
        self.ui.dateTextBrowser.setText(f"Date: {labelDate}")
        self.ui.timeTextBrowser.setText(f"Date: {labelTime}")

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())