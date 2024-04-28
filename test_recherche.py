import json
import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import nearest_points
from shapely.ops import transform
import pyproj
from geopy.distance import geodesic


# Charger le fichier GeoJSON des places
localite_copy_gdf = gpd.read_file("data/places.geojson")
# Fonction pour trouver la localité la plus proche d'un point avec une zone tampon étendue
def trouve_place_proche(point):
    # Initialiser le rayon minimal de la zone tampon à 50m
    rayon_minimal = 10  # en mètres

    # Définir le rayon maximal de la zone tampon à 700m
    rayon_maximal = 700  # en mètres

    # Convertir les distances de mètres en degrés (approximatif)
    # Approximation basée sur une longitude moyenne pour l'emplacement d'intérêt
    conversion_degrees_per_meter = 1 / 111000  # Approximation moyenne
    
    rayon_minimal_deg = rayon_minimal * conversion_degrees_per_meter
    rayon_maximal_deg = rayon_maximal * conversion_degrees_per_meter

    # Créer une fonction de projection pour calculer la zone tampon en mètres
    project = pyproj.Transformer.from_proj(
        pyproj.Proj(init='epsg:4326'),  # WGS84
        pyproj.Proj(proj='aea', lat_1=point.y-rayon_maximal_deg, lat_2=point.y+rayon_maximal_deg),  # Albers Equal Area
        always_xy=True)

    # Fonction pour projeter les coordonnées en mètres
    def project_point(x, y):
        return project.transform(x, y)

    # Créer un point projeté
    projected_point = transform(project_point, point)

    # Créer des zones tampons circulaires autour du point projeté avec des rayons min et max
    buffered_points = [
        projected_point.buffer(rayon_minimal),
        projected_point.buffer(rayon_maximal)
    ]

    # Convertir les zones tampons en degrés
    def unproject_point(x, y):
        return project.transform(x, y, inverse=True)

    unprojected_buffers = [transform(unproject_point, buffered_point) for buffered_point in buffered_points]

    # Sélectionner les localités qui intersectent la zone tampon
    localites_proches = gpd.GeoDataFrame()
    for buffered_point in unprojected_buffers:
        localites_proches = localites_proches.append(localite_copy_gdf[localite_copy_gdf.geometry.intersects(buffered_point)])

    # Si au moins une localité est trouvée
    if not localites_proches.empty:
        # Trouver le point de localité le plus proche du point
        nearest_geom = nearest_points(point, localites_proches.unary_union)[1]
        
        # Trouver la localité correspondant au point le plus proche
        nearest_localite = localites_proches[localites_proches.geometry == nearest_geom]
        
        return nearest_localite
    else:
        # Si aucune localité n'est trouvée dans la zone tampon
        return gpd.GeoDataFrame()  # Retourne un GeoDataFrame vide

