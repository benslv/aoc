import sys

dx = {
    "forward": 1,
    "up": 0,
    "down": 0,
}

dy = {
    "forward": 0,
    "up": -1,
    "down": 1,
}

inp = [x.split() for x in sys.stdin.readlines()]


# Part 1

pos = 0
depth = 0

for dir, dist in inp:
    pos += dx[dir] * int(dist)
    depth += dy[dir] * int(dist)

print(f"Part 1: {pos*depth}")

# Part 2

pos = 0
depth = 0
aim = 0

for dir, dist in inp:
    if dir == "forward":
        pos += int(dist)
        depth += aim * int(dist)
    else:
        aim += dy[dir] * int(dist)

print(f"Part 2: {pos*depth}")