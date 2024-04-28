import json
from shapely.geometry import Point
from localite_plus_proche import *
from lieu_plus_proche import *
from geopy.distance import geodesic
from fonctions_geo import *


# Charger le fichier GeoJSON des places
with open('data/places.geojson', encoding='utf-8') as f:
    places_data = json.load(f)

# Fonction pour rechercher une place et afficher sa localité la plus proche
def recherche_places_et_localites_par_nom():
    # Demander le nom à rechercher à l'utilisateur
    nom_recherche = input("Entrez le nom de la place à rechercher : ")

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
        print(f"\nJ'ai trouvé {len(places_trouvees)} lieux: ")
        
        # Afficher les lieux trouvés avec un numéro d'index
        for i, place in enumerate(places_trouvees):
            print(f"{i+1}. {place['properties']['name']}")


        while True:
            # Demander à l'utilisateur de choisir un endroit
            choix = input("\nEntrez le numéro de l'endroit que vous souhaitez sélectionner (ou 'stop' pour arrêter) : ")

            if choix.lower() == 'stop':
                print("J'arrete cette recherche.")
                return
            else:
                try:
                    choix = int(choix)
                    if 0 < choix <= len(places_trouvees):
                        # Afficher les propriétés de l'endroit sélectionné
                        selected_place = places_trouvees[choix - 1]
                        print("\nPropriétés de l'endroit sélectionné :")
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
                        # Si les coordonnées sont sous forme de liste imbriquée, choisir le premier point
                        if isinstance(coordinates[0], list):
                            coordinates = coordinates[0][0]  # Choisir le premier point de la liste
                        
                        # Créer un point avec les coordonnées de la place
                        place_point = Point(coordinates)

            
                        # Chercher la localité la plus proche de la place
                        localite_proche = trouver_localite_proche(place_point)
                        if not localite_proche.empty:  # Check if localite_proche is not empty
                            localite_place = localite_proche["nom_loc"].values[0]
                            arrondissement_place = localite_proche["arrondisst"].values[0]
                            commune_place = localite_proche["commune"].values[0]
                            resultat = retour_de_recherche(place=nom_place, amenity=amenity_place, arrondissement=arrondissement_place, 
                            localite=localite_place, tourism=tourism_place, shop=shop_place, leisure=leisure_place)
                            print(resultat)
                            # Chercher le type de place le plus proche
                            type_de_place_proche, nom_de_place_proche, localisation_de_la_place = trouver_place_proche(place_point, places_data)

                            if type_de_place_proche:
                                distance = geodesic((coordinates[1], coordinates[0]), (localisation_de_la_place[1], localisation_de_la_place[0])).meters
                                type_traduit = traduire_type(type_de_place_proche)

                                if nom_de_place_proche:
                                    print("Nom:", nom_de_place_proche)
                                    print(f"A {round(distance, 2)} mètres de là se trouve {type_traduit} nommé {nom_de_place_proche}")
                                else:
                                    print(f"A {round(distance, 2)} mètres de là se trouve {type_traduit} dont le nom m'est encore inconnu")
                                    
                            else:
                                print("Aucune place de type recherché trouvée à proximité de la place.")
                            
                        else:
                            print("Aucune localité trouvée à proximité de la place. Peut-etre qu'elle ne se retrouve pas dans le littoral ou que vous m'ayew mal renseigné le nom.")
            
                    
                        # Mettre le code de retour de recherche 
                        break
                    else:
                        print("Numéro d'endroit invalide.")
                except ValueError:
                    print("Veuillez entrer un numéro valide.")
    else:
        print("Aucun lieu trouvé pour la recherche spécifiée.")





# recherche_places_et_localites_par_nom()