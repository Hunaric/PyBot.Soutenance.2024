import random
import json
from fonctions_geo import *

# Ici sont repertoriés les variables phrases:
presentation = [
    "Bonjour, je suis GéoLocate, votre assistant vocal directionnel. En quoi puis-je vous aider ?",
    "Hello! Ici GéoLocate pour vous aider. De quelle information avez vous besoin ?",
    "Bonjour, vous. Moi c'est GéoLocate, votre guide. Comment puis-je vous aider ?",
    "Cher ami, bonjour. En quoi puis-je vous aider ?",
    "Salutation a vous. De quoi avez vous beosin ?"
]

au_revoir = [
    "Au revorir et a bientôt",
]

def trouver_mot_cle(mot_donne):
    # Diviser l'entrée de l'utilisateur en mots
    chaque_mot = mot_donne.lower().split()
    
    # Liste pour stocker les correspondances trouvées
    matches = []
    
    # Parcourir chaque mot de l'entrée de l'utilisateur
    for mot in chaque_mot:
        # Vérifier si le mot correspond à une clé dans le fichier keyword.txt
        if mot in keywords.values():
            # Trouver la clé correspondante au mot
            matching_key = [key for key, value in keywords.items() if value == mot][0]
            matches.append(matching_key)
    
    return matches

if __name__ == '__main__':
    # Accueil et presentation
    # print(presentation[random.randint(0,len(presentation)-1)])
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
            print("Y a  t-il des details que je dois connaitre sur l'endroit ?")
            reponse = input("'Oui' ou 'Non' : ")
            
            if reponse.lower() == 'oui':
                print("Dites les moi alors, vous avez une idée de sa localité ? Si oui, ecirvez le ou mettez juste 'Non'...")
                detail_localite = input("Je vous écoute: ")
                
                if detail_localite.lower() == 'non':
                    detail_localite = None
                
                print("Savez-vous de quel genre d'endroit il s'agit  ? Si oui, ecirvez le ou mettez juste 'Non'...")
                detail_type = input("Je vous écoute: ")

                if detail_type.lower() == 'non':
                    detail_type = None 
                

            else:
                print("D'accord. J'effectue la recherche pour vous. Donnez moi quelques instants...")
            
        elif main_reponse.lower() == 'type':
            # Charger le fichier keyword.txt
            with open('keywords.txt', 'r', encoding='utf-8') as file:
                keywords = json.load(file)

            print("D'accord. Dites moi quel genre d'endroit vous recherchez.")
            type_place = input("Type d'endroit : ")
            # print("Maintenant, j'aimerais savoir si vous le recherchez dans une zone donnée. Si oui, dites moi où.")
            # zone_recherche = input("Je vous écoute: ")

            matching_keywords = trouver_mot_cle(type_place)
            if matching_keywords:
                print("Correspondances trouvées : ", matching_keywords)
            else:
                print("Aucune correspondance trouvée.")
                matching_keywords = None



