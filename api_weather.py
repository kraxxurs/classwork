import requests
import json

params = {'q': 'Kirov',
          'units': 'metric',
          'appid': ' '}

url = 'https://api.openweathermap.org/data/2.5/weather'
response = requests.get(url, params = params)

print(response.status_code)
print(response.json())