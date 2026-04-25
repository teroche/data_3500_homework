import requests
import csv
import json
import os
from datetime import datetime
from collections import Counter
from config import API_KEY

PARKS_URL = "https://developer.nps.gov/api/v1/parks"
ALERTS_URL = "https://developer.nps.gov/api/v1/alerts"

HEADERS = {
    "X-Api-Key": API_KEY
}

PARKS_FILE = "parks.csv"
ALERTS_FILE = "alerts.csv"
RESULTS_FILE = "results.json"

ANIMAL_KEYWORDS = {
    "bear": ["bear", "grizzly", "black bear"],
    "bison": ["bison"],
    "elk": ["elk"],
    "moose": ["moose"],
    "wolf": ["wolf", "wolves"],
    "coyote": ["coyote"],
    "mountain_lion": ["mountain lion", "cougar"],
    "snake": ["snake", "rattlesnake"],
    "bat": ["bat"],
    "deer": ["deer"],
    "alligator": ["alligator"],
    "wildlife": ["wildlife", "animal"]
}


def ensure_csv(file, headers):
    if not os.path.exists(file):
        with open(file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)


def append_row(file, row):
    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def get_existing_ids(file, column_name):
    ids = set()
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ids.add(row[column_name])
    return ids


def get_parks():
    params = {"limit": 500}
    r = requests.get(PARKS_URL, headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()["data"]


def get_alerts():
    params = {
        "limit": 500
    }

    r = requests.get(ALERTS_URL, headers=HEADERS, params=params)
    r.raise_for_status()

    data = r.json()
    return data.get("data", [])


def find_animal(text):
    text = text.lower()
    for animal, keywords in ANIMAL_KEYWORDS.items():
        for word in keywords:
            if word in text:
                return animal
    return ""


def save_parks(parks):
    today = datetime.now().strftime("%Y-%m-%d")
    existing = get_existing_ids(PARKS_FILE, "park_code")

    for p in parks:
        code = p.get("parkCode", "")
        if code in existing:
            continue

        append_row(PARKS_FILE, [
            today,
            code,
            p.get("fullName", ""),
            p.get("states", "")
        ])


def save_alerts(alerts, park_lookup):
    today = datetime.now().strftime("%Y-%m-%d")
    existing = get_existing_ids(ALERTS_FILE, "alert_id")

    for a in alerts:
        alert_id = a.get("id", "")
        if alert_id in existing:
            continue

        park_code = a.get("parkCode", "")
        park_name = park_lookup.get(park_code, "Unknown")
        title = a.get("title", "")
        description = a.get("description", "")
        category = a.get("category", "")

        text = title + " " + description
        animal = find_animal(text)

        append_row(ALERTS_FILE, [
            today,
            alert_id,
            park_code,
            park_name,
            category,
            title,
            description,
            "True" if animal else "False",
            animal
        ])


def read_alerts():
    rows = []
    with open(ALERTS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def analyze(rows):
    total = len(rows)
    animal_total = 0

    animal_counts = Counter()
    type_counts = Counter()
    park_counts = Counter()

    for r in rows:
        if r["is_animal_related"] == "True":
            animal_total += 1
            animal_counts[r["animal_type"]] += 1
            type_counts[r["alert_type"]] += 1
            park_counts[r["park_name"]] += 1

    percent = round((animal_total / total) * 100, 2) if total else 0

    return {
        "run_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_alerts": total,
        "animal_related_alerts": animal_total,
        "percent_animal_related": percent,
        "animal_counts": dict(animal_counts),
        "animal_alerts_by_type": dict(type_counts),
        "top_parks": park_counts.most_common(5)
    }


def save_results(results):
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)


def main():
    ensure_csv(PARKS_FILE, ["date_collected", "park_code", "park_name", "state"])
    ensure_csv(ALERTS_FILE, [
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

    parks = get_parks()
    save_parks(parks)

    park_lookup = {p["parkCode"]: p["fullName"] for p in parks if p.get("parkCode")}

    alerts = get_alerts()
    save_alerts(alerts, park_lookup)

    rows = read_alerts()
    results = analyze(rows)
    save_results(results)

    print("Done.")
    print("Total alerts:", results["total_alerts"])
    print("Animal alerts:", results["animal_related_alerts"])


if __name__ == "__main__":
    main()