import sys
from collections import defaultdict

inp = sys.stdin.readlines()


def gen_points(x1, y1, x2, y2):
    step_x = -1 if x2 < x1 else 1
    step_y = -1 if y2 < y1 else 1

    if x1 == x2:
        for y in range(y1, y2 + step_y, step_y):
            yield (x1, y)

    elif y1 == y2:
        for x in range(x1, x2 + step_x, step_x):
            yield (x, y1)

    else:
        i = 0  # would be nice to remove this and do some clever maths instead
        for x in range(x1, x2 + step_x, step_x):
            y = y1 + i * step_y

            i += 1

            yield (x, y)


points = defaultdict(int)

for line in inp:
    (x1, y1), (x2, y2) = [list(map(int, coord.split(",")))
                          for coord in line.split(" -> ")]

    for point in gen_points(x1, y1, x2, y2):
        points[point] += 1


# Comment out lines 19 to 26 for Part 1.
print(f"Part 2: {sum([v > 1 for v in points.values()])}")
