import requests
from twilio.rest import Client
from data import *


parameters ={
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_codes = [int(weather_data['list'][i]['weather'][0]['id']) for i in range(4)]
for i in weather_codes:
    if i < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18506652594',
        body="It's going to rain today. Remember to bring an ☔",
        to='+989369192338'
    )
    print(message.status)
