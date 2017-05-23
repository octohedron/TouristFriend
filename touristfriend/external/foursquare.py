import time
from touristfriend.api_keys import F_CLIENT_ID, F_CLIENT_SECRET
from touristfriend.business import Business
import requests

SEARCH_URL = 'https://api.foursquare.com/v2/venues/explore?ll={},{}&intent=browse&radius={}&limit=5&query={}&client_id={}&client_secret={}&v={}'


def search(lat, lng, distance, query):
    """
    Searches the Foursquare API (Max Limit = 50)

    :param lat: Latitude of the request
    :param long: Longitude of the request
    :param distance: Distance to search (meters)
    :param query: The niche, i.e. restaurants, bars, etc
    :returns: List of retrieved venues
    """

    url = SEARCH_URL.format(lat, lng, distance,
                            query, F_CLIENT_ID, F_CLIENT_SECRET,
                            time.strftime("%Y%m%d"))
    venue_list = []

    data = requests.get(url).json()
    for i in range(0, len(data['response']['groups'][0]['items'])):
        try:
            item = data['response']['groups'][0]['items'][i]
            venue = item['venue']
            venue_list.append(Business(venue['name'],
                                       venue['location']['address'],
                                       venue['rating'],
                                       venue['ratingSignals'],
                                       (venue['location']['lat'], venue['location']['lng'])))
        except IndexError:
            pass

    return venue_list
