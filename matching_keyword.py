import json


# Charger le fichier keyword.txt
with open('keywords.txt', 'r', encoding='utf-8') as file:
    keywords = json.load(file)

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

def inverse_mot_cle(valeur_donnee):
    # Parcourir les éléments du dictionnaire keywords
    for cle, valeur in keywords.items():
        # Vérifier si la valeur donnée correspond à la valeur actuelle du dictionnaire
        if cle == valeur_donnee:
            # Retourner la clé correspondante
            return valeur
    # Si aucune correspondance n'est trouvée, retourner None
    return None