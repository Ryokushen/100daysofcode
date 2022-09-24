import requests
import datetime

USERNAME = "ryokushen"
TOKEN = "09187263"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN ,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "reading1",
    "name": "reading",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

update_graphendpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

update_graph = {
    "date": datetime.date.today(),
    "quantity": "20",
}
today = []
for x in str(update_graph['date']):
    if x == "-":
        x = ""
        today.append(x)
    else:
        today.append(x)
todayjoined = "".join(today)
update_graph["date"] = todayjoined

response = requests.post(url=update_graphendpoint, json=update_graph, headers=headers)
print(response.text)
