from shapely.geometry import Point

def trouver_place_proche(point, places_data):
    # Initialize the minimum distance and the nearest place type
    min_distance = float('inf')
    nearest_place_type = None
    nearest_place_name = None
    types_de_places = ["bank", "pharmacy", "school", "police", "clinic", "restaurant"]

    # Iterate over the features in the places data
    for feature in places_data['features']:
        # Verifier si le feature a la propriete 'amenity' et si elle est dans la liste des types de place
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
