#!/usr/bin/python3
""" Log parsing task module """
import sys

# Variable Initialization
status_codes = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
size = 0
count = 0


def output():
    # Create the syntax of the program output
    print(f"File size: {size}")
    for item, value in status_codes.items():
        if value > 0:
            print(f"{item}: {value}")


try:
    # Read the stdin line by line
    for line in sys.stdin:
        result = line.split(" ")

        try:
            code = int(result[-2])  # Extract the status code
            size += int(result[-1])  # Extract file size
        except (TypeError, ValueError):
            continue

        if code in status_codes:
            status_codes[code] += 1

        count += 1
        # Print output after 10 lines
        if count % 10 == 0:
            output()
# Print output when Ctrl+c is pressed
except KeyboardInterrupt:
    output()
