import requests
import config
from datetime import datetime


# Set-up
TODAY = datetime.now().strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": config.token
}

user_params = {
    "token": config.token,
    "username": config.username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": "graph1",
    "name": "Vitamin Graph",
    "unit": "Count",
    "type": "int",
    "color": "ichou"
}

pixel_params = {
    "date": "20230808",
    "quantity": "5",
}


# Create User
# response = requests.post("https://pixe.la/v1/users", json=user_params)
# print(response.text)


# Create a Graph
# response2 = requests.post(f"https://pixe.la/v1/users/{config.username}/graphs", json=graph_params, headers=headers)
# print(response2.text)


# Post A Pixel
response3 = requests.post(f"https://pixe.la/v1/users/{config.username}/graphs/graph1", json=pixel_params, headers=headers)
print(response3.text)


# Updating a Pixel
# update_pixel_params = {
#     "quantity": "7"
# }
# response4 = requests.put(f"https://pixe.la/v1/users/{config.username}/graphs/graph1/20230822", json=update_pixel_params, headers=headers)


# Deleting a Pixel
# response5 = requests.delete(f"https://pixe.la/v1/users/{config.username}/graphs/graph1/20230822", headers=headers)

