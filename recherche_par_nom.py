import json
from voice_engine import say, say_only
from geopy.distance import geodesic
from shapely.geometry import Point
from localite_plus_proche import trouver_localite_proche
from lieu_plus_proche import *
from fonctions_geo import *
from matching_keyword import replace_values_with_keys


# Charger le fichier GeoJSON des places
with open('data/places.geojson', encoding='utf-8') as f:
    places_data = json.load(f)

# Fonction pour rechercher une place et afficher sa localité la plus proche
def recherche_places_et_localites_par_nom(nom_recherche):
    # Demander le nom à rechercher à l'utilisateur
    # nom_recherche = input("Entrez le nom de la place à rechercher : ")

    # Liste pour stocker les détails de toutes les places trouvées
    places_trouvees = []

    # Parcourir les features des places
    for feature in places_data['features']:
        # Vérifier si le nom recherché est dans les propriétés "name" ou "operator"
        if feature['properties'].get('name') and nom_recherche.lower() in feature['properties']['name'].lower():
            places_trouvees.append(feature)

    # Si des places sont trouvées
    if places_trouvees:
        nom_place, amenity_place, arrondissement_place, localite_place, tourism_place, shop_place, leisure_place = None, None, None, None, None, None, None
        say(f"\nJ'ai trouvé {len(places_trouvees)} lieux: ")
        
        # Afficher les lieux trouvés avec un numéro d'index
        for i, place in enumerate(places_trouvees):
            response = f"{i+1}. {place['properties']['name']}"
            print(response)
            response_fon = replace_values_with_keys(response)
            say_only(response_fon)


        while True:

            if len(places_trouvees) == 1:
    
                say("\nPropriétés de l'endroit trouvé :")
                selected_place = places_trouvees[0]
                nom_place = selected_place["properties"]["name"]
                if 'amenity' in selected_place["properties"]:
                    amenity_place = selected_place["properties"]["amenity"]
                else:
                    amenity_place = None

                if 'tourism' in selected_place["properties"]:
                    tourism_place = selected_place["properties"]["tourism"]
                else:
                    tourism_place = None

                if 'shop' in selected_place["properties"]:
                    shop_place = selected_place["properties"]["shop"]
                else:
                    shop_place = None

                if 'leisure' in selected_place["properties"]:
                    leisure_place = selected_place["properties"]["leisure"]
                else:
                    leisure_place = None


                # Extraire les coordonnées de la place
                coordinates = selected_place['geometry']['coordinates']            
                # Si les coordonnées sont sous forme de liste imbriquée, choisir le premier couple de points du premier polygone
                if isinstance(coordinates[0], list) and len(coordinates[0]) >= 2:
                    # Vérifier si coordinates[0] contient au moins deux éléments
                    if len(coordinates[0]) >= 2:
                        coordinates = coordinates[0]  # Utiliser le premier couple de points du premier polygone
                longitude, latitude = coordinates[0], coordinates[1]

                if isinstance(longitude, list):
                    # Si longitude ou latitude n'est pas un float, prendre le premier élément de chaque liste
                        coordinates = longitude
                        longitude = coordinates[0]
                        latitude = coordinates[1]
                        
                # Créer un objet Point à partir des coordonnées
                place_point = Point(longitude, latitude)
                # Chercher la localité la plus proche de la place
                localite_proche = trouver_localite_proche(place_point)
                if not localite_proche.empty:  # Check if localite_proche is not empty
                    localite_place = localite_proche["nom_loc"].values[0]
                    arrondissement_place = localite_proche["arrondisst"].values[0]
                    commune_place = localite_proche["commune"].values[0]
                    resultat = retour_de_recherche(place=nom_place, amenity=amenity_place, arrondissement=arrondissement_place, localite=localite_place, tourism=tourism_place, shop=shop_place, leisure=leisure_place)
                    resultat_fon = replace_values_with_keys(resultat)
                    print(resultat)
                    say_only(resultat_fon)
                    # Chercher le type de place le plus proche
                    type_de_place_proche, nom_de_place_proche, localisation_de_la_place = trouver_place_proche(place_point, places_data)

                    if type_de_place_proche:
                        distance = geodesic((coordinates[1], coordinates[0]), (localisation_de_la_place[1], localisation_de_la_place[0])).meters
                        type_traduit = traduire_type(type_de_place_proche)

                        if nom_de_place_proche:
                            # say("Nom:", nom_de_place_proche)
                            info = f"A {round(distance, 2)} mètres de là se trouve {type_traduit} nommé {nom_de_place_proche}"
                            info_fon = replace_values_with_keys(info)
                            print(info)
                            say_only(info_fon)
                        else:
                            info = f"A {round(distance, 2)} mètres de là se trouve {type_traduit} dont le nom m'est encore inconnu"
                            print(info)
                            info_fon = replace_values_with_keys(info)
                            say_only(info_fon)
                            
                    else:
                        say("Aucune place de type recherché trouvée à proximité de la place.")
                    
                else:
                    say("Aucune localité trouvée à proximité de la place. Peut-etre qu'elle ne se retrouve pas dans le littoral ou que vous m'ayew mal renseigné le nom.")
    
            
                # Mettre le code de retour de recherche 
                break
            else:
                # Demander à l'utilisateur de choisir un endroit
                texte = "Entrez le numéro de l'endroit que vous souhaitez sélectionner (ou 'stop' pour arrêter) : "
                say(texte)
                choix = input()

                if choix.lower() == 'stop':
                    say("J'arrete cette recherche.")
                    return
                else:
                    try:
                        choix = int(choix)
                        if 0 < choix <= len(places_trouvees):
                            # Afficher les propriétés de l'endroit sélectionné
                            selected_place = places_trouvees[choix - 1]
                            say("\nPropriétés de l'endroit sélectionné :")
                            nom_place = selected_place["properties"]["name"]
                            if 'amenity' in selected_place["properties"]:
                                amenity_place = selected_place["properties"]["amenity"]
                            else:
                                amenity_place = None

                            if 'tourism' in selected_place["properties"]:
                                tourism_place = selected_place["properties"]["tourism"]
                            else:
                                tourism_place = None

                            if 'shop' in selected_place["properties"]:
                                shop_place = selected_place["properties"]["shop"]
                            else:
                                shop_place = None

                            if 'leisure' in selected_place["properties"]:
                                leisure_place = selected_place["properties"]["leisure"]
                            else:
                                leisure_place = None


                            # Extraire les coordonnées de la place
                            coordinates = selected_place['geometry']['coordinates']            
                            # Si les coordonnées sont sous forme de liste imbriquée, choisir le premier couple de points du premier polygone
                            if isinstance(coordinates[0], list) and len(coordinates[0]) >= 2:
                                # Vérifier si coordinates[0] contient au moins deux éléments
                                if len(coordinates[0]) >= 2:
                                    coordinates = coordinates[0]  # Utiliser le premier couple de points du premier polygone
                            longitude, latitude = coordinates[0], coordinates[1]

                            if isinstance(longitude, list):
                                # Si longitude ou latitude n'est pas un float, prendre le premier élément de chaque liste
                                    coordinates = longitude
                                    longitude = coordinates[0]
                                    latitude = coordinates[1]
                                    
                            # Créer un objet Point à partir des coordonnées
                            place_point = Point(longitude, latitude)
                            # Chercher la localité la plus proche de la place
                            localite_proche = trouver_localite_proche(place_point)
                            if not localite_proche.empty:  # Check if localite_proche is not empty
                                localite_place = localite_proche["nom_loc"].values[0]
                                arrondissement_place = localite_proche["arrondisst"].values[0]
                                commune_place = localite_proche["commune"].values[0]
                                resultat = retour_de_recherche(place=nom_place, amenity=amenity_place, arrondissement=arrondissement_place, localite=localite_place, tourism=tourism_place, shop=shop_place, leisure=leisure_place)
                                resultat_fon = replace_values_with_keys(resultat)
                                print(resultat)
                                say_only(resultat_fon)
                                # Chercher le type de place le plus proche
                                type_de_place_proche, nom_de_place_proche, localisation_de_la_place = trouver_place_proche(place_point, places_data)

                                if type_de_place_proche:
                                    distance = geodesic((coordinates[1], coordinates[0]), (localisation_de_la_place[1], localisation_de_la_place[0])).meters
                                    type_traduit = traduire_type(type_de_place_proche)

                                    if nom_de_place_proche:
                                        # say("Nom:", nom_de_place_proche)
                                        info = f"A {round(distance, 2)} mètres de là se trouve {type_traduit} nommé {nom_de_place_proche}"
                                        info_fon = replace_values_with_keys(info)
                                        print(info)
                                        say_only(info_fon)
                                    else:
                                        info = f"A {round(distance, 2)} mètres de là se trouve {type_traduit} dont le nom m'est encore inconnu"
                                        print(info)
                                        info_fon = replace_values_with_keys(info)
                                        say_only(info_fon)
                                        
                                else:
                                    say("Aucune place de type recherché trouvée à proximité de la place.")
                                
                            else:
                                say("Aucune localité trouvée à proximité de la place. Peut-etre qu'elle ne se retrouve pas dans le littoral ou que vous m'ayew mal renseigné le nom.")
                
                        
                            # Mettre le code de retour de recherche 
                            break
                        else:
                            say("Numéro d'endroit invalide.")
                    except ValueError:
                        say("Veuillez entrer un numéro valide.")
    else:
        say("Aucun lieu trouvé pour la recherche spécifiée.")