
# HDD/CDD Calculator Automation

This repository automates the daily downloading of Heating Degree Days (HDD) and Cooling Degree Days (CDD) data for multiple locations using the `hdd-cdd-calculator` Python package.

## Overview

- Uses the [hdd-cdd-calculator](https://pypi.org/project/hdd-cdd-calculator/) Python library to fetch HDD/CDD data from the National Weather Service API.
- Automates fetching degree day data for configured locations daily.
- Saves data as timestamped CSV files in the `data/` folder.
- Supports running as a scheduled job using GitHub Actions (cron job equivalent).

## Repository Structure

```
hdd_cdd_calculator_automation/
├── scripts/
│   └── hdd_cdd_daily.py           # Main script to fetch and save HDD/CDD data
├── config/
│   └── locations.yaml             # List of locations with lat/lon coordinates
├── data/                         # CSV output files (tracked with .gitkeep)
├── requirements.txt               # Python dependencies including hdd-cdd-calculator
├── .gitignore                    # Ignores data files and Python caches
├── .github/
│   └── workflows/
│       └── daily-degree-days.yml  # GitHub Actions workflow for scheduled runs
└── README.md                     # This documentation
```

## Setup Instructions

1. **Clone the repository:**

```
git clone https://github.com/rmkenv/hdd_cdd_calculator_automation.git
cd hdd_cdd_calculator_automation
```

2. **Install dependencies:**

```
pip install -r requirements.txt
```

3. **Configure locations:**

Edit `config/locations.yaml` to add or modify the locations where you want to fetch HDD/CDD data. Example format:

```
locations:
  White House: [38.8977, -77.0365]
  New York City: [40.7128, -74.0060]
  Los Angeles: [34.0522, -118.2437]
```

4. **Run the script manually (optional):**

```
python scripts/hdd_cdd_daily.py
```

This will generate a CSV file in the `data/` folder named like `hdd_cdd_data_YYYY-MM-DD.csv`.

## Automating with GitHub Actions

This repo includes a GitHub Actions workflow (`.github/workflows/daily-degree-days.yml`) to automatically run the data fetch script every day at **11:59 PM Eastern Standard Time (UTC-5)**.

- The workflow installs Python, dependencies, runs the script, and then uploads the generated CSV files as downloadable artifacts.
- You can also manually trigger the workflow from the GitHub Actions UI.

### Scheduling Details

- Runs daily at 11:59 PM EST (adjust for daylight savings manually if needed).
- Output CSVs are saved in the `data/` folder during the run and uploaded as action artifacts for download.

## External Resources

- Python package [hdd-cdd-calculator on PyPI](https://pypi.org/project/hdd-cdd-calculator/) — the core dependency used to retrieve HDD/CDD data.
- [hdd-cdd-calculator GitHub repository](https://github.com/rmkenv/hdd_cdd_calculator) for source code and documentation of the package itself.

## Notes

- The `data/` directory contains a `.gitkeep` file to ensure it is tracked by Git even when empty.
- Modify or extend the `config/locations.yaml` file to suit other geographic needs.
- Ensure your Python environment is updated to match the dependencies in `requirements.txt`.
```
