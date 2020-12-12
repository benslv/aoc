import sys

lines = [x.rstrip() for x in sys.stdin]


def part_1():
    # 0 = N
    # 1 = E
    # 2 = S
    # 3 = W
    bearing = 1

    x = 0
    y = 0

    dX = {0: 0, 1: 1, 2: 0, 3: -1, "N": 0, "S": 0, "E": 1, "W": -1}
    dY = {0: 1, 1: 0, 2: -1, 3: 0, "N": 1, "S": -1, "E": 0, "W": 0}

    turn = {"L": -1, "R": 1}

    for line in lines:
        direction, value = line[0], int(line[1:])

        if direction in "LR":
            value /= 90
            bearing = (bearing + turn[direction]*value) % 4

        elif direction in "NSEW":
            x += dX[direction]*value
            y += dY[direction]*value

        elif direction == "F":
            x += dX[bearing]*value
            y += dY[bearing]*value

    return abs(x) + abs(y)


print(f"Part 1: {part_1()}")


def part_2():
    # Ship coordinates
    x = 0
    y = 0

    # Waypoint coordinates (relative to ship)
    wx = 10
    wy = 1

    w_dX = {"N": 0, "S": 0, "E": 1, "W": -1}
    w_dY = {"N": 1, "S": -1, "E": 0, "W": 0}

    for line in lines:
        direction, value = line[0], int(line[1:])

        if direction in "NSEW":
            wx += w_dX[direction]*value
            wy += w_dY[direction]*value

        elif direction in "L":
            for _ in range(value // 90):
                wx, wy = -wy, wx

        elif direction == "R":
            for _ in range(value // 90):
                wx, wy = wy, -wx

        elif direction == "F":
            x += wx * value
            y += wy * value

    return abs(x) + abs(y)


print(f"Part 2: {part_2()}")
