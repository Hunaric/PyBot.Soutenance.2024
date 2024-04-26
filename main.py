# Ici sont repertoriés les variables phrases:
presentation = [
    "Bonjour, je suis GeoLocate, votre assistant vocal directionnel. En quoi puis-je vous aider ?",
    "Hello! Ici GeoLocate pour vous aider. De quelle information avez vous besoin ?",
    "Bonjour, vous. Moi c'est GeoLocate, votre guide. Comment puis-je vous aider ?",
    "Cher ami, bonjour. En quoi puis-je vous aider ?",
    "Salutation a vous. De quoi avez vous beosin ?"
]

# Traduction des amenity
def traduire_amenity(amenity=null, tourism=null, shop=null, leisure=null):
    type = ""
    if amenity == "clinic":
        type = "une clinique"
    elif amenity == "bar" or amenity == "restaurant" or amenity == "pub":
        type = "un bar restaurant ou un maquis"
    elif amenity == "police":
        type = "un centre de police ou commissariat"
    elif amenity == "cafe":
        type = "un café"
    elif amenity == "kindergarten":
        type = "une école maternelle ou une crèche"
    elif amenity == "dentist":
        type = "un cabinet dentaire"
    elif amenity == "toilets":
        type = "une toilette"
    elif amenity == "airport":
        type = "un aéroport"
    elif amenity == "bank" or amenity == "atm":
        type = "une banque"
    elif amenity == "school" or amenity == "college" or "university":
        type = "une école, un collège ou une université"
    elif amenity == "pharmacy":
        type = "une pharmacie"
    elif amenity == "marketplace":
        type = "un marché"
    elif amenity == "marketplace":
        type = "un marché"
    elif amenity == "cinema":
        type = "une salle de cinéma"
    elif amenity == "fast_food":
        type = "un fast food"
    elif amenity == "bus_station":
        type = "une station de bus"
    elif amenity == "bureau_de_change":
        type = "un bureau de change"
    elif amenity == "doctors":
        type = "un centre de santé"
    elif amenity == "library" or shop == "books":
        type = "une librairie"
    elif amenity == "hospital":
        type = "un centre de santé"
    elif amenity == "coworking_space":
        type = "un espace de co working"
    elif amenity == "townhall":
        type = "un hôtel de ville ou un bureau administratif"
    elif amenity == "place_of_worship":
        type = "un lieu de culte traditionel, chrétien ou musulman"
    elif tourism == "hotel":
        type = "un hotel"
    elif tourism == "guest_house":
        type = "un guest house"
    elif tourism == "apartment":
        type = "un appartememnt"
    elif tourism == "motel":
        type = "un motel"
    elif leisure == "park":
        type = "une place publique"
    elif shop == "kiosk" or shop == "variety_store":
        type = "un kiosque ou une boutique d'alimentation générale"
    elif shop == "electronique" or shop == "hardware":
        type = "une boutique d'appareils élèctroniques"
    elif shop == "clothes":
        type = "une boutique de vêtements ou un centre de couture"
    elif shop == "optician":
        type = "une boutique de lunettes"
    elif shop == "beverages":
        type = "une boutique de boissons"
    elif shop == "massage":
        type = "un salon de massage"
    elif shop == "pastry":
        type = "un patisserie"
    elif shop == "cosmetics":
        type = "une boutique de produits cosmétiques"
    elif shop == "boutique":
        type = "une boutique"
    elif shop == "tyres":
        type = "une entreprise de vulcanisation"
    elif shop == "sewing":
        type = "un magazin de mode"
    elif shop == "beauty":
        type = "un institut de beauté"
    elif shop == "pawnbroker":
        type = "un système financié"
    elif shop == "medical_supply":
        type = "un soutien medical"
    elif shop == "travel_agency":
        type = "une agence de voyage"
    elif shop == "fabric":
        type = "un centre artisanal"
    elif shop == "mobile_phone":
        type = "une boutique de téléphone"
    elif shop == "car":
        type = "une entrepris d'automobile"
    elif shop == "supermarket":
        type = "un super marché"
    elif shop == "wine":
        type = "une boutique de vins"
    elif shop == "dry_cleaning":
        type = "un pressing"
    elif shop == "glazery":
        type = "une vitrerie"
    elif shop == "jewlry":
        type = "une boutique de bijoux"
    elif shop == "car_repair":
        type = "un garage automobile"
    elif shop == "video_games":
        type = "une salle de jeux vidéos"
    elif shop == "games":
        type = "une loterie"
    elif shop == "copyshop":
        type = "un centre de photocopie"
    elif shop == "estate_agent":
        type = "une agence immobilière"
    elif shop == "seafood":
        type = "une poissonnerie"
    else:
        type = "un type d'endroit encore inconnu pour moi"
    return type

# Traduction tourism
# def traduire_tourism(tourism):
#     type = ""
#     return type

# Fonctions de sortie d'indication:
def recherche_place_specifique(place=null, amenity=null,arrondissement=null, location=null, tourism=null, shop=null, leisure=null):
    texte = "Désolé, mes informations sont limitées au le littoral du Bénin."
    type = traduire_amenity(amenity,tourism, shop, leisure)
    if (location==null and arrondissement!=null):
        texte = f"{place} est {type} situé dans le {arrondissement} dont je ne connais pas la localité"
    elif (location!=null and arrondissement!=null):
        texte = f"{place} est {type} situé dans le {arrondissement} et plus précisement dans la localité de {localité}"
    elif (arrondissement==null):
        texte = f"{place} est {type} non repertorié dans le littoral"
    else:
        texte = f"l'endroit {place} que vous recherchez m'est encore inconnu"
    return texte


