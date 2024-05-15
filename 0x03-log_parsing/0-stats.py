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

try:
    for i, line in enumerate(sys.stdin, 1):
        line_data = re.search(r'(\d+.\d+.\d+.\d+)\s-\s\[(.*?)\]\s"GET\s\/projects\/260\sHTTP\/1.1"\s(\d+)\s(\d+)', line)
        if line_data:
            ip_address, date, status_code, file_size_line = line_data.groups()
            file_size += int(file_size_line)
            status_codes[status_code] += 1

        if i % 10 == 0:
            print(f'File size: {file_size}')
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f'{code}: {count}')

except KeyboardInterrupt:
    print(f'File size: {file_size}')
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f'{code}: {count}')
