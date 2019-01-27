from touristfriend.api_keys import Y_KEY
from touristfriend.business import Business
import requests
import json


def search(lat, lng, distance, query):
    """
    Searches the Yelp API (Max Limit = 20)

    :param lat: Latitude of the request
    :param long: Longitude of the request
    :param distance: Distance to search (meters)
    :param query: The niche, i.e. restaurants, bars, etc
    :returns: List of retrieved businesses
    """

    headers = {'Authorization': 'Bearer ' + Y_KEY}

    params = {}
    params['term'] = query
    params['limit'] = 15
    params['longitude'] = lng
    params['latitude'] = lat
    params['radius_filter'] = distance
    response = requests.get("https://api.yelp.com/v3/businesses/search",
                            params=params, headers=headers)
    data = json.loads(response.content.decode('utf-8'))
    business_list = []
    for i in range(0, len(data['businesses'])):
        try:
            business = data['businesses'][i]
            if business:
                business_list.append(Business(business['name'],
                                              business['location'][
                    'display_address'][0],
                    business['rating'],
                    business['review_count'],
                    (business["coordinates"]["latitude"],
                     business["coordinates"]["longitude"])))
        except IndexError:
            pass

    return business_list
