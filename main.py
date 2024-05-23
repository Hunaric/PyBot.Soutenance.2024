import random
import json
from fonctions_geo import *
from recherche_par_nom import *
from matching_keyword import *
from recherche_autre import *

# Ici sont repertoriés les variables phrases:
presentation = [
    "Bonjour, je suis GéoLocator, votre assistant vocal directionnel.",
    "Hello! Ici GéoLocator pour vous aider.",
    "Bonjour, vous. Moi c'est GéoLocator, votre guide.?",
    "Cher ami, bonjour.",
    "Salutation a vous."
]

au_revoir = [
    "Au revorir et a bientôt",
]

if __name__ == '__main__':
    # Accueil et presentation
    print(presentation[random.randint(0,len(presentation)-1)])
    indiquer = True
    trouver = False
    while indiquer:
        main_reponse = input("Une recherche par 'nom' ou par 'type' ou 'stop' : ")  

        if main_reponse.lower() == 'stop':
            indiquer = False

        elif main_reponse.lower() == 'nom':
            print("D'accord. Veuillez m'indiquer le nom de l'endroit que vous recherchez s'il vous plait.")
            nom_place = input("Nom de l'endroit : ")
            # Fonction de recherche avec le nom
            # print("Y a  t-il des details que je dois connaitre sur l'endroit ?")
            # reponse = input("'Oui' ou 'Non' : ")
            
            # if reponse.lower() == 'oui':
            #     print("Dites les moi alors, vous avez une idée de sa localité ? Si oui, ecirvez le ou mettez juste 'Non'...")
            #     detail_localite = input("Je vous écoute: ")
                
            #     if detail_localite.lower() == 'non':
            #         detail_localite = None
                
            #     print("Savez-vous de quel genre d'endroit il s'agit  ? Si oui, ecirvez le ou mettez juste 'Non'...")
            #     detail_type = input("Je vous écoute: ")

            #     if detail_type.lower() == 'non':
            #         detail_type = None 
                
            # else:
            #     print("D'accord. J'effectue la recherche pour vous. Donnez moi quelques instants...")
            recherche_places_et_localites_par_nom(nom_place)
            
        elif main_reponse.lower() == 'type':

            print("D'accord. Dites moi quel genre d'endroit vous recherchez.")
            type_place = input("Type d'endroit : ")
            # print("Maintenant, j'aimerais savoir si vous le recherchez dans une zone donnée. Si oui, dites moi où.")
            # zone_recherche = input("Je vous écoute: ")

            matching_keywords = trouver_mot_cle(type_place)
            if matching_keywords:
                keyword = matching_keywords[0]
                mot_cle = trouver_mot_cle(keyword)
                # print("Correspondances trouvées : ", matching_keywords)
                # print("Correspondances trouvées : ", matching_keywords[0])
                recherche_autre_critere(keyword=keyword)
            else:
                print("Aucune correspondance trouvée.")
                matching_keywords = None

    print(au_revoir[random.randint(0,len(au_revoir)-1)])



