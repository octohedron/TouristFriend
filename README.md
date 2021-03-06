# TouristFriend


TouristFriend is an API for searching and combining results from Google Places and Yelp.

For the foursquare implementation check out the branch `foursquare`

Returns a combined list of places ranked by their ratings as a Bayesian estimate

### Try it out
```Bash
$ curl http://touristfriend.club/api/40000/29.743883,-95.361621/restaurants
```

## Sample output

```JavaScript
[
  {
    "Rating": "9.49",
    "Sources": 1,
    "Number_of_Ratings": 868,
    "Location": "37.761594,-122.42427",
    "Name": "Pizzeria Delfina"
  },
  {
    "Rating": "9.39",
    "Sources": 1,
    "Number_of_Ratings": 404,
    "Location": "37.7682006597,-122.421604657",
    "Name": "Shizen"
  },
  {
    "Rating": "9.32",
    "Sources": 1,
    "Number_of_Ratings": 45,
    "Location": "37.763093,-122.424281",
    "Name": "Turner's Kitchen"
  },
  // Up to 15 results...
]
```

URI Breakdown: `http://touristfriend.club/api/{meters}/{latitude},{longitude}/{query}`

## Setup
You'll need to acquire API keys for each of the individual services and add them to api_keys.py.

+ [Google Places](https://developers.google.com/places/web-service/get-api-key)
+ [Yelp](https://www.yelp.com/developers/v3/manage_app)

### Set environment variables

```Bash
# Google Places
$ export G_API=YOUR_GOOGLE_API_KEY

# Yelp
$ export YELP_API_KEY=YOUR_YELP_API_KEY

# Flask app, standing on the root of the cloned repo
$ export FLASK_APP=$(pwd)/touristfriend/__init__.py
```
### Install dependencies

```Bash
pip install -U Flask flask-cors
```

### Run it

```Bash
# For localhost
$ flask run # 127.0.0.1
# For external server
$ flask run --host "0.0.0.0" &
```

### Try it

```Bash
$ curl http://localhost:5000/api/40000/48.888001,2.337442/restaurants
```

### With Docker example

```Bash
$ docker build -t tfriend --build-arg GMAPS_KEY=YOUR_GOOGLE_MAPS_KEY \
  --build-arg G_API=YOUR_GOOGLE_API_KEY \
  --build-arg YELP_API_KEY=YOUR_YELP_API_KEY . && \
  docker run -p 5000:5000 tfriend
```

Feel free to use the `touristfriend.club` API for testing or demoing, if you plan on using it on production, consider deploying it yourself.

LICENSE: MIT
