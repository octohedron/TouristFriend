# TouristFriend


TouristFriend is an API for searching and combining results from Google Places, Yelp, and Foursquare

Returns a combined list of places ranked by their ratings as a Bayesian estimate

### Try it out: 
```Bash
$ curl http://touristfriend.club/api/40000/29.743883,-95.361621/restaurants
```

## Sample output

```JavaScript
[
  {
    "Rating": "9.35",
    "Sources": 1,
    "Name": "Le Comptoir Général",
    "Number of Ratings": 1289
  },
  {
    "Rating": "8.83",
    "Sources": 2,
    "Name": "Marlusse et Lapin",
    "Number of Ratings": 130
  },
  {
    "Rating": "8.81",
    "Sources": 1,
    "Name": "Harry's New York",
    "Number of Ratings": 426
  },
  // Up to 15 results...
]
```

URI Breakdown: `http://touristfriend.club/api/{meters}/{latitude},{longitude}/{query}`

## Setup
You'll need to acquire API keys for each of the individual services and add them to api_keys.py.

+ [Google Places](https://developers.google.com/places/web-service/get-api-key)
+ [Yelp](https://www.yelp.com/developers/v3/manage_app)
+ [Foursquare](https://developer.foursquare.com/)

### Set environment variables

```Bash
# Foursquare
$ export F_ID=YOUR_FOURSQUARE_ID
$ export F_C_S=YOUR_FOURSQUARE_CLIENT_SECRET

# Google Places
$ export G_API=YOUR_GOOGLE_API_KEY

# Yelp
$ export YELP_ID=YOUR_YELP_ID
$ export YELP_SECRET=YOUR_YELP_SECRET
```

## Usage

### Run it
```Bash
$ python api.py
```
### Try it
```Bash
$ curl http://localhost:5000/api/40000/48.888001,2.337442/restaurants
```

LICENSE: MIT
