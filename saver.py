import json
import csv

# Function to save the data as JSON
def save_as_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

# Function to save the data as CSV
def save_as_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["headline", "url"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")
