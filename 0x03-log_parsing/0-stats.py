#!/usr/bin/env python3
"""Log parsing script"""
import re
import sys

file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        line_data = re.search(r'(\d+.\d+.\d+.\d+)\s-\s\[(.*?)\]\s"GET\s\/projects\/260\sHTTP\/1.1"\s(\d+)\s(\d+)', line)
        if line_data:
            ip_address, date, status_code, file_size_line = line_data.groups()
            file_size += int(file_size_line)
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            print(f'File size: {file_size}')
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f'{code}: {status_codes[code]}')

except KeyboardInterrupt:
    print(f'File size: {file_size}')
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f'{code}: {status_codes[code]}')
