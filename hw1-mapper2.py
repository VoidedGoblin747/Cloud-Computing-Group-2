#!/usr/bin/env python3
from csv import reader
import sys

# This mapper reads the NYC crime CSV and filters for "DANGEROUS WEAPONS" crimes.
# For each matching row, it extracts the month from the report date and outputs:
#   month_number\t1
#
# We use month_number (01, 02, ... 12) as the key so that sorting
# groups all entries for the same month together for the reducer.
#
# CSV columns used:
#   line[1]  = rpt_dt (report date, format like "09/30/2016" or "2016-09-30")
#   line[7]  = ofns_desc (crime type description)

for line in reader(sys.stdin):
    # Get the crime type (column 7) and report date (column 1)
    crime_type = line[7].strip()
    date_str = line[1].strip()

    # Skip header row or empty values
    if not crime_type or not date_str or crime_type == "OFNS_DESC":
        continue

    # Only process "DANGEROUS WEAPONS" crimes
    if crime_type != "DANGEROUS WEAPONS":
        continue

    # Extract month and year from the date
    # Date format could be "MM/DD/YYYY" or "YYYY-MM-DD"
    if '/' in date_str:
        # Format: MM/DD/YYYY
        parts = date_str.split('/')
        month = parts[0]
        year = parts[2]
    elif '-' in date_str:
        # Format: YYYY-MM-DD
        parts = date_str.split('-')
        month = parts[1]
        year = parts[0]
    else:
        continue

    # Only count crimes from 2016
    if year != "2016":
        continue

    # Output: month_number\t1
    print(f"{month}\t1")
