import speech_recognition as sr
import pyttsx3
from matching_keyword import *
import datetime

listener = sr.Recognizer()

def say(text, speed=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)  # Vitesse de lecture
    print(text)
    engine.say(text)
    engine.runAndWait()

def say_only(text, speed=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)  # Vitesse de lecture
    engine.say(text)
    engine.runAndWait()
    
def voiceRecognizer():
    try:
        with sr.Microphone() as source:
            print('En ecoute...')
            sr.pause_theshold = 1
            sr.non_speaking_duration = 15
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="fr-FR")
            texte = f"Vous avez dit : \"{command}\""
            say(texte)
            return command
            # with open("output.txt", "w"):
            #     file.write(command)
    except:
        erreur = "Je crois avoir du mal a comprendre votre requête"
        say(erreur)
        pass
    
def voiceCity():
    voice = None
    try:
        with sr.Microphone() as source:
            print('En ecoute...')
            sr.pause_theshold = 1
            sr.non_speaking_duration = 15
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="fr-FR")
            return command
    except:
        erreur = "Je crois avoir du mal a comprendre votre requête"
        say(erreur)
        pass