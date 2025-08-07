
# HDD/CDD Daily Automation
Automation of the hdd_cdd_calculator for energy management 

## Setup

1. Clone this repo.
2. Install dependencies:
    pip install -r requirements.txt
3. Adjust locations in config/locations.yaml as needed.

## Usage

Run the script manually:
    python scripts/hdd_cdd_daily.py

Or set up a daily cron job (see below).

## Cron Job

To run every day at 7am (adjust paths as necessary):

    0 7 * * * /usr/bin/python3 /path/to/hdd-cdd-automation/scripts/hdd_cdd_daily.py

All CSV files will be saved in data/
