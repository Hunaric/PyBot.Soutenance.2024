import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('En ecoute...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        print(command)
        # say(command)
except:
    erreur = "Rien ne s'est passe comme prevu"
    print(erreur)
    # say(erreur)
    pass
