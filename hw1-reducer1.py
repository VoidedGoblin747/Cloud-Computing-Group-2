#!/usr/bin/env python3
import sys

# This reducer receives sorted lines from the mapper in the format:
#   borough\tcrime_type
#
# Since the input is sorted by key (borough), all lines for the same
# borough arrive together. We count total crimes per borough and
# collect unique crime types per borough.

current_borough = None
current_count = 0
crime_types = set()

# Store results for all boroughs so we can find the max at the end
borough_data = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Split on tab — mapper outputs: borough\tcrime_type
    parts = line.split('\t')
    if len(parts) != 2:
        continue

    borough, crime_type = parts

    # If we encounter a new borough, save the previous one's data
    if borough != current_borough:
        if current_borough is not None:
            borough_data[current_borough] = {
                'count': current_count,
                'crimes': crime_types
            }
        current_borough = borough
        current_count = 0
        crime_types = set()

    current_count += 1
    crime_types.add(crime_type)

# Don't forget to save the last borough
if current_borough is not None:
    borough_data[current_borough] = {
        'count': current_count,
        'crimes': crime_types
    }

# Find the borough with the most crimes
max_borough = max(borough_data, key=lambda b: borough_data[b]['count'])
max_count = borough_data[max_borough]['count']
max_crimes = borough_data[max_borough]['crimes']

# Print the required output format
print(f"Most of the crimes were reported in {max_borough}.")
print(f"Total number of crimes reported in {max_borough} is {max_count}.")
print(f"Crime types reported in {max_borough} are {', '.join(sorted(max_crimes))}.")
