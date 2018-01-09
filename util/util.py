from geopy import distance
from googlemaps import convert
import os


def get_key(file):
    if os.path.isfile(file):
        with open(file) as key_file:
            gkey = key_file.readline()
            return gkey
    else:
        return False


def get_distances(coordinates):
    if len(coordinates) == 2:
        return distance.vincenty(coordinates[0].values(), coordinates[1].values()).km
    else:
        return False


def get_coordinates_from_encoded_polyline(directions):
    if 'overview_polyline' in directions[0].keys():
        lat_long_set = convert.decode_polyline(directions[0]['overview_polyline']['points'])
        return lat_long_set
    else:
        return False
