import sys
from copy import deepcopy

lines = [list(line.rstrip()) for line in sys.stdin]


def get_empty_neighbours(x, y, seats):
    # Create matrix of relative coordinates to adjacent seats.
    adjacency = [(i, j) for i in (-1, 0, 1)
                 for j in (-1, 0, 1) if not (i == j == 0)]

    count = 0
    # For each adjacent cell...
    for dx, dy in adjacency:
        # ...check that it's within the boundaries of the seating grid.
        if 0 <= (x + dx) < len(seats[dy]) and 0 <= (y + dy) < len(seats):
            # ...increment the count if it's occupied.
            count += seats[y+dy][x+dx] == "#"

    return count


def get_empty_neighbours_2(x, y, seats):
    # Create matrix of relative coordinates to adjacent seats.
    adjacency = [(i, j) for i in (-1, 0, 1)
                 for j in (-1, 0, 1) if not (i == j == 0)]

    count = 0
    # For each direction to a "neighbour" cell...
    for i, j in adjacency:
        # ...initially check a distance of 1 away (i.e. literally adjacent)
        distance = 1
        while True:
            # ...calculate the absolute coordinate of the cell.
            dx = i * distance + x
            dy = j * distance + y

            # ...check that the cell is within the boundaries of the seating grid.
            if not(0 <= (dx) < len(seats[y]) and 0 <= (dy) < len(seats)):
                break

            # ...check whether the cell contains a seat, and whether it's occupied.
            if seats[dy][dx] == "#":
                count += 1
                break
            elif seats[dy][dx] == "L":
                break

            # If no seat was found, increase the distance by 1 and check again.
            distance += 1

    return count


def step(seats, count_function, vos=4):
    next_state = deepcopy(seats)

    # Iterate through all the cells in the grid.
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            # If the cell contains a seat...
            if seats[y][x] != ".":
                # ...calculate how many adjacent cells are occupied seats
                adj = count_function(x, y, seats)
                if adj == 0:
                    next_state[y][x] = "#"
                elif adj >= vos:
                    next_state[y][x] = "L"

    return next_state


seats = deepcopy(lines)
prev_seats = []

# Step through the simulation until there's no change between two iterations.
while prev_seats != seats:
    prev_seats = seats
    seats = step(seats, get_empty_neighbours)

# Count the number of occupied seats in the final seating grid.
part_1 = sum([row.count("#") for row in seats])
print(f"Part 1: {part_1}")


seats = deepcopy(lines)
prev_seats = []

# Step through the simulation until there's no change between two iterations.
while prev_seats != seats:
    prev_seats = seats
    # Same as above, but the number of occupied seats required for a 
    seats = step(seats, get_empty_neighbours_2, vos=5)

# Count the number of occupied seats in the final seating grid.
part_2 = sum([row.count("#") for row in seats])
print(f"Part 2: {part_2}")
