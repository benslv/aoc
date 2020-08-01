poly = list(open("day5.txt", "r").read())


def react(poly):
    reacted = None
    while reacted or reacted is None:
        reacted = False
        i = 0
        while i < len(poly) - 1:
            if poly[i] == poly[i+1].swapcase():
                del poly[i]
                del poly[i]

                reacted = True
            i += 1

        if not reacted:
            break

    return poly


# Part 1
part_1 = react(poly)
print(f"Part 1: {len(part_1)}")

# Part 2
units = set()
for char in poly:
    units.add(char.lower())

min_length = None

for char in units:
    removed_poly = [x for x in poly if x not in [char, char.upper()]]
    reaction = len(react(removed_poly))
    if min_length is None or reaction < min_length:
        min_length = reaction

print(f"Part 2: {min_length}")
