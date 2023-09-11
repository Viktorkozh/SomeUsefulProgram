import tkinter as tk


# Set the initial direction

global direction
direction = "right"

def start_program():
    message_label.config(text="It just works")

def rotate_text():
    global direction
    current_text = message_label.cget("text")

    if direction == "right":
        if message_label.winfo_x() + message_label.winfo_width() >= window.winfo_width():
            direction = "down"
    elif direction == "down":
        if message_label.winfo_y() + message_label.winfo_height() >= window.winfo_height():
            direction = "left"
    elif direction == "left":
        if message_label.winfo_x() <= 0:
            direction = "up"
    elif direction == "up":
        if message_label.winfo_y() <= 0:
            direction = "right"
    if direction == "right":
        message_label.place(x=message_label.winfo_x() + 1, y=message_label.winfo_y())
    elif direction == "down":
        message_label.place(x=message_label.winfo_x(), y=message_label.winfo_y() + 1)
    elif direction == "left":
        message_label.place(x=message_label.winfo_x() - 1, y=message_label.winfo_y())
    elif direction == "up":
        message_label.place(x=message_label.winfo_x(), y=message_label.winfo_y() - 1)
    message_label.after(15, rotate_text)

# Create the main window
window = tk.Tk()
window.title("Program")
window.geometry("300x200")

# Create a label to display the message
message_label = tk.Label(window, text=" ")
message_label.pack(pady=50)

# Create a start button
start_button = tk.Button(window, text="Start", command=start_program)
start_button.place(relx=0.5, rely=0.5, anchor="center")

# Start rotating the text
rotate_text()

# Start the GUI event loop
window.mainloop()
