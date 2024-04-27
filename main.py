import random
import json

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

def traduire_amenity(amenity=None, tourism=None, shop=None, leisure=None):
    amenity_mapping = {
        "clinic": "une clinique",
        "bar": "un bar restaurant ou un maquis",
        "restaurant": "un bar restaurant ou un maquis",
        "pub": "un bar restaurant ou un maquis",
        "police": "un centre de police ou commissariat",
        "cafe": "un café",
        "kindergarten": "une école maternelle ou une crèche",
        "dentist": "un cabinet dentaire",
        "toilets": "une toilette",
        "airport": "un aéroport",
        "bank": "une banque",
        "atm": "une banque",
        "school": "une école, un collège ou une université",
        "college": "une école, un collège ou une université",
        "university": "une école, un collège ou une université",
        "pharmacy": "une pharmacie",
        "marketplace": "un marché",
        "cinema": "une salle de cinéma",
        "fast_food": "un fast food",
        "bus_station": "une station de bus",
        "bureau_de_change": "un bureau de change",
        "doctors": "un centre de santé",
        "library": "une librairie",
        "books": "une librairie",
        "hospital": "un centre de santé",
        "coworking_space": "un espace de co working",
        "townhall": "un hôtel de ville ou un bureau administratif",
        "place_of_worship": "une église, une mosquée ou un couvent"
    }

    tourism_mapping = {
        "hotel": "un hôtel",
        "guest_house": "un guest house",
        "apartment": "un appartement",
        "motel": "un motel"
    }

    leisure_mapping = {
        "park": "une place publique"
    }

    shop_mapping = {
        "kiosk": "un kiosque ou une boutique d'alimentation générale",
        "variety_store": "un kiosque ou une boutique d'alimentation générale",
        "electronique": "une boutique d'appareils élèctroniques",
        "hardware": "une boutique d'appareils élèctroniques",
        "clothes": "une boutique de vêtements ou un centre de couture",
        "optician": "une boutique de lunettes",
        "beverages": "une boutique de boissons",
        "massage": "un salon de massage",
        "pastry": "un patisserie",
        "cosmetics": "une boutique de produits cosmétiques",
        "boutique": "une boutique",
        "tyres": "une entreprise de vulcanisation",
        "sewing": "un magazin de mode",
        "beauty": "un institut de beauté",
        "pawnbroker": "un système financié",
        "medical_supply": "un soutien medical",
        "travel_agency": "une agence de voyage",
        "fabric": "un centre artisanal",
        "mobile_phone": "une boutique de téléphone",
        "car": "une entrepris d'automobile",
        "supermarket": "un super marché",
        "wine": "une boutique de vins",
        "dry_cleaning": "un pressing",
        "glazery": "une vitrerie",
        "jewlry": "une boutique de bijoux",
        "car_repair": "un garage automobile",
        "video_games": "une salle de jeux vidéos",
        "games": "une loterie",
        "copyshop": "un centre de photocopie",
        "estate_agent": "une agence immobilière",
        "seafood": "une poissonnerie"
    }

    if amenity:
        return amenity_mapping.get(amenity, "un type d'endroit encore inconnu pour moi")
    elif tourism:
        return tourism_mapping.get(tourism, "un type d'endroit encore inconnu pour moi")
    elif shop:
        return shop_mapping.get(shop, "un type d'endroit encore inconnu pour moi")
    elif leisure:
        return leisure_mapping.get(leisure, "un type d'endroit encore inconnu pour moi")
    else:
        return "un type d'endroit encore inconnu pour moi"

# Traduction tourism
# def traduire_tourism(tourism):
#     type = ""
#     return type

# Fonctions de sortie d'indication:
def recherche_place_specifique(place=None, amenity=None,arrondissement=None, location=None, tourism=None, shop=None, leisure=None):
    texte = "Désolé, mes informations sont limitées au le littoral du Bénin."
    type = traduire_amenity(amenity,tourism, shop, leisure)
    if (location==None and arrondissement!=None):
        texte = f"{place} est {type} situé dans le {arrondissement} dont je ne connais pas la localité"
    elif (location!=None and arrondissement!=None):
        texte = f"{place} est {type} situé dans le {arrondissement} et plus précisement dans la localité de {localité}"
    elif (arrondissement==None):
        texte = f"{place} est {type} non repertorié dans le littoral"
    else:
        texte = f"l'endroit {place} que vous recherchez m'est encore inconnu"
    return texte

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
                


