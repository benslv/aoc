import re
import sys
from collections import defaultdict

lines = sys.stdin.read().splitlines()

part_zone = set()
gear_points = set()

gears = defaultdict(set)


def get_all_adjacent(y: int, x: int):
    points = []
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            dy = y + j
            dx = x + i
            if (j != 0 or i != 0) and dy >= 0 and dx >= 0 and dy < len(lines) and dx < len(lines[0]):
                points.append((y+j, x+i))

    return points


# Calculate the areas adjacent to symbols.
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if not char.isdigit() and char != ".":
            points = get_all_adjacent(y, x)
            part_zone.update(points)

            if char == "*":
                gear_points.add((y, x))


# # Second pass through for part numbers
is_part_num = False

part_1 = 0

for y, line in enumerate(lines):
    acc = ""
    points = []
    for x, char in enumerate(line):
        points += (y, x)
        if char.isdigit():
            acc += char

            if (y, x) in part_zone:
                is_part_num = True

        else:
            if is_part_num:
                part_1 += int(acc)
                is_part_num = False

            acc = ""

    if is_part_num:
        part_1 += int(acc)
        is_part_num = False

print(f"{part_1=}")


for gear in gear_points:
    adj = get_all_adjacent(*gear)

    nums = set()

    for y, x in adj:

        for match in re.finditer(r"\d+", lines[y]):
            if x >= match.span()[0] and x <= match.span()[1] - 1:
                gears[gear].add(int(match.group()))

two_gears = [val for val in gears.values() if len(val) == 2]

part_2 = sum(g1*g2 for g1, g2 in two_gears)

print(f"{part_2}")
