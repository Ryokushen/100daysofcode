import os
import requests
import datetime

# Set environment variables for sensitive data
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/fbba0bd391a802039df3378c3f03280e/workoutTracking/workouts"

exercise_input = input("Tell me which exercises you performed:")

# Set Nutritionix Post parameters and headers
id_key = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_input,
}
# Nutritionix Exercise Post Request and Error Raising
r = requests.post(url=NUTRITIONIX_ENDPOINT, data=parameters, headers=id_key)
r.raise_for_status()
api_call = r.json()
print(api_call)

# Sheety Data Format For Loop
for exercise in api_call["exercises"]:
    body = {
        'workout': {
            "date": datetime.datetime.now().strftime("%x"),
            "time": datetime.datetime.now().strftime("%X"),
            "exercise": exercise['name'].title(),
            "calories": exercise['nf_calories'],
            "duration": exercise['duration_min']
        }
    }

    # Sheety API Endpoint
    s = requests.post(url=SHEETY_ENDPOINT, json=body)
    print(s.status_code)
    print(s.text)


