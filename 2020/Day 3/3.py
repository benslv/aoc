import fileinput

lines = [line.strip() for line in fileinput.input()]

x = 0
part_1 = 0

for line in lines:
    part_1 += line[x] == "#"
    x = (x + 3) % len(line)

print("Part 1:", part_1)

# Right, Down
slopes = [[1, 1],
          [3, 1],
          [5, 1],
          [7, 1],
          [1, 2]]


# Init at 1 because multiplying onto it.
part_2 = 1

for (dx, dy) in slopes:
    x, y = 0, 0
    trees = 0
    while y < len(lines):
        trees += lines[y][x] == "#"
        x = (x + dx) % len(lines[y])
        y = (y + dy)
    part_2 *= trees

print("Part 2:", part_2)
