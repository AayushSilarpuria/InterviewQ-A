import json
import csv

# Load the JSON file
with open("build.json", "r") as f:
    data = json.load(f)

# Extract information for the 1st CSV file
csv1_rows = [["Field Name", "label", "count"]]
for item in data:
    field_name = item["field_name"]
    label = item["label"]
    count = item["count"]
    csv1_rows.append([field_name, label, count])

# Write the 1st CSV file
with open("csv1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv1_rows)

# Extract information for the 2nd CSV file
csv2_rows = [["Field Name", "label", "attribute_name", "attribute_value", "attribute_count"]]
for item in data:
    field_name = item["field_name"]
    label = item["label"]
    for attribute in item["attributes"]:
        attribute_name = attribute["attribute_name"]
        attribute_value = attribute["attribute_value"]
        attribute_count = attribute["count"]
        csv2_rows.append([field_name, label, attribute_name, attribute_value, attribute_count])

# Write the 2nd CSV file
with open("csv2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv2_rows)

# Print a message indicating that the CSV files have been created successfully
print("CSV files have been created successfully!")
