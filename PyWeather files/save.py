import json

# Save information to a JSON file
def save_info(data, filename="app_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file)
        print("Data saved successfully!")

# Load information from a JSON file
def load_info(filename="app_data.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    else:
        return None

# Example usage
app_data = {"location": "Lagos", "latitude": 6.5244, "longitude": 3.3792}
save_info(app_data)

# Load the information when the app restarts
loaded_data = load_info()
if loaded_data:
    print(f"Loaded data: {loaded_data}")
else:
    print("No saved data found.")
