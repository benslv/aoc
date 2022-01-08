import sys
from collections import Counter
from functools import reduce

inp = [[int(x) for x in line.strip()] for line in sys.stdin.readlines()]

part_1 = 0

for y in range(len(inp)):
    for x in range(len(inp[y])):
        cell = inp[y][x]

        adjacent = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

        if all(cell < inp[y][x] for y, x in adjacent if y in range(len(inp)) and x in range(len(inp[y]))):
            part_1 += 1 + cell

print("Part 1:", part_1)


def basin(y, x):
    adjacent = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

    downhill = None

    for (dy, dx) in adjacent:
        if dy in range(len(inp)) and dx in range(len(inp[y])) and inp[dy][dx] < inp[y][x]:
            downhill = (dy, dx)

    if downhill == None:
        return (y, x)

    return basin(*downhill)


basins = []

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] != 9:
            basins.append(basin(y, x))

c = Counter(basins)

print("Part 2:", reduce(lambda a, b: a*b, [x[1] for x in c.most_common(3)]))
