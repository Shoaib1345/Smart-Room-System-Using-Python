import tkinter as tk
from tkinter import ttk

# States
fan_on = False
light_on = False
ac_on = False

def toggle_fan():
    global fan_on
    if mode_var.get() == "Manual":
        fan_on = not fan_on
        fan_status.config(text=f"Fan: {'ON' if fan_on else 'OFF'}")

def toggle_light():
    global light_on
    if mode_var.get() == "Manual":
        light_on = not light_on
        light_status.config(text=f"Light: {'ON' if light_on else 'OFF'}")

def toggle_ac():
    global ac_on
    if mode_var.get() == "Manual":
        ac_on = not ac_on
        ac_status.config(text=f"AC: {'ON' if ac_on else 'OFF'}")

# Main window
root = tk.Tk()
root.title("Smart Room System")
root.geometry("500x600")
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("TLabel", background="#f0f4f7", font=("Segoe UI", 12))
style.configure("Header.TLabel", font=("Segoe UI", 20, "bold"))
style.configure("TButton", font=("Segoe UI", 11))
style.configure("TRadiobutton", background="#f0f4f7", font=("Segoe UI", 11))

# Header
header = ttk.Label(root, text="Smart Room System", style="Header.TLabel")
header.grid(row=0, column=0, columnspan=2, pady=20)

# Sensor Data
sensor_frame = ttk.LabelFrame(root, text="Sensor Data", padding=15)
sensor_frame.grid(row=1, column=0, columnspan=2, padx=30, pady=10, sticky="ew")

ttk.Label(sensor_frame, text="Temperature: -- °C").grid(row=0, column=0, sticky="w", pady=2)
ttk.Label(sensor_frame, text="Light Level: --").grid(row=1, column=0, sticky="w", pady=2)
ttk.Label(sensor_frame, text="Motion: --").grid(row=2, column=0, sticky="w", pady=2)

# Device Status
status_frame = ttk.LabelFrame(root, text="Device Status", padding=15)
status_frame.grid(row=2, column=0, columnspan=2, padx=30, pady=10, sticky="ew")

fan_status = ttk.Label(status_frame, text="Fan: OFF")
light_status = ttk.Label(status_frame, text="Light: OFF")
ac_status = ttk.Label(status_frame, text="AC: OFF")

fan_status.grid(row=0, column=0, sticky="w", pady=2)
light_status.grid(row=1, column=0, sticky="w", pady=2)
ac_status.grid(row=2, column=0, sticky="w", pady=2)

# Control Mode
mode_frame = ttk.LabelFrame(root, text="Control Mode", padding=15)
mode_frame.grid(row=3, column=0, columnspan=2, padx=30, pady=10, sticky="ew")

mode_var = tk.StringVar(value="Auto")
ttk.Radiobutton(mode_frame, text="Auto", variable=mode_var, value="Auto").grid(row=0, column=0, sticky="w", pady=2)
ttk.Radiobutton(mode_frame, text="Manual", variable=mode_var, value="Manual").grid(row=1, column=0, sticky="w", pady=2)

# Manual Controls
manual_frame = ttk.LabelFrame(root, text="Manual Controls", padding=15)
manual_frame.grid(row=4, column=0, columnspan=2, padx=30, pady=10, sticky="ew")

ttk.Button(manual_frame, text="Toggle Fan", command=toggle_fan).grid(row=0, column=0, sticky="ew", pady=5)
ttk.Button(manual_frame, text="Toggle Light", command=toggle_light).grid(row=1, column=0, sticky="ew", pady=5)
ttk.Button(manual_frame, text="Toggle AC", command=toggle_ac).grid(row=2, column=0, sticky="ew", pady=5)

root.mainloop()
