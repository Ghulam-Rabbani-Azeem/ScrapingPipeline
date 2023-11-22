import gdown
import pandas as pd

# Replace the URL with the direct download link of the CSV file
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTgHcm8rLgPUtL4u6Srgaybkl-Vm3p5RoYz5QJXlkD1JExRsZiGQf5XpBS8YJDK_Pus6mJFIsz0-8i4/pub?output=csv'

output_csv = 'file.csv'  # Local file name to save the downloaded CSV
output_json = 'file.json'  # Local file name to save the JSON data

# Download CSV file
gdown.download(url, output_csv, quiet=False)

# Read CSV file into a pandas DataFrame
data = pd.read_csv(output_csv)

# Convert DataFrame to JSON and save to file
data.to_json(output_json, orient='records')

print(f'CSV file downloaded as "{output_csv}" and converted to JSON as "{output_json}"')
