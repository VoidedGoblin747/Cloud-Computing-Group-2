#!/usr/bin/env python3
import sys
import csv

# NYC Crime data is CSV, so use csv.reader to handle commas safely
reader = csv.reader(sys.stdin)

# Skip header row if present
header = True

for row in reader:
    if header:
        header = False
        continue

    try:
        # Adjust these indexes based on your dataset columns
        # Typical NYC crime dataset fields:
        # row[13] = BOROUGH
        # row[7]  = OFFENSE DESCRIPTION (crime type)
        borough = row[13].strip().upper()
        crime_type = row[7].strip().upper()

        if borough and crime_type:
            print(f"{borough}\t{crime_type}")

    except Exception:
        # Skip malformed rows
        continue
