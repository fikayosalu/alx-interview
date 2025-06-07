#!/usr/bin/python3
""" 0-stats """

import sys
import re
from collections import defaultdict

# Allowed status codes
VALID_STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Counters
total_size = 0
status_counts = defaultdict(int)
line_count = 0

# Regex pattern to validate and extract fields
log_pattern = re.compile(
    r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Prints the collected metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(VALID_STATUS_CODES):
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            ip, date, status, size = match.groups()
            total_size += int(size)
            if status in VALID_STATUS_CODES:
                status_counts[status] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Print stats one final time if not already printed due to 10-line mark
if line_count % 10 != 0:
    print_stats()
