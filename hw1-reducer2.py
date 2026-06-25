#!/usr/bin/env python3
import sys

month_names = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
        }

current_month = None
current_count = 0

print("DANGEROUS WEAPONS reported per month:")

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    month, count = line.split('\t')
    count = int(count)

    if current_month == month:
        current_count += count
    else:
        if current_month is not None:
            print(f"{month_names[current_month]} {current_count}")

        current_month = month
        current_count = count

if current_month is not None:
    print(f"{month_names[current_month]} {current_count}")
