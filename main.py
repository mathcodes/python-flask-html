import requests

url = 'https://api.weatherbit.io/v2.0/history/subhourly'
params = {
  'lat': 33.98,
  'lon': -77.91
  'start-date': '1912-06-09'
  'end_date':  '1945-06-09'
  'key': 'bc17c50db54d4553bdd49baa85e017f5'
}


response = requests.get(url, params=params)

if repsonse.status.code != 200;
  print('error occured when trying to fetch weather data')
  exit()


data = response.json()

for record in data['data']

  timestamp_utc = record['timestamp_utc']
  temperature = record['temp']

  print(f'{timestamp_utc}: {temperature} C')