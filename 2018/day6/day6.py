from collections import defaultdict

data = [list(map(int, i.split(", ")))
        for i in open("day6.txt", "r").readlines()]


def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


max_x = max(list(zip(*data))[0])
max_y = max(list(zip(*data))[1])

grid = {}

"""
Determine which of the named coordinates each grid square is closest to.
Produces a dictionary with tuples for keys, and the named coordinates as values.
Named coordinate is marked as "-1" if it is equidistant between two named coordinates.
"""
for x in range(max_x):
    for y in range(max_y):
        min_dist = min(manhattan([x, y], [i, j])for i, j in data)
        for n, (i, j) in enumerate(data):
            if manhattan([x, y], [i, j]) == min_dist:
                if grid.get((x, y), -1) != -1:
                    grid[(x, y)] = -1
                    break
                grid[(x, y)] = n

# print(f"Grid: {grid}")


"""
Determine which of the named coordinates have infinite areas.
This is done by seeing which named coordinates "have" grid squares lying on the edge of the grid.
"""
infinite_points = set()

for k, v in grid.items():
    if k[0] in [0, max_x] or k[1] in [0, max_y]:
        infinite_points.add(grid[k])

# print(f"Infinite Points: {infinite_points}")

"""
Count the number of occurrences of each named coordinate in our grid, ignoring equidistant points
or coordinates with infinite area.
"""

counts = defaultdict(int)

for v in grid.values():
    if v != -1 and v not in infinite_points:
        counts[v] += 1

print(f"Part 1: {max(counts.values())}")


"""
Iterate through each grid square and calculate the total Manhattan distance to each named
coordinate.
If it's less than 10000, add it to a list of points.
"""
valid_points = []
for x in range(max_x):
    for y in range(max_y):
        distance = sum([manhattan([x, y], [i, j]) for i, j in data])
        if distance < 10000:
            valid_points.append((x, y))

print(f"Part 2: {len(valid_points)}")
