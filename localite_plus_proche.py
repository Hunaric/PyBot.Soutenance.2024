from shapely.ops import nearest_points
import geopandas as gpd

# Fonction pour trouver la localité la plus proche d'un point
def trouver_localite_proche(point):
    # Initialiser le rayon de la zone tampon
    rayon = 0.1  # Commence avec une zone tampon de 0.1 degré

    # Charger le fichier GeoJSON des localités
    localite_copy_gdf = gpd.read_file("data/localites.geojson")

    # Définir le rayon maximal de la zone tampon
    rayon_maximal = 0.9  # Limite le rayon à 0.9 degré

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
