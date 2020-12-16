import sys
import re

fields, m, nearby = sys.stdin.read().split("\n\n")


ranges = {}

vals = set()

# Generate a set of numbers created from all of the upper and lower field ranges.
for line in fields.splitlines():
    parts = [int(x) for x in re.findall(r"([A-Za-z]+): (\d+)-(\d+) or (\d+)-(\d+)", line)[0][1:]]

    for i in range(parts[0], parts[1]+1):
        vals.add(i)

    for i in range(parts[2], parts[3]+1):
        vals.add(i)


# print(vals)

invalid = 0

for ticket in nearby.splitlines()[1:]:
    for val in [int(x) for x in ticket.split(",")]:
        if val not in vals:
            invalid += val
            break

print(invalid)