#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

args = sys.argv[1:]
# Get all arguments except for the first (which is the script name)

total = 0
for arg in args:
    total += int(arg)

print(total)
