import googlemaps
import datetime


def get_direction(gkey, start_location, end_location, transport_mode='driving', departure_time=datetime.datetime.now()):
    gmaps = googlemaps.Client(key=gkey)
    directions_result = gmaps.directions(start_location,
                                         end_location,
                                         mode=transport_mode,
                                         departure_time=departure_time)
    return directions_result