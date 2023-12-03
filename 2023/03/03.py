import sys

lines = sys.stdin.read().splitlines()

# with open("/home/ben/git/aoc/2023/03/03.in") as f:
#     lines = f.readlines()

part_zone = set()


def update_part_zone(y: int, x: int) -> None:
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            if not (j == 0 and i == 0):
                part_zone.add((y+j, x+i))


# Calculate the areas adjacent to symbols.
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if not char.isdigit() and char != ".":
            update_part_zone(y, x)

# # Second pass through for part numbers
is_part_num = False

part_1 = 0

for y, line in enumerate(lines):
    acc = ""
    for x, char in enumerate(line):
        if char.isdigit():
            acc += char

            if (y, x) in part_zone:
                is_part_num = True
        else:
            if is_part_num:
                part_1 += int(acc)
                is_part_num = False

            acc = ""

    if is_part_num:
        part_1 += int(acc)
        is_part_num = False


print(f"{part_1=}")
