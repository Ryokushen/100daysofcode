from ast import While
import email
import requests
from datetime import datetime
from smtplib import SMTP
import schedule
import time

MY_LAT = 36.755169 # Your latitude
MY_LONG = -76.237442 # Your longitude
MY_EMAIL = "fakeremail@gmail.com"
MY_PASSWORD = "reactionary82!"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

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


def iss_check():
    if (compare_pos() == True and sunset <= current_hour) or (compare_pos() == True and current_hour <= sunrise):
        with SMTP("smtp.gmail.com", port=587) as template:
            template.starttls()
            template.login(user=MY_EMAIL, password=MY_PASSWORD)
            template.sendmail(from_addr=MY_EMAIL, to_addrs='fakeemail@gmail.com',
            msg="Subject:International Space Station\n\n The ISS is above you. Look Outside! :)")


schedule.every(60).seconds.do(iss_check)

while True:
    schedule.run_pending()
    time.sleep(1)




