import json
from shapely.geometry import Point, shape, Polygon


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

# Demander à l'utilisateur le type d'endroit recherché
type_recherche = input("Entrez le type d'endroit que vous recherchez (amenity/shop/leisure) : ")

# Vérifier si le type de recherche correspond à l'un des mots-clés
type_trouve = False
for keyword, value in keywords.items():
    if type_recherche.lower() in [keyword.lower(), value.lower()]:
        type_recherche = keyword
        type_trouve = True
        break

if not type_trouve:
    print("Type d'endroit non pris en charge.")
else:
    # Stocker les places correspondant au type de recherche
    places_trouvees = []
    for feature in places_data['features']:
        if feature['properties'].get('amenity') == type_recherche:
            places_trouvees.append(feature)

    # Si aucune place n'est trouvée, afficher un message et terminer le programme
    if not places_trouvees:
        print("Aucune place correspondante n'a été trouvée.")
    else:
        # Demander à l'utilisateur la zone de recherche ou le numéro de l'arrondissement
        zone_recherche = input("Entrez le nom de la zone ou de la localité, ou un numéro d'arrondissement (entre 1 et 13) : ")

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
                    print("Arrondissement non trouvé.")
                else:
                    places_trouvees_dans_arrondissement = []
                    for place in places_trouvees:
                        place_geometry = shape(place['geometry'])
                        if isinstance(place_geometry, Point):
                            if arrondissement_shape.contains(place_geometry):
                                place_name = place['properties'].get('name')
                                if place_name is not None:  # Vérifier si le nom de la place n'est pas None
                                    places_trouvees_dans_arrondissement.append(place_name)
                        elif isinstance(place_geometry, Polygon):
                            if arrondissement_shape.intersects(place_geometry):
                                place_name = place['properties'].get('name')
                                if place_name is not None:  # Vérifier si le nom de la place n'est pas None
                                    places_trouvees_dans_arrondissement.append(place_name)

                    if places_trouvees_dans_arrondissement:
                        print("\nPlaces trouvées dans l'arrondissement :")
                        for place in places_trouvees_dans_arrondissement:
                            print(place)
                    else:
                        print(arrondissement_info)
                        print("Aucune place trouvée dans cet arrondissement.")

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
                    