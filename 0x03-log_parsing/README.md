# Log Parsing Script

## Overview

This script reads log entries from `stdin`, processes them line by line, and computes useful metrics, including the total file size and counts of different HTTP status codes. It prints the results after every 10 lines or when a keyboard interruption (CTRL+C) is received.

## Concepts Used

The following concepts were applied in the development of this script:

1. **File I/O in Python**:
   - Reading data from `stdin` line by line and processing each line.

2. **Signal Handling in Python**:
   - Handling `KeyboardInterrupt` (CTRL+C) to allow the program to exit gracefully and display the results at any point during execution.

3. **Data Processing**:
   - Extracting specific data points (such as status code and file size) from each log entry for further analysis.

4. **Dictionaries in Python**:
   - Storing and counting occurrences of various HTTP status codes using a dictionary for efficient lookups and updates.

5. **Exception Handling**:
   - Handling various exceptions, such as `ValueError`, during data extraction and ensuring the program continues running even when encountering malformed input.

## Requirements

- Python 3.x

### Each log line should have the following format:

&lt;IP Address&gt; - [&lt;date&gt;] "GET /projects/260 HTTP/1.1" &lt;status code&gt; &lt;file size&gt;

## Example Output

After processing 10 lines (or a keyboard interrupt), the script will output the following:

```bash
File size: 3500
200: 3
301: 1
404: 6
