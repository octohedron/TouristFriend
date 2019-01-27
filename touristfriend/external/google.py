from touristfriend.api_keys import G_API_KEY
from touristfriend.business import Business
import requests

SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&types={}&key={}'
PLACE_URL = 'https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}'


def search(lat, lng, distance, query):
    """
    Searches the Google Places API (Max Limit = 20)

    :param lat: Latitude of the request
    :param long: Longitude of the request
    :param distance: Distance to search (meters)
    :param query: The niche, i.e. restaurants, bars, etc
    :returns: List of retrieved places
    """

    url = SEARCH_URL.format(lat, lng, distance, query, G_API_KEY)
    place_list = []

    data = requests.get(url).json()

    for i in range(0, len(data['results'])):
        try:
            result = data['results'][i]
            place = search_place(result['place_id'])
            place_list.append(place)
            if len(place_list) == 5:
                break
        except Exception:
            pass

    return place_list


def search_place(place_id):
    """
    Searches Google for a specific Place

    :param id: Google Place ID
    :returns: Business object
    """
    url = PLACE_URL.format(place_id, G_API_KEY)
    data = requests.get(url).json()
    place = data['result']
    try:
        if not "hotel" in (place['name'].lower()):
            return Business(place['name'],
                            place['formatted_address'].split(',')[0],
                            place['rating'],
                            len(place['reviews']),
                            (place["geometry"]["location"]["lat"],
                                place["geometry"]["location"]["lng"]))
    except KeyError:
        pass
