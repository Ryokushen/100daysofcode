import requests

API_KEY = "69f04e4613056b159c2761a9d9e664d2"


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 36.755169,
    "lon": -76.237442,
    "appid": API_KEY

}
r = requests.get(OWM_Endpoint, params=weather_params)
r.raise_for_status()
data = r.json()
print(data['hourly'])
