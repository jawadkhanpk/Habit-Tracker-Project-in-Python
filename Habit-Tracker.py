import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "jawadkhanpk"
TOKEN = "79879879823423"
GRAPHID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Step 1 Creating a Pixela User Account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Step 2 Creating a Graph Definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphs_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {

    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graphs_config, headers=headers)
# print(response.text)


# Step 3 Get the graph!
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph


# Step 4 Post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

date = datetime(year=2024, month=6, day=28)
pixel_data = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "20.0"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# Step 5 Put the value to a graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "12.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# Step 6 Delete a value from a graph

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date.strftime('%Y%m%d')}"
response = requests.delete(url=pixela_endpoint, headers=headers)
print(response.text)