import csv
import random
import time

# Generate fake sensor data (Voltage & Current)
with open("data/sample_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time (s)", "Voltage (V)", "Current (A)"])
    
    for t in range(1, 21):  # 20 samples
        voltage = round(random.uniform(210, 230), 2)   # Voltage between 210V–230V
        current = round(random.uniform(0.5, 5.0), 2)   # Current between 0.5A–5A
        writer.writerow([t, voltage, current])
        time.sleep(0.1)  # Simulate delay

