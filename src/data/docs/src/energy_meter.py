import pandas as pd
import matplotlib.pyplot as plt

# Read the generated data
df = pd.read_csv("data/sample_data.csv")

# Calculate Power (W) = Voltage * Current
df["Power (W)"] = df["Voltage (V)"] * df["Current (A)"]

# Calculate Energy (Wh) = cumulative sum of Power over time
# Assuming each sample = 1 second interval → 1/3600 hours
df["Energy (Wh)"] = df["Power (W)"].cumsum() * (1/3600)

# Save updated data to new CSV
df.to_csv("data/energy_data.csv", index=False)

# Plot the results
plt.figure(figsize=(10,5))
plt.plot(df["Time (s)"], df["Power (W)"], label="Power (W)", color="blue")
plt.plot(df["Time (s)"], df["Energy (Wh)"], label="Energy (Wh)", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Values")
plt.title("Smart Energy Meter Simulation")
plt.legend()
plt.grid(True)

# Save plot
plt.savefig("docs/energy_plot.png")
plt.show()
