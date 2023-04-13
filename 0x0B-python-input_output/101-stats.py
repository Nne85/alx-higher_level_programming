#!/usr/bin/python3
"""
A module with a function that reads stdin line by line and computes metric
"""


import sys


def print_stats(file_size, status_codes):
    """
    reads stdin line by line and computes metrics
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    count = 0
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                    404: 0, 405: 0, 500: 0
                    }

    try:
        for line in sys.stdin:
            count += 1
            split_line = line.split(" ")
            if len(split_line) < 3:
                continue
            file_size += int(split_line[-1])
            code = int(split_line[-2])
            if code in status_codes:
                status_codes[code] += 1

            if count % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_stats(file_size, status_codes)
