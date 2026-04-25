# Wildlife Alerts in U.S. National Parks

## Overview
This project uses the National Park Service (NPS) API to collect and analyze park alerts. The focus is on identifying alerts related to wildlife and animals.

## Data Source
Data is collected from the NPS API:
- Parks endpoint
- Alerts endpoint

## Data Storage
- parks.csv → stores park information
- alerts.csv → stores alert data
- results.json → stores analysis results

## Features
- Pulls live JSON data from API
- Appends new data (does not overwrite CSV files)
- Identifies animal-related alerts using keyword matching
- Performs analysis on alert types and frequency

## Analysis
The program calculates:
- Total alerts
- Animal-related alerts
- Percentage of animal alerts
- Most common animals mentioned
- Alert types (Danger, Closure, etc.)
- Parks with the most animal alerts

## How to Run
1. Add your API key to config.py
2. Run: