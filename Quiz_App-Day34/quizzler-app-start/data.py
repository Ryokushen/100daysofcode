import requests


parameters = {
    'amount': 10,
    'type': 'boolean'
}


get_questions = requests.get("https://opentdb.com/api.php?", params=parameters)
get_questions.raise_for_status()
data = get_questions.json()
question_data = data["results"]

