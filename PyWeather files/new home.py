import tkinter as tk
from tkinter import ttk, messagebox
import requests
#import geocoder

'''def get_location():
    g = geocoder.ip("me")  # Get current location based on IP
    if g.latlng:
        return g.latlng[0], g.latlng[1]
    else:
        messagebox.showerror("Error", "Could not determine location")
        return None, None'''
def get_current_location(api_key):
    url = 'https://ipinfo.io/json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        loc = data['loc'].split(',')
        lat = loc[0]
        lon = loc[1]
        return lat, lon
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None, None

def get_weather():
    api_key = "90699fe89890e52e22f6125f750d2bf5"  # Replace with your actual API key
    lat, lon = get_current_location(api_key)
    if lat is None or lon is None:
        return
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            city_label.config(text=f"City: {lat},{lon} {data['name']}")
            temp_label.config(text=f"Temperature: {data['main']['temp']}°C")
            humidity_label.config(text=f"Humidity: {data['main']['humidity']}%")
            desc_label.config(text=f"Condition: {data['weather'][0]['description']}")
        else:
            messagebox.showerror("Error", "Could not retrieve weather data")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

frame = ttk.Frame(root, padding="10")
frame.pack(pady=20)

city_label = tk.Label(frame, text="City: ")
city_label.pack()

temp_label = tk.Label(frame, text="Temperature: ")
temp_label.pack()

humidity_label = tk.Label(frame, text="Humidity: ")
humidity_label.pack()

desc_label = tk.Label(frame, text="Condition: ")
desc_label.pack()

get_weather_button = ttk.Button(frame, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

#get_weather()  # Automatically fetch weather on startup

root.mainloop()
