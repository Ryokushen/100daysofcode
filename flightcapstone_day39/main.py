# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.data

if sheet_data["prices"][0]["iataCode"] == "":
    for row in sheet_data["prices"]:
        row["iataCode"] = flight_search.response

data_manager.destination_data = sheet_data["prices"]
data_manager.update_dest()




