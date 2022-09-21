from win32com.client import Dispatch #levano audio speak
import speech_recognition as sr #levano audio rec
import datetime 
import os # screenshot
import pyautogui #levano screenshot
from playsound import playsound    
from tkinter import* 
import psutil # Bennet CPU
import pyjokes # Bennet Jokes







#====================Levano functions========================#           

speak = Dispatch("SAPI.SpVoice").Speak #SAPI.SpVoice = de built in windows voice

#===========================================================#


#====================Bennet functions========================#
def cpu():
	cpu = str(psutil.cpu_percent())
	print(cpu)
	speak(f"You are using {cpu} percent of the cpu.")

	
def jokes():
	my_joke = pyjokes.get_joke('en', category='neutral')
	print(my_joke)
	speak(my_joke)

def greet():
    speak("Starting up George")	

#==========================================================#




#====================Levano functions========================#
    #H = uur M = minuten S = Seconds
def time(): 
    Time = datetime.datetime.now().strftime('%H:%M:%S')
    speak("The current time is ")
    print("The current time is ")
    speak(Time)
    print(Time)

    #Y= Year volledig, B= Maand volledig A= Dag volledig
def date():   
    year= datetime.datetime.now().strftime("%Y:")# 	Year, full version
    Month= datetime.datetime.now().strftime("%B:")# Month name, full version
    Day= datetime.datetime.now().strftime("%A:")#  	Weekday, full version
    speak(year)
    speak(Month)
    speak(Day)

def whoareyou():
    speak ("My name is george i was made by Bennet Levano ")
    print ("My name is george i was made by Bennet Levano ")

def screenshot():
    myScreenshot = pyautogui.screenshot() 
    myScreenshot.save('pj.png')
 
#===========================================================#




#====================Levano functions========================#           

def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #wait for 1 sec dan luisteren naar audio
        audio = r.listen(source)    # listen for the first phrase and extract it into audio data
     

    try:
        print("Recongnizning...")
        recognised = r.recognize_google(audio, language='en')
        #speak("You said")
        print("You said")
        print(recognised)

    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return None

    return recognised


#===========================================================#
#============Aanroepen van de gemaakte functies=============#
#===========================================================#


def run_code():
    run = True 

    while run:

        output = takecommand()

    #==============Levano Aanroepen van functions=================#  
        if "time" in output:
            time()

        elif "date" in output:
            date()

        elif "screenshot" in output:
            screenshot()

            
        elif "who are you" in output:
            whoareyou()

        elif "hallo jarvis" in output:
            greet()


    #===============Bennet Aanroepen van functions=================#
        elif "CPU" in output:
            cpu()

        elif "joke" in output:
            jokes()

#===========================================================#




import tkinter as tk

from PIL import ImageTk, Image


root = tk.Tk()
#out = takecommand()



button = Button(root, text="start AI", command = run_code)
button.pack()

img = ImageTk.PhotoImage(Image.open("mlvoice.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")



root.mainloop()
