import tkinter as tk
import threading
from pynput.mouse import Listener
import pyautogui
import tkinter.messagebox as messagebox
import pygetwindow as gw

# Define coordinates_label as a global variable
coordinates_label = None

def update_coordinates(x, y):
    coordinates_label.config(text=f"({x}, {y})")
    window.geometry(f"30x30+{x+10}+{y-40}")

def save_coordinates(x, y):
    with open("click_coordinates.txt", "a") as f:
        f.write(f"({x}, {y})\n")

def on_click(x, y, button, pressed):
    if pressed:
        update_coordinates(x, y)
        save_coordinates(x, y)

def start_mouse_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()

def clear_coordinates():
    with open("click_coordinates.txt", "w") as f:
        f.write("")
    messagebox.showinfo("Coordinates Cleared", "Previous coordinates have been cleared.")

# Check if the user wants to clear previous coordinates
if messagebox.askyesno("Clear Coordinates", "Do you want to erase previous coordinates?"):
    clear_coordinates()

# Create the main window
window = tk.Tk()
window.title("Mouse Coordinates")
window.geometry("30x30")

# Set the Tkinter window to be always on top
window.attributes('-topmost', 1)

# Set the global coordinates_label variable
coordinates_label = tk.Label(window, text="")
coordinates_label.pack(side="right")

# Start a thread to listen for mouse clicks
mouse_thread = threading.Thread(target=start_mouse_listener)
mouse_thread.daemon = True
mouse_thread.start()

# Start the GUI event loop
window.mainloop()
