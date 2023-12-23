import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

inp = sys.stdin.read().splitlines()

grid = {
    (y, x): inp[y][x] for y in range(len(inp)) for x in range(len(inp[y]))
}

start = (0, 1)
finish = (len(inp)-1, len(inp[0])-2)


def is_valid_direction(dy, dx, char):
    match char:
        case "<":
            return dx < 0
        case ">":
            return dx > 0
        case "^":
            return dy < 0
        case "v":
            return dy > 0


def get_valid_routes(position, ignore_slopes):
    [y, x] = position

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if abs(dy) != abs(dx):
                if ignore_slopes and grid.get((y+dy, x+dx), "#") != "#":
                    yield (y+dy, x+dx)
                else:
                    match char := grid.get((y+dy, x+dx), "#"):
                        case ".":
                            yield (y+dy, x+dx)
                        case "<" | ">" | "^" | "v":
                            if is_valid_direction(dy, dx, char):
                                yield (y+dy, x+dx)


def DFS(start, finish, ignore_slopes=False):
    paths = []

    def traverse(path):
        current_point = path[-1]

        if current_point == finish:
            paths.append(path)
            return

        for route in get_valid_routes(current_point, ignore_slopes):
            if route not in path:
                traverse([*path, route])

    traverse([start])

    return paths


part_1 = max(len(path) for path in DFS(start, finish)) - 1

print(f"{part_1=}")

junctions = {start}
junc_distances = defaultdict(list)

for pos in grid:
    if len([x for x in get_valid_routes(pos, ignore_slopes=True) if grid[pos] != "#"]) > 2:
        junctions.add(pos)

junctions.add(finish)

# BFS distances between junctions
for j in junctions:
    queue = [j]
    seen = {j}
    distance = 1

    while len(queue) > 0:
        next_queue = []

        for pos in queue:
            for route in get_valid_routes(pos, ignore_slopes=True):
                if route in seen:
                    continue

                if route in junctions:
                    junc_distances[j].append((distance, route))
                else:
                    next_queue.append(route)

                seen.add(route)

        distance += 1
        queue = next_queue


def part2(path):
    paths = []

    def DFS(path, distance):
        current_point = path[-1]

        if current_point == finish:
            paths.append((distance, path))
            return

        for d, point in junc_distances[current_point]:
            if point not in path:
                DFS([*path, point], distance + d)

    DFS(path, 0)

    return paths


part_2 = max((path for path in part2([start])), key=lambda x: x[0])[0]


print(f"{part_2=}")
