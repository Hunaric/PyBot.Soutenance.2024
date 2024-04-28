import json
from shapely.geometry import Point, shape, Polygon
from matching_keyword import *
from fonctions_geo import traduire_type
from localite_plus_proche import trouver_localite_proche


# Charger le fichier GeoJSON des endroits
with open('C:/Users/LENOVO/Downloads/Data/Propre/allplace.geojson', encoding="utf-8") as f:
    places_data = json.load(f)

# Charger le fichier GeoJSON des localités
with open('C:/Users/LENOVO/Downloads/Data/Propre/localite_copy.geojson', encoding="utf-8") as f:
    localite_data = json.load(f)

# Charger le fichier GeoJSON des arrondissements
with open('C:/Users/LENOVO/Downloads/Data/Propre/ctn_arrondissements.geojson', encoding="utf-8") as f:
    arrondissement_data = json.load(f)
    
# Charger les mots-clés à partir du fichier keywords.txt
with open('C:/Users/LENOVO/Desktop/PyBot/keywords.txt', 'r') as f:
    keywords = json.load(f)
    

def recherche_autre_critere(keyword):
    mot_cle = inverse_mot_cle(keyword)
    # Stocker les places correspondant au type de recherche
    places_trouvees = []
    for feature in places_data['features']:
        if feature['properties'].get('amenity') == keyword:
            places_trouvees.append(feature)

    # Si aucune place n'est trouvée, afficher un message et terminer le programme
    if not places_trouvees:
        print("Aucune place correspondante n'a été trouvée.")
    else:
        # Demander à l'utilisateur la zone de recherche ou le numéro de l'arrondissement
        zone_recherche = input("Dites soit le nom de la zone ou de la localité, soit le numéro d'arrondissement (entre 1 et 13) : ")

        # Recherche par arrondissement si l'entrée est un numéro
        if zone_recherche.isdigit():
            num_arrondissement = int(zone_recherche)
            if num_arrondissement < 1 or num_arrondissement > 13:
                print("Numéro d'arrondissement invalide.")
            else:
                arrondissement_trouve = False
                for feature in arrondissement_data['features']:
                    arrondissement_name = feature['properties']['arrond']
                    arrondissement_number = int(''.join(filter(str.isdigit, arrondissement_name)))  # Extraire le nombre d'arrondissement
                    if arrondissement_number == num_arrondissement:
                        arrondissement_shape = shape(feature['geometry'])
                        arrondissement_info = feature['properties']
                        arrondissement_trouve = True
                        break

                if not arrondissement_trouve:
                    print("Aucun arrondissement ne correspond a cette valeur.")
                else:
                    places_trouvees_dans_arrondissement = []
                    for place in places_trouvees:
                        place_geometry = shape(place['geometry'])
                        if isinstance(place_geometry, Point):
                            if arrondissement_shape.contains(place_geometry):
                                place_name = place['properties'].get('name')
                                if place_name is not None:  # Vérifier si le nom de la place n'est pas None
                                    places_trouvees_dans_arrondissement.append(place)
                        elif isinstance(place_geometry, Polygon):
                            if arrondissement_shape.intersects(place_geometry):
                                place_name = place['properties'].get('name')
                                if place_name is not None:  # Vérifier si le nom de la place n'est pas None
                                    places_trouvees_dans_arrondissement.append(place)

                    if places_trouvees_dans_arrondissement:                            
                        # Initialisation des types:
                        if 'amenity' in place["properties"]:
                            amenity_place = place["properties"]["amenity"]
                        else:
                            amenity_place = None

                        if 'tourism' in place["properties"]:
                            tourism_place = place["properties"]["tourism"]
                        else:
                            tourism_place = None

                        if 'shop' in place["properties"]:
                            shop_place = place["properties"]["shop"]
                        else:
                            shop_place = None

                        if 'leisure' in place["properties"]:
                            leisure_place = place["properties"]["leisure"]
                        else:
                            leisure_place = None

                        type_final = traduire_type(amenity=amenity_place, tourism=tourism_place, shop=shop_place, leisure=leisure_place)

                        print(f"\nJ'ai trouvé {len(places_trouvees_dans_arrondissement)} {mot_cle} dans le {arrondissement_name} :")
                        for place in places_trouvees_dans_arrondissement:
                            coordinates = place['geometry'].get('coordinates')
                            if isinstance(coordinates[0], list):
                                coordinates = coordinates[0][0]  # Choisir le premier point de la liste
                                
                            # Créer un point avec les coordonnées de la place
                            place_point = Point(coordinates)
                            localite_proche = trouver_localite_proche(place_point)

                            if not localite_proche.empty:  # Check if localite_proche is not empty
                                localite_place = localite_proche["nom_loc"].values[0]
                                print(f"J'ai retrouvé {type_final} qui a pour nom {place['properties']['name']} et qui se retouve a {localite_place}")
                            else:
                                print(f"J'ai retrouvé {type_final} qui a pour nom {place['properties']['name']}")
                            # print(coordinates)
                            # print(place['geometry'].get('coordinates'))
                    else:
                        # print(arrondissement_info)
                        print(f"Aucun endoit du type {mot_cle} trouvée dans le {arrondissement_name}.")

        else:
            # Recherche par localité
            min_distance = float('inf')
            localites_trouvees = []
            for feature in localite_data['features']:
                if feature['properties']['nom_loc'].lower().startswith(zone_recherche.lower()):
                    localite_shape = shape(feature['geometry'])
                    localites_trouvees.append((feature['properties']['nom_loc'], localite_shape))

            if not localites_trouvees:
                print("Aucune localité correspondante n'a été trouvée.")
            else:
                for localite_name, localite_shape in localites_trouvees:
                    places_proches = []
                    localite_point = localite_shape.centroid  # Utiliser le point central de la localité
                    for place in places_trouvees:
                        place_geometry = shape(place['geometry'])
                        place_name = place['properties'].get('name')  # Obtenir le nom de la place
                        if place_name is not None:  # Vérifier si le nom de la place n'est pas None
                            if isinstance(place_geometry, Point):  # Vérifier si c'est un point
                                distance = localite_point.distance(place_geometry)  # Calculer la distance à partir du point central de la localité
                                distance_meter = distance * 1000
                            elif isinstance(place_geometry, Polygon):  # Si c'est un polygone, utiliser le point central du polygone
                                exterior_point = Point(place_geometry.exterior.coords[0])
                                distance = localite_point.distance(exterior_point)

                            if distance <= 2000:  # Vérifier si l'école est dans un rayon de 2 km
                                places_proches.append((place_name, distance, distance_meter))

                    if places_proches:
                        places_proches.sort(key=lambda x: x[1])  # Trier par distance
                        print(f"\nÉcoles trouvées dans la localité '{localite_name}' :")
                        for place, distance, meter in places_proches[:5]:
                            print(f"{place} - Distance : {meter:.2f} mètres")
                    else:
                        print(f"Aucune école trouvée dans la localité '{localite_name}' dans le rayon spécifié.")
                    