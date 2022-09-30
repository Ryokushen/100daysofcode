from data_manager import DataManager

data_manager = DataManager()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city_input = data_manager.data['prices']
        for item in self.city_input:
            if 'iataCode' in item:
                item['iataCode'] = 'TESTING'

        self.data = self.city_input
