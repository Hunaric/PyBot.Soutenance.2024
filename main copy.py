import random
import json
from fonctions_geo import *
from recherche_par_nom import *
from matching_keyword import *
from recherche_autre import *
from voice_engine import *

# Ici sont repertoriés les variables phrases:
presentation = [
    "Bonjour, je suis GéoLocate, votre assistant vocal directionnel.",
    "Hello! Ici GéoLocate pour vous aider.",
    "Bonjour, vous. Moi c'est GéoLocate, votre guide.?",
    "Cher ami, bonjour.",
    "Salutation a vous."
]

au_revoir = [
    "Au revoir et a bientôt",
]

if __name__ == '__main__':
    # Accueil et presentation
    say(presentation[random.randint(0,len(presentation)-1)])
    indiquer = True
    trouver = False
    while indiquer:
        txt = "Vous souhaitez effectuer une recherche par 'nom' ou par 'type' ? Si non, tapez ou dites 'stop' "
        say(txt)
        main_reponse = input()  

        if main_reponse.lower() == 'stop':
            indiquer = False

        elif main_reponse.lower() == 'nom':
            say("D'accord. Veuillez m'indiquer le nom de l'endroit que vous recherchez s'il vous plait.")
            texte = "Nom de l'endroit : "
            say(texte)
            nom_place = input()
            # Fonction de recherche avec le nom
            # say("Y a  t-il des details que je dois connaitre sur l'endroit ?")
            # reponse = input("'Oui' ou 'Non' : ")
            
            # if reponse.lower() == 'oui':
            #     say("Dites les moi alors, vous avez une idée de sa localité ? Si oui, ecirvez le ou mettez juste 'Non'...")
            #     detail_localite = input("Je vous écoute: ")
                
            #     if detail_localite.lower() == 'non':
            #         detail_localite = None
                
            #     say("Savez-vous de quel genre d'endroit il s'agit  ? Si oui, ecirvez le ou mettez juste 'Non'...")
            #     detail_type = input("Je vous écoute: ")

            #     if detail_type.lower() == 'non':
            #         detail_type = None 
                
            # else:
            #     say("D'accord. J'effectue la recherche pour vous. Donnez moi quelques instants...")
            recherche_places_et_localites_par_nom(nom_place)
            
        elif main_reponse.lower() == 'type':

            say("D'accord. Dites moi quel genre d'endroit vous recherchez.")
            texte_2 = "Type d'endroit : "
            say(texte_2)
            type_place = input()
            # say("Maintenant, j'aimerais savoir si vous le recherchez dans une zone donnée. Si oui, dites moi où.")
            # zone_recherche = input("Je vous écoute: ")

            matching_keywords = trouver_mot_cle(type_place)
            if matching_keywords:
                keyword = matching_keywords[0]
                mot_cle = trouver_mot_cle(keyword)
                # say("Correspondances trouvées : ", matching_keywords)
                # say("Correspondances trouvées : ", matching_keywords[0])
                recherche_autre_critere(keyword=keyword)
            else:
                say("Aucune correspondance trouvée.")
                matching_keywords = None

    say(au_revoir[random.randint(0,len(au_revoir)-1)])



