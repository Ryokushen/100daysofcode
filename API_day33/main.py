import requests
from datetime import datetime

MY_LAT = 36.714588
MY_LNG = -76.249931
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)