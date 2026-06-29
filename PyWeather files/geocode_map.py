import folium
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the OpenCage API key from the .env file
OPENCAGE_API_KEY = os.getenv("OPENCAGE_API_KEY")

if not OPENCAGE_API_KEY:
    raise ValueError("API key is missing. Please add it to the .env file.")

def geocode(location):
    """
    Fetch latitude and longitude for a given location using OpenCage API.
    """
    BASE_URL = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": location,
        "key": OPENCAGE_API_KEY,
        "limit": 1,
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    if data["results"]:
        result = data["results"][0]
        latitude = result["geometry"]["lat"]
        longitude = result["geometry"]["lng"]
        components = result["components"]
        city = components.get("city", "")
        state = components.get("state", "")
        country = components.get("country", "")
        continent = components.get("continent", "")
        location_name = ", ".join(filter(None, [city, state, country, continent]))
        return latitude, longitude, location_name
    else:
        raise ValueError("No results found for the given location.")

def save_map(latitude, longitude, location_name):
    """
    Create and save a map with the given coordinates and location name.
    """
    # Create the map object
    map_object = folium.Map(location=[latitude, longitude], zoom_start=13)

    # Add a marker for the location
    folium.Marker([latitude, longitude], popup=f"Location: {location_name}").add_to(map_object)

    # Sanitize location_name for a valid filename
    sanitized_name = location_name.replace(" ", "_").replace(",", "").replace("'", "")
    filename = f"{sanitized_name}.html"

    # Save the map as an HTML file
    map_object.save(filename)
    print(f"Map saved as: {filename}")
    return filename

if __name__ == "__main__":
    location = input("Enter a location: ")
    try:
        latitude, longitude, location_name = geocode(location)
        print(f"Coordinates: {latitude}, {longitude}")
        print(f"Location Name: {location_name}")
        save_map(latitude, longitude, location_name)
    except Exception as e:
        print(f"Error: {e}")
