from pprint import pprint
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/fbba0bd391a802039df3378c3f03280e/day39CapstoneFlightDeals/prices"


class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.request = requests.get(url=SHEETY_ENDPOINT)
        self.request.raise_for_status
        self.data = self.request.json()
