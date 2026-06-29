from datetime import datetime, timedelta
from PIL import Image, ImageTk
import requests

API_KEY = '90699fe89890e52e22f6125f750d2bf5'
lat = 6.435
lon = 3.435

def get_fore_weather(lat, lon):
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


weather = get_fore_weather(lat, lon)


# Get weather for the next 6 hours (2 intervals)

next_3_hours = weather['list'][int(3)]  # Forecast for 3 to 6 hours ahead
next_6_hours = weather['list'][int(6)]
next_12_hours = weather['list'][int(12)]
next_24_hours = weather['list'][int(24)]

tem_3 =next_3_hours['main']['temp']
w_f3 = next_3_hours['weather'][0]['description'].lower()

tem_6 =next_6_hours['main']['temp']
w_f6 = next_6_hours['weather'][0]['description'].lower()

tem_12 =next_12_hours['main']['temp']
w_f12 = next_12_hours['weather'][0]['description'].lower()

tem_24 =next_24_hours['main']['temp']
w_f24 = next_24_hours['weather'][0]['description'].lower()

print(int(tem_3),w_f3)
print(int(tem_6),w_f6)
print(int(tem_12),w_f12)
print(int(tem_24),w_f24)




