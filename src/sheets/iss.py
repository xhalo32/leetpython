#!/usr/bin/python
import requests

parameters = {"lat": 40.71, "lon": -74}
response = requests.get("http://api.open-notify.org/iss-pass.json",
    params=parameters)
print(response.status_code)
print(response.json())
print(response.headers)

r = requests.get("http://api.open-notify.org/astros.json")
jsono = r.json()
print(jsono['number'])
