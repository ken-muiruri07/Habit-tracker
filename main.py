import requests
from datetime import datetime

USERNAME = "muiruri07"
TOKEN = "dhw9hifijnfwifhuiw"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "dhw9hifijnfwifhuiw",
    "username": "muiruri07",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Hours spent coding",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you spend coding today? "),
}
response = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}", json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
update_pixel = {
    "quantity": "6"
}
# response = requests.put(url=update_endpoint, json=update_pixel, headers=headers)
# print(response.text)

delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)




