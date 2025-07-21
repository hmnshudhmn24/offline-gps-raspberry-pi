# 🧭 Offline GPS — Raspberry Pi 5 Project

A **portable offline GPS tracker** with a web-based real-time map UI for bikers and travelers, built for Raspberry Pi 5! This project turns your Pi into a lightweight GPS unit that tracks your location and displays it using an interactive map—all without internet.

## 📦 Features

- 🛰️ Real-time GPS data using `gpsd`
- 🗺️ Interactive map view using Folium and Flask
- 💾 Offline-friendly - once base maps are downloaded, no internet is needed
- 📍 Route tracking with polyline trails
- 🔌 Runs locally on the Raspberry Pi with a web interface

## 🧰 Tech Stack

- `Python 3`
- `gpsd` for GPS data
- `Folium` for map generation
- `Flask` for serving the map UI
- `systemd` or `tmux` for headless auto-start (optional)

## 🚀 Setup Instructions

1. **Install Dependencies**
   ```bash
   sudo apt install gpsd gpsd-clients python3-gps
   pip install flask folium
   ```

2. **Connect GPS Module** to USB/serial port.

3. **Run the App**
   ```bash
   python3 offline_gps.py
   ```

4. Open your browser and go to: `http://<raspberry-pi-ip>:5000`

## 🛠️ Optional Enhancements

- Save track data to GPX format
- Add compass & altitude widgets
- Add battery status using GPIO

## 🏍️ Ideal For

- Bikers who want offline navigation
- Remote area field workers
- DIY vehicle GPS solutions
- Raspberry Pi outdoor/IoT projects

---

Made for explorers, coders, and makers! 🌍🛠️