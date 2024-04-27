# Fonction de retour sur place recherchée
def retour_de_recherche(place=None, amenity=None,arrondissement=None, localite=None, tourism=None, shop=None, leisure=None):
    texte = "Désolé, mes informations sont limitées au le littoral du Bénin."
    type = traduire_type(amenity,tourism, shop, leisure)
    if (localite==None and arrondissement!=None):
        texte = f"{place} est {type} situé dans le {arrondissement} dont je ne connais pas la localité"
    elif (localite!=None and arrondissement!=None):
        texte = f"{place} est {type} situé dans le {arrondissement} et plus précisement dans la localité de {localite}"
    elif (arrondissement==None):
        texte = f"{place} est {type} non repertorié dans le littoral"
    else:
        texte = f"l'endroit {place} que vous recherchez m'est encore inconnu"
    return texte


# Fonctions necesaires a la traduction des types de données
def traduire_type(amenity=None, tourism=None, shop=None, leisure=None):
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

# a = traduire_type(, None, 'park')
# print(a)