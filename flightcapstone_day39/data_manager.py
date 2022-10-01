import requests


SHEETY_ENDPOINT = "https://api.sheety.co/fbba0bd391a802039df3378c3f03280e/day39CapstoneFlightDeals/prices"
SHEETY_PUT_ENDPOINT = "https://api.sheety.co/fbba0bd391a802039df3378c3f03280e/day39CapstoneFlightDeals/prices"


class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        request = requests.get(url=SHEETY_ENDPOINT)
        data = request.json()['prices']
        self.destination_data = {city['id']: city['city'] for city in data if city['iataCode'] == ''}
        return self.destination_data

    def update_iata(self, destination: dict):
        for id, city in destination.items():
            body = {
                'price': {
                    'iataCode': city,
                }
            }
            response = requests.put(url=f"{SHEETY_PUT_ENDPOINT}/{id}", json=body)
            print(response.text)




