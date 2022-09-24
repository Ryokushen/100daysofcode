import requests
import datetime

USERNAME = "username"
TOKEN = "token"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN ,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Configure/Create a new graph
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

# Update Graph with Minutes Read
update_graphendpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

# Use datetime module and strftime to format date

today = datetime.date.today()
format_date = today.strftime("%Y%m%d")
update_graph = {
    "date": format_date,
    "quantity": "20",
}

# response = requests.post(url=update_graphendpoint, json=update_graph, headers=headers)
# print(response.text)

# Update past pixel / Delete (Change .put or .delete)
update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{format_date}"

pixel_update = {
    "quantity": "30"
}

response = requests.delete(url=update_pixel, json=pixel_update, headers=headers)
print(response.text)

