with open("1.in", "r") as f:
    directions = f.read().split(", ")

# 0 = N
# 1 = E
# 2 = S
# 3 = W
bearing = 0

x = 0
y = 0

dX = {0: 0, 1: 1, 2: 0, 3: -1}
dY = {0: 1, 1: 0, 2: -1, 3: 0}

turn = {"L": -1, "R": 1}

points = set()
prev_len = 0
found_hq = False

for d in directions:
    direction, dist = d[0], int(d[1:])

    bearing = (bearing + turn[direction]) % 4

    for _ in range(dist):
        x += dX[bearing]
        y += dY[bearing]

        # Part 2
        points.add((x, y))
        if len(points) == prev_len and not found_hq:
            print(f"Part 2: {abs(x)+abs(y)}")
            found_hq = True
        else:
            prev_len = len(points)


# Part 1
print(f"Part 1: {abs(x) + abs(y)}")
