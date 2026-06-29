def geocode_address():
    """
    Get latitude, longitude, and location details for the provided address and display them.
    """
    address = entry_address.get()
    
    if not address:
        messagebox.showwarning("Input Error", "Please enter an address.")
        return
    
    # Geocode the address
    result = geocode(address)
    
    if 'latitude' in result and 'longitude' in result:
        # Show results in the output text box
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Coordinates: {result['latitude']}, {result['longitude']}\n")
        output_text.insert(tk.END, f"City: {result['city']}\n")
        output_text.insert(tk.END, f"State: {result['state']}\n")
        output_text.insert(tk.END, f"Country: {result['country']}\n")
        output_text.insert(tk.END, f"Continent: {result['continent']}\n")

        # Generate the map and save it
        map_file = generate_map(result['latitude'], result['longitude'], result['city'], result['state'], result['country'], result['continent'])
        
        # Notify the user that the map has been saved
        messagebox.showinfo("Map Saved", f"The map has been saved as {map_file}.")
        
        # Open the map in the default web browser
        webbrowser.open(map_file)

    else:
        # Show error if no results found
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result["error"])
