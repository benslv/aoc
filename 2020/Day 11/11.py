import fileinput
from copy import deepcopy

lines = [list(line.rstrip()) for line in fileinput.input()]

"""
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
"""


def get_empty_neighbours(x: int, y: int, seats: list[str]) -> int:
    adjacency = [(i, j) for i in (-1, 0, 1)
                 for j in (-1, 0, 1) if not (i == j == 0)]

    count = 0
    for dx, dy in adjacency:
        if 0 <= (x + dx) < len(seats[dy]) and 0 <= (y + dy) < len(seats):
            count += seats[y+dy][x+dx] == "#"

    return count


def get_empty_neighbours_2(x, y, seats):
    adjacency = [(i, j) for i in (-1, 0, 1)
                 for j in (-1, 0, 1) if not (i == j == 0)]

    count = 0
    for i, j in adjacency:
        distance = 1
        while True:
            dx = i * distance
            dy = j * distance

            if 0 <= (x + dx) < len(seats[y]) and 0 <= (y + dy) < len(seats):
                if seats[y+dy][x+dx] == "#":
                    count += 1
                    break
                elif seats[y+dy][x+dx] == "L":
                    break
            else:
                break

            distance += 1

    return count


def step(seats, count_function, vos=4):
    next_state = deepcopy(seats)

    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if seats[y][x] != ".":
                adj = count_function(x, y, seats)
                if adj == 0:
                    next_state[y][x] = "#"
                elif adj >= vos:
                    next_state[y][x] = "L"

    return next_state


seats = deepcopy(lines)
prev_seats = []

while prev_seats != seats:
    prev_seats = seats
    seats = step(seats, get_empty_neighbours)

part_1 = sum([row.count("#") for row in seats])
print(f"Part 1: {part_1}")


seats = deepcopy(lines)
prev_seats = []

while prev_seats != seats:
    prev_seats = seats
    seats = step(seats, get_empty_neighbours_2, vos=5)

part_2 = sum([row.count("#") for row in seats])
print(f"Part 2: {part_2}")
