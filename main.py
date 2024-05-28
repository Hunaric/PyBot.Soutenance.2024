import random
from fonctions_geo import *
from recherche_par_nom import *
from matching_keyword import *
from recherche_autre import *
from voice_engine import *

# Ici sont repertoriés les variables phrases:
presentation = [
    "Bonjour, je suis GéoLocate, votre assistant vocal directionnel.",
    "Hello! Ici GéoLocate pour vous aider.",
    "Bonjour, vous. Moi c'est GéoLocate, votre guide.",
    "Cher ami, bonjour.",
    "Salutation a vous."
]

au_revoir = [
    "Au revoir et a bientôt",
]

if __name__ == '__main__':
    # Accueil et presentation
    say(presentation[random.randint(0, len(presentation) - 1)])
    indiquer = True
    while indiquer:
        main_reponse = None
        while main_reponse is None:
            txt = "Vous souhaitez effectuer une recherche par 'nom' ou par 'type' ? Si non, dites 'stop' "
            say(txt)
            main_reponse = voiceRecognizer()

        if 'stop' in main_reponse.lower() or "stoppe" in main_reponse.lower() or "arrête" in main_reponse.lower() or "arrêter" in main_reponse.lower():
            indiquer = False
        elif 'nom' in main_reponse.lower() or 'non' in main_reponse.lower():
            say("D'accord. Veuillez m'indiquer le nom de l'endroit que vous recherchez s'il vous plaît.")
            texte = "Nom de l'endroit : "
            nom_place = input(texte)
            recherche_places_et_localites_par_nom(nom_place)
        elif 'type' in main_reponse.lower() or 'pratique' in main_reponse.lower():
            say("D'accord")
            type_place = None
            while type_place is None:
                say("Dites moi quel genre d'endroit vous recherchez.")
                texte_2 = "Type d'endroit : "
                print(texte_2)
                type_place = voiceRecognizer()

            matching_keywords = trouver_mot_cle(type_place)
            if matching_keywords:
                keyword = matching_keywords[0]
                mot_cle = trouver_mot_cle(keyword)
                recherche_autre_critere(keyword=keyword)
            else:
                say("Aucune correspondance trouvée.")
                matching_keywords = None

    say(au_revoir[random.randint(0, len(au_revoir) - 1)])
