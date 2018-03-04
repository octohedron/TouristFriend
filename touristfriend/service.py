from touristfriend.external import foursquare
from touristfriend.external import google
from touristfriend.external import yelp


def bayesian(R, v, m, C):
    """
    Computes the Bayesian average for the given parameters

    :param R: Average rating for this business
    :param v: Number of ratings for this business
    :param m: Minimum ratings required
    :param C: Mean rating across the entire list
    :returns: Bayesian average
    """

    # Convert to floating point numbers
    R = float(R)
    v = float(v)
    m = float(m)
    C = float(C)

    return ((v / (v + m)) * R + (m / (v + m)) * C)


def write_businesses(businesses):
    """
    Returns a list of businesses for the API

    :param filename: Output file name
    :param businesses: List of businesses to write
    """
    businesses.sort(key=lambda x: x.bayesian, reverse=True)
    result = []
    for business in businesses:
        result.append(
            {'Location':
             '{},{}'.format(business.location[0], business.location[1]),
             'Name': business.name,
             'Rating': '{0:.2f}'.format(business.bayesian),
                       'Number_of_Ratings': business.rating_count,
                       'Sources': business.source_count})
    return result


def execute_search(locations, distance, query):
    """
    Searches each API module at the given location(s) and distance.

    :param locations: User supplied lat/long point(s)
    :param distance: How far to search (meters)
    :param query: The niche, i.e. restaurants, bars, etc
    :returns: Full list of businesses
    """
    full_business_list = []
    for engine in [foursquare, google, yelp]:
        businesses = []
        for lat, lng in locations:
            businesses.extend(engine.search(lat, lng, distance, query))
        # Remove duplicates from API call overlap
        names = set()
        filtered_list = []
        for business in businesses:
            if business:
                filtered_list.append(business)
                names.add(business.name)
        businesses = filtered_list
        # Calculate low threshold and average ratings
        try:
            low_threshold = min(
                business.rating_count for business in businesses)
        except:
            # go to next item
            continue
        average_rating = sum(
            business.rating for business in businesses) / len(businesses)
        # Convert to 10 point scale
        if engine.__name__ == 'touristfriend.external.foursquare':
            scale_multiplier = 1
        else:
            scale_multiplier = 2
        # Add bayesian estimates to business objects
        for business in businesses:
            business.bayesian = bayesian(business.rating * scale_multiplier,
                                         business.rating_count,
                                         low_threshold,
                                         average_rating * scale_multiplier)

        # Add this search engine's list to full business list
        full_business_list.extend(businesses)

    return full_business_list


def combine_duplicate_businesses(businesses):
    """
    Averages ratings of the same business from different sources

    :param businesses: Full list of businesses
    :returns: Filtered list with combined sources
    """
    seen_addresses = set()
    filtered_list = []
    for business in businesses:
        if business.address not in seen_addresses:
            filtered_list.append(business)
            seen_addresses.add(business.address)
        else:
            # Find duplicate in list
            for b in filtered_list:
                if b.address == business.address:
                    # Average bayesian ratings and update source count
                    new_rating = (b.bayesian + business.bayesian) / 2.0
                    b.bayesian = new_rating
                    b.source_count = b.source_count + 1

    return filtered_list
