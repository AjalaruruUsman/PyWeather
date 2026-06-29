import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Create a circle (initial dummy position)
circle = canvas.create_oval(0, 0, 30, 30, fill='orange')

# Function to update circle position based on time
def update_position_based_on_time():
    current_time = time.strftime("%H:%M:%S")  # Get current time as string HH:MM:SS
    print("Current Time:", current_time)  # Optional: print time to see updates
    
    # Example positions
    if current_time >= "06:00:00" and current_time < "07:00:00":  # Between 6 AM and 9 AM
        x, y = 50, 100
    elif current_time >= "07:00:00" and current_time < "08:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "08:00:00" and current_time < "09:00:00":  # Between 12 PM and 3 PM
        x, y = 250, 150
    elif current_time >= "09:00:00" and current_time < "10:00:00":  # Between 3 PM and 6 PM
        x, y = 300, 250
    elif current_time >= "10:00:00" and current_time < "11:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "11:00:00" and current_time < "12:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "12:00:00" and current_time < "13:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "13:00:00" and current_time < "14:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "14:00:00" and current_time < "15:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "15:00:00" and current_time < "16:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "16:00:00" and current_time < "17:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "17:00:00" and current_time < "18:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    elif current_time >= "18:00:00" and current_time < "06:00:00":  # Between 9 AM and 12 PM
        x, y = 150, 50
    else:  # Default / Night time
        x, y = 200, 300

    # Set circle to new position (30x30 size)
    canvas.coords(circle, x - 15, y - 15, x + 15, y + 15)

    # Repeat every second to update position if time changes
    root.after(1000, update_position_based_on_time)

# Start updating based on time
update_position_based_on_time()

root.mainloop()
