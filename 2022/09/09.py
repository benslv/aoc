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


def move_tail(head, tail):
    t_x, t_y = tail[0], tail[1]

    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        if head[0] > tail[0]:
            t_x += 1
        elif head[0] < tail[0]:
            t_x -= 1

        if head[1] > tail[1]:
            t_y += 1
        elif head[1] < tail[1]:
            t_y -= 1

    return (t_x, t_y)


def part_1():
    h_pos = [0, 0]
    t_pos = (0, 0)

    t_spaces = set()
    t_spaces.add((0, 0))

    for line in lines:
        direction, distance = line.split(" ")

        for _ in range(int(distance)):
            h_pos[0] += DX[direction]
            h_pos[1] += DY[direction]

            t_pos = move_tail(h_pos, t_pos)
            t_spaces.add(t_pos)

    return len(t_spaces)


print(f"Part 1: {part_1()=}")


def part_2():
    knots = [(0, 0) for _ in range(10)]
    t_spaces = set()
    t_spaces.add((0, 0))

    for line in lines:
        direction, distance = line.split(" ")

        for _ in range(int(distance)):

            knots[0] = (knots[0][0] + DX[direction],
                        knots[0][1] + DY[direction])

            for i in range(1, len(knots)):
                knots[i] = move_tail(knots[i-1], knots[i])

            t_spaces.add(knots[9])

    return len(t_spaces)


print(f"Part 2: {part_2()=}")
