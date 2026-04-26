def analyze(alert_rows):

    # count total alerts
    total_alerts = len(alert_rows)

    # initialize counters
    animal_related_alerts = 0

    animal_counts = {}
    alert_type_counts = {}
    park_counts = {}

    # loop through each row
    for row in alert_rows:

        # check if animal related
        if row["is_animal_related"] == "True":

            animal_related_alerts = animal_related_alerts + 1

            # count animal types
            animal = row["animal_type"]

            if animal in animal_counts:
                animal_counts[animal] = animal_counts[animal] + 1
            else:
                animal_counts[animal] = 1

            # count alert types
            alert_type = row["alert_type"]

            if alert_type in alert_type_counts:
                alert_type_counts[alert_type] = alert_type_counts[alert_type] + 1
            else:
                alert_type_counts[alert_type] = 1

            # count parks
            park = row["park_name"]

            if park in park_counts:
                park_counts[park] = park_counts[park] + 1
            else:
                park_counts[park] = 1

    # calculate percentage
    if total_alerts == 0:
        percent_animal = 0
    else:
        percent_animal = (animal_related_alerts / total_alerts) * 100
        percent_animal = round(percent_animal, 2)

    # find top 5 parks manually
    park_list = []

    for park in park_counts:
        park_list.append([park, park_counts[park]])

    # sort the list
    park_list.sort(key=lambda x: x[1], reverse=True)

    # take top 5
    top_parks = park_list[:5]

    # create results dictionary
    results = {
        "total_alerts": total_alerts,
        "animal_related_alerts": animal_related_alerts,
        "percent_animal_related": percent_animal,
        "animal_counts": animal_counts,
        "animal_alerts_by_type": alert_type_counts,
        "top_parks": top_parks
    }

    return results