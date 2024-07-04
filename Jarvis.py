import sys
import os
import subprocess
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how can I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:  {query}\n")
        return query  # Return the recognized query back to the main program

    except Exception as e:
        print("Say that again please...")
        return "None"

def closeChromeTab():
    pyautogui.hotkey('alt', 'f4')

try:
 def increase_volume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(volume.GetMasterVolume() + 0.4,None)


 def decrease_volume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(volume.GetMasterVolume() - 0.4, None)
except Exception as e:
    print("Say that again please...")
def pause_youtube():
    try:
        pyautogui.press('space')  # Presses the spacebar to pause the YouTube video
        speak("Pausing YouTube video")
    except Exception as e:
        print(e)
def forward_youtube():
    try:
        pyautogui.press('l')
        speak("Skipping YouTube video...")
    except Exception as e:
        print(e)
def backward_youtube():
    try:
        pyautogui.press('j')
        speak("Skipping YouTube video...")
    except Exception as e:
        print(e)

def zoom_youtube():
    try:
        pyautogui.press('f')
        speak("Zooming YouTube video...")
    except Exception as e:
        print(e)
def close_youtube():
    try:
        pyautogui.hotkey('alt', 'f4')  # Simulate pressing Alt+F4 to close the active window
        speak("Closing YouTube video")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    wishMe()
while True:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open google' in query:
        webbrowser.open('google.com')
    elif 'chatgpt' in query:
        speak("Searching Chat GPT...")
        query = query.replace("chatgpt", "")
        pywhatkit.playonyt(query)
        speak(f"Searching {query} on Chat GPT")
    elif 'made you' in query:
        speak("Made by Surendra and Vishnu ")
        print("Surendra & Vishnu")
    elif 'youtube' in query:
        speak("Searching YouTube...")
        query = query.replace("youtube", "")
        pywhatkit.playonyt(query)
        speak(f"Playing {query} on YouTube")
    elif 'volume up' in query:
        speak("Increasing volume...")
        try:
            increase_volume()
        except Exception as e:
            print(e)

    elif 'volume down' in query:
        speak("Decreasing volume...")
        try:
            decrease_volume()
        except Exception as e:
            print(e)
    elif 'pause video' in query or 'resume video' in query:
        pause_youtube()
    elif 'skip forward' in query:
        forward_youtube()
    elif 'skip backward' in query:
        backward_youtube()
    elif 'zoom in' in query or 'zoom out' in query or 'zoomIn' in query or 'zoomOut' in query:
        zoom_youtube()
    elif 'close' in query :
        close_youtube()
    elif 'exit' in query:
        speak("Exiting program.")
        break
