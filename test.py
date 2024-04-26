import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def voiceRecognizer():
    try:
        with sr.Microphone() as source:
            print('En ecoute...')
            sr.pause_theshold = 1
            sr.non_speaking_duration = 5
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="fr-FR")
            print(f"Vous avez dit : \"{command}\"")
            say(command)
            return command
            # with open("output.txt", "w"):
            #     file.write(command)
    except:
        erreur = "Rien ne s'est passé comme prevu"
        print(erreur)
        say(erreur)
        pass

if __name__ == '__main__':
    accueil = "Mi quoi Bord. Que puis-je faire pour vous ?"
    bye = "Au revoir et a la prochaine"
    say(accueil)
    # while True:
    maVoix = voiceRecognizer()
    if maVoix:
        if "recherche un endroit" in maVoix.lower() or "trouver un lieu" in maVoix.lower():
            print("D'accord")
        if "quelle heure" in maVoix.lower():
            heure = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Il sonne exactement {heure} heure {minute} minutes")
    else:
        say(bye)