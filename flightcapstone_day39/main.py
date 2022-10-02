# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
flight_search = FlightSearch(data_manager)
# iata_code = flight_search.update_locations()
# data_manager.update_iata(iata_code)


print(flight_search.locations)
