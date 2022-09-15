from re import X
import requests

API_KEY = "69f04e4613056b159c2761a9d9e664d2"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 36.755169,
    "lon": -76.237442,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"

}
r = requests.get(OWM_Endpoint, params=weather_params)
r.raise_for_status()
weather_data = r.json()

list_of_weather = weather_data['hourly'][0:12]
first_12 = list_of_weather

first_12_weather = []
for x in range(0, 12):
    first_12_weather.append(first_12[x]["weather"])

weather_id = []
for x in first_12_weather:
    weather_id.append(x[0]['id'])

for num in weather_id:
    if num < 700:
        print("Bring an umbrella!")
