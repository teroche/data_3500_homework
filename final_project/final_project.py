import requests
import csv
import json
import os
from datetime import datetime
from config import API_KEY

PARKS_URL = "https://developer.nps.gov/api/v1/parks"
ALERTS_URL = "https://developer.nps.gov/api/v1/alerts"

PARKS_FILE = "parks.csv"
ALERTS_FILE = "alerts.csv"
RESULTS_FILE = "results.json"

HEADERS = {
    "X-Api-Key": API_KEY
}

animal_keywords = {
    "bear": ["bear", "grizzly", "black bear"],
    "bat": ["bat", "bats"],
    "snake": ["snake", "rattlesnake"],
    "bison": ["bison"],
    "elk": ["elk"],
    "moose": ["moose"],
    "deer": ["deer"],
    "coyote": ["coyote"],
    "wolf": ["wolf", "wolves"],
    "wildlife": ["wildlife", "animal", "animals"]
}


# create parks.csv
if not os.path.exists(PARKS_FILE):
    with open(PARKS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date_collected", "park_code", "park_name", "state"])


# create alerts.csv
if not os.path.exists(ALERTS_FILE):
    with open(ALERTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "date_collected",
            "alert_id",
            "park_code",
            "park_name",
            "alert_type",
            "title",
            "description",
            "is_animal_related",
            "animal_type"
        ])


# get park data from the API
park_params = {
    "limit": 500
}

park_request = requests.get(PARKS_URL, headers=HEADERS, params=park_params)
park_data = park_request.json()
parks = park_data["data"]


# make a dictionary that connects park codes to park names
park_lookup = {}

for park in parks:
    park_code = park.get("parkCode", "")
    park_name = park.get("fullName", "")

    if park_code != "":
        park_lookup[park_code] = park_name


# read existing park codes
existing_park_codes = set()

with open(PARKS_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        existing_park_codes.add(row["park_code"])


# append new parks to parks.csv
today = datetime.now().strftime("%Y-%m-%d")

with open(PARKS_FILE, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for park in parks:
        park_code = park.get("parkCode", "")
        park_name = park.get("fullName", "")
        state = park.get("states", "")

        if park_code not in existing_park_codes:
            writer.writerow([today, park_code, park_name, state])


# get alert data from the API
alert_params = {
    "limit": 500
}

alert_request = requests.get(ALERTS_URL, headers=HEADERS, params=alert_params)
alert_data = alert_request.json()
alerts = alert_data["data"]


# read existing alert IDs
existing_alert_ids = set()

with open(ALERTS_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        existing_alert_ids.add(row["alert_id"])


# append new alerts to alerts.csv
with open(ALERTS_FILE, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for alert in alerts:
        alert_id = alert.get("id", "")

        if alert_id not in existing_alert_ids:

            park_code = alert.get("parkCode", "")
            alert_type = alert.get("category", "")
            title = alert.get("title", "")
            description = alert.get("description", "")

            if park_code in park_lookup:
                park_name = park_lookup[park_code]
            else:
                park_name = "Unknown"

            combined_text = title + " " + description
            combined_text = combined_text.lower()

            is_animal_related = "False"
            animal_type = ""

            for animal in animal_keywords:
                keyword_list = animal_keywords[animal]

                for keyword in keyword_list:
                    if keyword in combined_text:
                        is_animal_related = "True"
                        animal_type = animal

            writer.writerow([
                today,
                alert_id,
                park_code,
                park_name,
                alert_type,
                title,
                description,
                is_animal_related,
                animal_type
            ])


# read alerts.csv for analysis
alert_rows = []

with open(ALERTS_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        alert_rows.append(row)


# analyze the alert data
total_alerts = len(alert_rows)
animal_related_alerts = 0

animal_counts = {}
alert_type_counts = {}
park_counts = {}

for row in alert_rows:

    if row["is_animal_related"] == "True":

        animal_related_alerts = animal_related_alerts + 1

        animal = row["animal_type"]

        if animal in animal_counts:
            animal_counts[animal] = animal_counts[animal] + 1
        else:
            animal_counts[animal] = 1

        alert_type = row["alert_type"]

        if alert_type in alert_type_counts:
            alert_type_counts[alert_type] = alert_type_counts[alert_type] + 1
        else:
            alert_type_counts[alert_type] = 1

        park = row["park_name"]

        if park in park_counts:
            park_counts[park] = park_counts[park] + 1
        else:
            park_counts[park] = 1


# calculate percentage of animal-related alerts
if total_alerts == 0:
    percent_animal_related = 0
else:
    percent_animal_related = animal_related_alerts / total_alerts
    percent_animal_related = percent_animal_related * 100
    percent_animal_related = round(percent_animal_related, 2)


# create a list of parks and counts
park_list = []

for park in park_counts:
    park_list.append([park, park_counts[park]])


# sort parks from highest count to lowest count
park_list.sort(key=lambda item: item[1], reverse=True)


# get the top 5 parks
top_parks = park_list[:5]


# save results in a dictionary
results = {
    "run_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "total_alerts": total_alerts,
    "animal_related_alerts": animal_related_alerts,
    "percent_animal_related": percent_animal_related,
    "animal_counts": animal_counts,
    "animal_alerts_by_type": alert_type_counts,
    "top_parks": top_parks
}


# write results to results.json
with open(RESULTS_FILE, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)


print("Done.")
print("Total alerts:", total_alerts)
print("Animal alerts:", animal_related_alerts)
