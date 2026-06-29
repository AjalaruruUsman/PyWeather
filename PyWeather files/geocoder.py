import os
import re
import folium
import requests

# Constants
API_KEY = "ff80dd8e35b24d0faaeb62ef9faa434a"
BASE_URL = "https://api.opencagedata.com/geocode/v1/json"

def geocode(address):
    """
    Fetch geocoding data for a given address.
    """
    params = {
        "q": address,
        "key": API_KEY,
        "limit": 1,
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["results"]:
            result = data["results"][0]
            components = result["components"]
            return {
                "latitude": result["geometry"]["lat"],
                "longitude": result["geometry"]["lng"],
                "city": components.get("city", ""),
                "state": components.get("state", ""),
                "country": components.get("country", ""),
                "continent": components.get("continent", ""),
            }
        else:
            return {"error": "No results found."}
    except requests.RequestException as e:
        return {"error": str(e)}

def generate_map(latitude, longitude, city, state, country, continent):
    """
    Generate a map with the given latitude and longitude, and save it as an HTML file.
    The map filename is derived from the state or city name.
    """
    # Determine the name to use for the filename
    location_name = state or city or "location"
    location_name = re.sub(r"[^\w\s]", "", location_name)  # Remove special characters
    location_name = location_name.replace(" ", "_")  # Replace spaces with underscores

    print(f"DEBUG: Location name for file: {location_name}")  # Debugging log

    # Create a map centered around the latitude and longitude
    location_map = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add a marker for the location
    folium.Marker([latitude, longitude], popup=f"{city}, {state}, {country}, {continent}").add_to(location_map)

    # Save the map to an HTML file
    map_filename = f"{location_name}_map.html"
    location_map.save(map_filename)
    print(f"DEBUG: Map saved as {map_filename}")  # Debugging log
    return map_filename

def main():
    """
    Main function to prompt user for input and generate map.
    """
    address = input("Enter an address to search: ").strip()
    if not address:
        print("No address provided.")
        return
    
    # Geocode the address
    result = geocode(address)
    
    if "latitude" in result and "longitude" in result:
        print(f"Coordinates: {result['latitude']}, {result['longitude']}")
        print(f"City: {result['city']}")
        print(f"State: {result['state']}")
        print(f"Country: {result['country']}")
        print(f"Continent: {result['continent']}")

        # Generate the map and save it
        map_file = generate_map(result['latitude'], result['longitude'], result['city'], result['state'], result['country'], result['continent'])
        print(f"The map has been saved as {map_file}.")

        # Open the map in the default web browser
        os.system(f'start {map_file}')  # Works on Windows
    else:
        print("Error:", result.get("error", "An unknown error occurred."))

if __name__ == "__main__":
    main()
