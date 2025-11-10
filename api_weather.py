import requests
import json

params = {'q': 'Kirov',
          'units': 'metric',
          'appid': 'ae65b77354e6a2f442406268ce96d315'}

url = 'https://api.openweathermap.org/data/2.5/weather'
response = requests.get(url, params = params)

print(response.status_code)
print(response.json())