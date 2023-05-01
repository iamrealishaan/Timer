import tkinter as tk
import time
import winsound

# Define the main window
root = tk.Tk()
root.title("Timer")

# Define the timer label
timer_label = tk.Label(root, font=("Arial", 30))
timer_label.pack(pady=20)

# Define the start button
def start_timer():
    # Get the timer duration from the user (in seconds)
    duration = int(timer_entry.get())
    
    # Disable the timer entry and start button
    timer_entry.config(state="disabled")
    start_button.config(state="disabled")
    
    # Start the timer
    for i in range(duration, 0, -1):
        timer_label.config(text=i)
        root.update()
        time.sleep(1)
    
    # Play the sound
    winsound.Beep(440, 1000)
    
    # Reset the timer label and enable the timer entry and start button
    timer_label.config(text="Time's up!")
    timer_entry.config(state="normal")
    start_button.config(state="normal")

timer_entry = tk.Entry(root, font=("Arial", 30))
timer_entry.pack(pady=20)

start_button = tk.Button(root, text="Start", font=("Arial", 20), command=start_timer)
start_button.pack(pady=20)

# Run the main loop
root.mainloop()
