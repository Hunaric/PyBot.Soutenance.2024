import json
from shapely.geometry import Point
from localite_plus_proche import *
from lieu_plus_proche import *
from geopy.distance import geodesic


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
        nom_place, amenity_place, arrondissement_place, localite_place, tourism_place, shop_place, leisure_place = None
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

                        # Extraire les coordonnées de la place
                        coordinates = place['geometry']['coordinates']
                        # Si les coordonnées sont sous forme de liste imbriquée, choisir le premier point
                        if isinstance(coordinates[0], list):
                            coordinates = coordinates[0][0]  # Choisir le premier point de la liste
                        
                        # Créer un point avec les coordonnées de la place
                        place_point = Point(coordinates)

            
                        # Chercher la localité la plus proche de la place
                        localite_proche = trouver_localite_proche(place_point)
                        if not localite_proche.empty:  # Check if localite_proche is not empty
                            localite = localite_proche["nom_loc"].values[0]
                            arrondissement = localite_proche["arrondisst"].values[0]
                            commune = localite_proche["commune"].values[0]
                        else:
                            print("Aucune localité trouvée à proximité de la place.")
            
        #     # Chercher le type de place le plus proche
        #     type_de_place_proche, nom_de_place_proche = trouver_place_proche(place_point, places_data)
        #     if type_de_place_proche:
        #         print("\nPlace de type le plus proche :")
        #         print("Type:", type_de_place_proche)
        #         if nom_de_place_proche:
        #             print("Nom:", nom_de_place_proche)
        #         else:
        #             print("Nom: Aucun nom disponible")
        #     else:
        #         print("Aucune place de type recherché trouvée à proximité de la place.")
            
        #     # Trouver la distance entre la place recherchée et la place la plus proche
        #     distance = geodesic((coordinates[1], coordinates[0]), (localite_proche.geometry.y.values[0], localite_proche.geometry.x.values[0])).meters
        #     print("\nDistance entre la place recherchée et la place la plus proche:", round(distance, 2), "mètres")
            
    #         print("---------------------------------------------")
    # else:
    #     print("Aucune place correspondant à la recherche n'a été trouvée.")
                    
                        # Mettre le code de retour de recherche 
                        break
                    else:
                        print("Numéro d'endroit invalide.")
                except ValueError:
                    print("Veuillez entrer un numéro valide.")
    else:
        print("Aucun lieu trouvé pour la recherche spécifiée.")





recherche_places_et_localites_par_nom()