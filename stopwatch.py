import tkinter as tk
import time

# Stopwatch state
is_running = False
start_time = 0
elapsed = 0

def update_display():
    if is_running:
        global elapsed
        elapsed = time.time() - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))
        time_label.config(text=formatted_time)
        root.after(1000, update_display)

def start_timer():
    global is_running, start_time
    if not is_running:
        is_running = True
        start_time = time.time() - elapsed
        update_display()

def stop_timer():
    global is_running
    is_running = False

def reset_timer():
    global is_running, elapsed
    is_running = False
    elapsed = 0
    time_label.config(text="00:00:00")

# GUI setup
root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x150")

time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
time_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

tk.Button(buttons_frame, text="Start", width=8, command=start_timer).pack(side="left", padx=5)
tk.Button(buttons_frame, text="Stop", width=8, command=stop_timer).pack(side="left", padx=5)
tk.Button(buttons_frame, text="Reset", width=8, command=reset_timer).pack(side="left", padx=5)

root.mainloop()
