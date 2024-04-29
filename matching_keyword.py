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
        # Parcourir les éléments du dictionnaire keywords
        for key, values in keywords.items():
            # Vérifier si le mot est présent dans les valeurs associées à la clé
            if mot in values:
                matches.append(key)
                break  # Sortir de la boucle interne si une correspondance est trouvée
    
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