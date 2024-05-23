import random
import threading
import time
from fonctions_geo import *
from recherche_par_nom import *
from matching_keyword import *
from recherche_autre import *
from voice_engine import *

# Variables de phrases
presentation = [
    "Bonjour, je suis GéoLocate, votre assistant vocal directionnel.",
    "Hello! Ici GéoLocate pour vous aider.",
    "Bonjour, vous. Moi c'est GéoLocate, votre guide.",
    "Cher ami, bonjour.",
    "Salutation à vous."
]

au_revoir = [
    "Au revoir et à bientôt",
]

# Variable partagée pour les réponses
response_event = threading.Event()
shared_response = None

def voice_listener():
    global shared_response
    while not response_event.is_set():
        try:
            voice_response = voiceRecognizer()
            if voice_response:
                shared_response = voice_response.lower()
                response_event.set()
        except Exception as e:
            print(f"Erreur de reconnaissance vocale : {e}")

def process_input(user_input):
    if 'stop' in user_input or 'stoppe' in user_input:
        return 'stop'
    elif 'nom' in user_input:
        say("D'accord. Veuillez m'indiquer le nom de l'endroit que vous recherchez s'il vous plaît.")
        nom_place = input("Nom de l'endroit : ")
        recherche_places_et_localites_par_nom(nom_place)
    elif 'type' in user_input:
        say("D'accord. Dites-moi quel genre d'endroit vous recherchez.")
        type_place = input("Type d'endroit : ")
        matching_keywords = trouver_mot_cle(type_place)
        if matching_keywords:
            keyword = matching_keywords[0]
            recherche_autre_critere(keyword=keyword)
        else:
            say("Aucune correspondance trouvée.")
    else:
        say("Commande non reconnue. Veuillez réessayer.")
    return None

if __name__ == '__main__':
    # Accueil et présentation
    say(presentation[random.randint(0, len(presentation) - 1)])
    
    while True:
        # Lancer le thread pour l'écoute vocale
        response_event.clear()
        listener_thread = threading.Thread(target=voice_listener)
        listener_thread.start()
        
        txt = "Vous souhaitez effectuer une recherche par 'nom' ou par 'type' ? Si non, tapez ou dites 'stop' : "
        say(txt)
        
        # Attendre l'entrée utilisateur
        main_reponse = input().lower()
        response_event.set()  # Arrêter la reconnaissance vocale

        listener_thread.join()  # Attendre que le thread se termine
        
        with response_event:
            user_input = shared_response if shared_response else main_reponse
            shared_response = None
        
        if user_input:
            if process_input(user_input) == 'stop':
                break

    say(au_revoir[random.randint(0, len(au_revoir) - 1)])
