# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py.
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve
# the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
# http://python-data.dr-chuck.net/geojson

import urllib.request
import urllib.parse
import json
import re

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved',len(data),'characters')

    try: js = json.loads(data.decode('utf-8'))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    # retrieve the first place_id from JSON that uniqueley identifies a place as within Google maps
    place_id = js["results"][0]["place_id"]
    print("Place id: ", place_id)
