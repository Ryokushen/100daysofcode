from data_manager import DataManager
import os
import requests


KIWI_API = {
    'apikey': os.environ.get('KIWI_API')
}
KIWI_ENDPOINT = 'https://api.tequila.kiwi.com/locations/query'
# KIWI_ENDPOINT_FLIGHT = f'https://api.tequila.kiwi.com/v2/search?fly_from=LON&fly_to={}&dateFrom={}&dateTo={}'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, data: DataManager):
        self.locations = data.get_data()

    def update_locations(self):
        for id, city in self.locations.items():
            new_data = {
                'term': city
            }
            response = requests.get(
                url=KIWI_ENDPOINT, headers=KIWI_API, params=new_data)
            response.raise_for_status()
            self.locations[id] = response.json()['locations'][0]['code']
            print(response.text)
        return self.locations

    # def search_flights(self):
    #     response = requests.get(url=KIWI_ENDPOINT_FLIGHT, headers=KIWI_API)
    #     response.raise_for_status()
