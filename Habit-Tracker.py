import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "YOUR_TOKEN_HERE",
    "username": "YOUR_USERNAME_HERE",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

