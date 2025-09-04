# ⚡ ESP32 Smart Home / Smart Energy Meter (Simulation + Code)

## 📌 Overview
This project simulates a **Smart Energy Meter** using Python:
- Generates sample Voltage & Current readings
- Calculates **Power (W)** and **Energy (Wh)**
- Plots the consumption graph

## 📂 Structure
- `src/` → Python source code
- `data/` → Generated CSV data
- `docs/` → Plots & diagrams
- `requirements.txt` → Required Python libraries

## 🚀 Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/Vishnuduttana/esp32-smart-home.git
   cd esp32-smart-home
## ▶️ Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Vishnuduttana/esp32-smart-home.git
   cd esp32-smart-home
pip install -r requirements.txt
python src/generate_data.py
python src/energy_meter.py
