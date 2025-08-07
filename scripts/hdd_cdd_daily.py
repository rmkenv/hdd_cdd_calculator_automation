import os
import csv
import yaml
from datetime import datetime
from hdd_cdd import get_degree_days_for_location

# Path configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CONFIG_FILE = os.path.join(BASE_DIR, "config", "locations.yaml")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def read_locations():
    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)
    return config["locations"]

def fetch_and_save_data(locations, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Location", "Date", "High Temp (F)", "Low Temp (F)", 
            "Mean Temp (F)", "HDD", "CDD"
        ])
        for loc_name, coords in locations.items():
            lat, lon = coords
            results = get_degree_days_for_location(lat, lon)
            for result in results:
                writer.writerow([
                    loc_name,
                    result.date,
                    result.high_temp,
                    result.low_temp,
                    f"{result.mean_temp:.1f}",
                    f"{result.hdd:.1f}",
                    f"{result.cdd:.1f}"
                ])

if __name__ == "__main__":
    today_date = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(DATA_DIR, f"hdd_cdd_data_{today_date}.csv")
    locations = read_locations()
    fetch_and_save_data(locations
