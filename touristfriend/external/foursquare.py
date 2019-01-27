import time
from touristfriend.api_keys import F_CLIENT_ID, F_CLIENT_SECRET
from touristfriend.business import Business
import requests

search_url = 'https://api.foursquare.com/v2/venues/explore?ll={},{}&intent=browse&radius={}&limit=5&query={}&client_id={}&client_secret={}&v={}'
details_url = "https://api.foursquare.com/v2/venues/{}?client_id={}&client_secret={}&v={}"


def search(lat, lng, distance, query):
    """
    Searches the Foursquare API (Max Limit = 50)

    :param lat: Latitude of the request
    :param long: Longitude of the request
    :param distance: Distance to search (meters)
    :param query: The niche, i.e. restaurants, bars, etc
    :returns: List of retrieved venues
    """

    url = search_url.format(lat, lng, distance,
                            query, F_CLIENT_ID, F_CLIENT_SECRET,
                            time.strftime("%Y%m%d"))
    venue_list = []
    data = requests.get(url).json()
    for i in range(0, len(data['response']['groups'][0]['items'])):
        d_url = details_url.format(
            data['response']['groups'][0]['items'][i]['venue']['id'],
            F_CLIENT_ID,
            F_CLIENT_SECRET,
            time.strftime("%Y%m%d"))
        venue_data = requests.get(d_url).json()
        try:
            venue = venue_data['response']['venue']
            venue_list.append(Business(venue['name'],
                                       ", ".join(
                                       venue['location']['formattedAddress']),
                                       venue['rating'],
                                       venue['ratingSignals'],
                                       (venue['location']['lat'],
                                        venue['location']['lng'])))
        except Exception:
            pass

    return venue_list
