# Assumption:
# T moves to previous position of H if H moves and is no longer touching T
import sys

lines = sys.stdin.read().splitlines()

DY = {
    "U": 1,
    "D": -1,
    "L": 0,
    "R": 0
}

DX = {
    "U": 0,
    "D": 0,
    "L": -1,
    "R": 1
}

# [x, y]
h_pos = [0, 0]
prev_h_pos = (0, 0)
t_pos = (0, 0)

t_spaces = set()
t_spaces.add((0,0))

for line in lines:
    direction = line.split(" ")[0]
    distance = int(line.split(" ")[1])

    for _ in range(distance):
        prev_h_pos = tuple(h_pos)

        h_pos[0] += DX[direction]
        h_pos[1] += DY[direction]

        if abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1:
            t_pos = prev_h_pos
            t_spaces.add(t_pos)

part_1 = len(t_spaces)
print(f"Part 1: {part_1=}")