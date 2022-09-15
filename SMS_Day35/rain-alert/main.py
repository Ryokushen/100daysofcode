import requests
import smtplib

API_KEY = "69f04e4613056b159c2761a9d9e664d2"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_EMAIL = 'ryokushen37.emailtesting@gmail.com'
MY_PASSWORD = 'bsisfmbvpjecznrq'
TEST_EMAIL = 'ryokushen37@yahoo.com'

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
    first_12_weather.append(first_12[x]["weather"][0]['id'])

weather_status = ""
for num in first_12_weather:
    if num < 700:
        weather_status = "Bring an umbrella!"
#----------------------------------------------------------EMAIL--------------------------------------------------------------------#


def whatistheweather(weather):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TEST_EMAIL,
                            msg=f"Subject: Weather Status \n\n {weather}")


whatistheweather(weather_status)
print('Done...')
