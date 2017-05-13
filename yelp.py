import requests
from api_keys import Y_ID, Y_S
from business import Business


def search(lat, lng, distance, query):
    """
    Searches the Yelp API (Max Limit = 20)

    :param lat: Latitude of the request
    :param long: Longitude of the request
    :param distance: Distance to search (meters)
    :returns: List of retrieved businesses
    """

    payload = {'grant_type': 'client_credentials',
               'client_id': Y_ID,
               'client_secret': Y_S}

    token = requests.post('https://api.yelp.com/oauth2/token',
                          params=payload).json()["access_token"]
    headers = {'Authorization': 'Bearer ' + token}

    params = {}
    params['term'] = query
    params['longitude'] = lng
    params['latitude'] = lat
    params['radius_filter'] = distance
    data = requests.get("https://api.yelp.com/v3/businesses/search",
                        params=params, headers=headers).json()

    business_list = []
    for i in range(0, 5):
        business = data['businesses'][i]
        business_list.append(Business(business['name'],
                                      business['location'][
                                          'display_address'][0],
                                      business['rating'],
                                      business['review_count']))
    return business_list
