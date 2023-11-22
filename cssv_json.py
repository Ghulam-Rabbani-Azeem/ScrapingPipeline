import csv
import json

csv_file = 'Directory/tesla-stock-price.csv'  # Replace with your CSV file name
json_file = 'output.json'  # Replace with the desired output JSON file name

# Read data from CSV and convert to JSON
data = []
with open(csv_file, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        data.append(row)

# Write data to a JSON file
with open(json_file, 'w') as jsonfile:
    jsonfile.write(json.dumps(data, indent=4))  # Indent for pretty formatting (optional)
