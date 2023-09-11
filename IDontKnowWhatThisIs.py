import tkinter as tk

def start_program():
    message_label.config(text="It just works                                   ")

def rotate_text():
    current_text = message_label.cget("text")
    message_label.config(text=current_text[1:] + current_text[0])
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
start_button.pack()

# Start rotating the text
rotate_text()

# Start the GUI event loop
window.mainloop()
