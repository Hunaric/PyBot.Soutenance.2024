import json
import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import nearest_points
from shapely.ops import transform
import pyproj
from geopy.distance import geodesic

# Charger le fichier GeoJSON des places
with open('data/places.geojson') as f:
    places_data = json.load(f)

# Charger le fichier GeoJSON des localités
localite_copy_gdf = gpd.read_file("data/localites.geojson")

# Liste des types de places à rechercher
types_de_places = ["bank", "pharmacy", "school", "police", "clinic", "restaurant"]

def trouver_type_de_place_proche(point):
    # Initialize the minimum distance and the nearest place type
    min_distance = float('inf')
    nearest_place_type = None
    nearest_place_name = None

    # Iterate over the features in the places data
    for feature in places_data['features']:
        # Check if the feature has an 'amenity' property and it's in the list of types to search
        if feature['properties'].get('amenity') in types_de_places:
            # Extract the coordinates of the feature
            coordinates = feature['geometry']['coordinates']
            # If the coordinates are a list of lists, choose the first point
            if isinstance(coordinates[0], list):
                coordinates = coordinates[0][0]
            # Create a point from the coordinates
            feature_point = Point(coordinates)
            # Calculate the distance between the point and the feature point
            distance = point.distance(feature_point)
            # Check if the distance is less than the minimum distance
            if distance < min_distance and distance != 0:  # Avoid considering the point itself as the nearest
                # Update the minimum distance and the nearest place type
                min_distance = distance
                nearest_place_type = feature['properties']['amenity']
                nearest_place_name = feature['properties'].get('name', 'Unnamed')  # Default to 'Unnamed' if name is None

    # Return the nearest place type and name
    return nearest_place_type, nearest_place_name


# Fonction pour rechercher une place et afficher sa localité la plus proche
def recherche_places_et_localites():
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
        print("\nPlaces trouvées :")
        for place in places_trouvees:
            print("\nDétails de la place:")
            for key, value in place['properties'].items():
                # Vérifier si la valeur n'est pas None avant de l'afficher
                if value is not None:
                    print(f"{key}: {value}")
            print("Type:", place['geometry']['type'])
            print("Coordonnées:", place['geometry']['coordinates'])

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
                print("\nLocalité la plus proche de la place :")
                print("Nom de la localité:", localite_proche["nom_loc"].values[0])
                print("Arrondissement:", localite_proche["arrondisst"].values[0])
                print("Commune:", localite_proche["commune"].values[0])
            else:
                print("Aucune localité trouvée à proximité de la place.")
            
            # Chercher le type de place le plus proche
            type_de_place_proche, nom_de_place_proche = trouver_type_de_place_proche(place_point)
            if type_de_place_proche:
                print("\nPlace de type le plus proche :")
                print("Type:", type_de_place_proche)
                if nom_de_place_proche:
                    print("Nom:", nom_de_place_proche)
                else:
                    print("Nom: Aucun nom disponible")
            else:
                print("Aucune place de type recherché trouvée à proximité de la place.")
            
            # Trouver la distance entre la place recherchée et la place la plus proche
            distance = geodesic((coordinates[1], coordinates[0]), (localite_proche.geometry.y.values[0], localite_proche.geometry.x.values[0])).meters
            print("\nDistance entre la place recherchée et la place la plus proche:", round(distance, 2), "mètres")
            
            print("---------------------------------------------")
    else:
        print("Aucune place correspondant à la recherche n'a été trouvée.")


# Fonction pour trouver la localité la plus proche d'un point avec une zone tampon étendue
# def trouver_localite_proche(point):
#     # Initialiser le rayon minimal de la zone tampon à 50m
#     rayon_minimal = 50  # en mètres

#     # Définir le rayon maximal de la zone tampon à 700m
#     rayon_maximal = 700  # en mètres

#     # Convertir les distances de mètres en degrés (approximatif)
#     # Approximation basée sur une longitude moyenne pour l'emplacement d'intérêt
#     conversion_degrees_per_meter = 1 / 111000  # Approximation moyenne
    
#     rayon_minimal_deg = rayon_minimal * conversion_degrees_per_meter
#     rayon_maximal_deg = rayon_maximal * conversion_degrees_per_meter

#     # Créer une fonction de projection pour calculer la zone tampon en mètres
#     project = pyproj.Transformer.from_proj(
#         pyproj.Proj(init='epsg:4326'),  # WGS84
#         pyproj.Proj(proj='aea', lat_1=point.y-rayon_maximal_deg, lat_2=point.y+rayon_maximal_deg),  # Albers Equal Area
#         always_xy=True)

#     # Fonction pour projeter les coordonnées en mètres
#     def project_point(x, y):
#         return project.transform(x, y)

#     # Créer un point projeté
#     projected_point = transform(project_point, point)

#     # Créer des zones tampons circulaires autour du point projeté avec des rayons min et max
#     buffered_points = [
#         projected_point.buffer(rayon_minimal),
#         projected_point.buffer(rayon_maximal)
#     ]

#     # Convertir les zones tampons en degrés
#     def unproject_point(x, y):
#         return project.transform(x, y, inverse=True)

#     unprojected_buffers = [transform(unproject_point, buffered_point) for buffered_point in buffered_points]

#     # Sélectionner les localités qui intersectent la zone tampon
#     localites_proches = gpd.GeoDataFrame()
#     for buffered_point in unprojected_buffers:
#         localites_proches = localites_proches.append(localite_copy_gdf[localite_copy_gdf.geometry.intersects(buffered_point)])

#     # Si au moins une localité est trouvée
#     if not localites_proches.empty:
#         # Trouver le point de localité le plus proche du point
#         nearest_geom = nearest_points(point, localites_proches.unary_union)[1]
        
#         # Trouver la localité correspondant au point le plus proche
#         nearest_localite = localites_proches[localites_proches.geometry == nearest_geom]
        
#         return nearest_localite
#     else:
#         # Si aucune localité n'est trouvée dans la zone tampon
#         return gpd.GeoDataFrame()  # Retourne un GeoDataFrame vide


# Fonction pour trouver la localité la plus proche d'un point
def trouver_localite_proche(point):
    # Initialiser le rayon de la zone tampon
    rayon = 0.1  # Commence avec une zone tampon de 0.1 degré

    # Définir le rayon maximal de la zone tampon
    rayon_maximal = 1.0  # Limite le rayon à 1 degré

    while rayon <= rayon_maximal:
        # Créer une zone tampon autour du point
        buffered_point = point.buffer(rayon)

        # Sélectionner les localités qui intersectent la zone tampon
        localites_proches = localite_copy_gdf[localite_copy_gdf.geometry.intersects(buffered_point)]

        # Si au moins une localité est trouvée
        if not localites_proches.empty:
            # Trouver le point de localité le plus proche du point
            nearest_geom = nearest_points(point, localites_proches.unary_union)[1]
            
            # Trouver la localité correspondant au point le plus proche
            nearest_localite = localites_proches[localites_proches.geometry == nearest_geom]
            
            return nearest_localite
        else:
            # Augmenter le rayon de la zone tampon
            rayon += 0.1  # Augmenter de 0.1 degré à chaque itération

    # Si aucune localité n'est trouvée dans le rayon maximal
    return gpd.GeoDataFrame()  # Return an empty GeoDataFrame

# Appeler la fonction pour rechercher des places et afficher leurs localités
recherche_places_et_localites()
