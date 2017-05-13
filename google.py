from api_keys import G_API_KEY
from business import Business
import requests

SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&types={}&key={}'
PLACE_URL = 'https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}'


def search(lat, lng, distance, query):
    """
    Searches the Google Places API (Max Limit = 20)

    :param lat: Latitude of the request
    :param long: Longitude of the request
    :param distance: Distance to search (meters)
    :returns: List of retrieved places
    """

    url = SEARCH_URL.format(lat, lng, distance, query, G_API_KEY)
    place_list = []

    try:
        data = requests.get(url).json()
        for i in range(0, 5):
            result = data['results'][i]
            try:
                place = search_place(result['place_id'])
                place_list.append(place)
            except Exception:
                pass
    except Exception, e:
        print e

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
    return Business(place['name'],
                    place['formatted_address'].split(',')[0],
                    place['rating'],
                    len(place['reviews']))
