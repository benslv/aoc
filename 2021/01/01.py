import sys

inp = list(map( int, (sys.stdin.readlines())))

part_1 = 0
depth = None

for line in inp:
    if depth != None and line > depth:
        part_1 += 1

    depth = line

print(f"Part 1: {part_1}")

part_2 = 0
depth = None

for i in range(len(inp) - 2):

    new_depth = sum(inp[i:i+3])

    if depth != None and new_depth > depth:
        part_2 += 1

    depth = new_depth

print(f"Part 2: {part_2}")
