import email
import requests
from datetime import datetime
from smtplib import SMTP

MY_LAT = 36.755169 # Your latitude
MY_LONG = -76.237442 # Your longitude
MY_EMAIL = "ryokushen37.emailtesting@gmail.com"
MY_PASSWORD = "6KHEfXgzsYvg7Bv"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
# print(iss_longitude)
# print(iss_latitude)

def compare_pos():
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True
        


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if compare_pos() == True and sunset < current_hour < sunrise:
    with SMTP("smtp.gmail.com", port=587) as template:
        template.connect
        template.starttls
        template.login(email=MY_EMAIL, password=MY_PASSWORD)
        template.send_message(from_addr=MY_EMAIL, to_addrs="ryokushen37@yahoo.com"
        msg="Subject:\n\n The ISS is above you. Look Outside! :)")






