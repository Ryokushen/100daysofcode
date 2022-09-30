# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
import requests
SHEETY_ENDPOINT = "https://api.sheety.co/fbba0bd391a802039df3378c3f03280e/day39CapstoneFlightDeals/prices"

request = requests.get(url=SHEETY_ENDPOINT)
request.raise_for_status
r = request.json()
pprint(r)
