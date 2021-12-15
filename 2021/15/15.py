import sys

inp = [[int(x) for x in line] for line in sys.stdin.read().splitlines()]
# inp = [[int(x) for x in line] for line in open(
#     "/home/ben/git/aoc/2021/15/15.3.test").read().splitlines()]


def solve(start, target, inp, part=1):

    inp_grid = {}

    for y in range(len(inp)):
        for x in range(len(inp[y])):
            inp_grid[(x, y)] = inp[y][x]

    grid_width = len(inp[0])
    grid_height = len(inp[0])

    distances = {(x, y): float("inf")
                 for x in range(len(inp[0])) for y in range(len(inp))}

    distances[(0, 0)] = 0

    if part == 2:
        inp_grid_copy = inp_grid.copy()

        for i in range(5):
            for j in range(5):
                # No adjustments to existing tile.
                if i + j == 0:
                    continue

                shift_x = grid_width * i
                shift_y = grid_height * j

                for (x, y), val in inp_grid_copy.items():
                    new_x = x + shift_x
                    new_y = y + shift_y

                    val += i+j

                    while val > 9:
                        val -= 9

                    inp_grid[(new_x, new_y)] = val
                    distances[(new_x, new_y)] = float("inf")

        grid_width *= 5
        grid_height *= 5

    unvisited = {(x, y) for x, y in inp_grid.keys()}

    visited = set()

    current = start
    adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while True:
        for x, y in adjacent:
            dx = current[0] + x
            dy = current[1] + y

            if dx in range(grid_width) and dy in range(grid_height):
                distances[(dx, dy)] = min(distances[(dx, dy)],
                                          distances[current] + inp_grid[(dx, dy)])

        unvisited -= {current}
        visited |= {current}

        if target in visited:
            return distances

        current = min([(node, distances[node])
                       for node in unvisited], key=lambda x: x[1])[0]


target = (len(inp)-1, len(inp)-1)

part_1 = solve((0, 0), target, inp)
print("Part 1:", part_1[target])

target2 = (5*(len(inp))-1, 5*(len(inp))-1)

part_2 = solve((0, 0), target2, inp, part=2)
print("Part 2:", part_2[target2])
