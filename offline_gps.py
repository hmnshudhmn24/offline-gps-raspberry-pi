import os
import sys
import time
import threading
from datetime import datetime
from math import radians, cos, sin, asin, sqrt

try:
    import gps
except ImportError:
    print("gps module not found. Make sure gpsd is installed and running.")
    sys.exit(1)

import folium
from flask import Flask, send_file

# Flask app for serving map
app = Flask(__name__)
gps_data = {"lat": 0.0, "lon": 0.0}
track_points = []

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r

def gps_tracker():
    global gps_data, track_points
    session = gps.gps(mode=gps.WATCH_ENABLE)
    while True:
        try:
            report = session.next()
            if report['class'] == 'TPV':
                if hasattr(report, 'lat') and hasattr(report, 'lon'):
                    gps_data["lat"] = report.lat
                    gps_data["lon"] = report.lon
                    if not track_points or haversine(track_points[-1][1], track_points[-1][0], report.lon, report.lat) > 0.01:
                        track_points.append((report.lat, report.lon))
        except KeyError:
            continue
        except StopIteration:
            break
        except Exception as e:
            print("Error:", e)
            time.sleep(1)

@app.route('/')
def map_view():
    global gps_data, track_points
    fmap = folium.Map(location=[gps_data["lat"], gps_data["lon"]], zoom_start=16)
    if track_points:
        folium.PolyLine(locations=track_points, color='blue').add_to(fmap)
        folium.Marker(location=track_points[-1], tooltip="Current Location").add_to(fmap)
    fmap.save('map.html')
    return send_file('map.html')

def start_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def main():
    print("Starting GPS tracker...")
    gps_thread = threading.Thread(target=gps_tracker)
    gps_thread.daemon = True
    gps_thread.start()
    start_flask()

if __name__ == '__main__':
    main()