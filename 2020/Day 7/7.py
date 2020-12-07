from collections import defaultdict
import fileinput

lines = [line.split() for line in fileinput.input()]

bags = defaultdict(dict)  # Stores which colour bags each bag contains.

# Parse input and construct dictionary of bag colours.
for line in lines:
    outer = " ".join(line[0:2])

    inners = {" ".join(line[4+i: 4+i+2]): line[4+i-1] for i in range(1, len(line[4:]), 4)}

    bags[outer] = inners if "other bags." not in inners else {}


def search(colour):
    if not bags[colour]:  # If the bag contains no bags inside it.
        return False
    elif "shiny gold" in bags[colour]:
        return True
    else:
        return any([search(inner) for inner in bags[colour]])


def search_num(colour):
    # If the bag contains no other bags, return one (for the bag itself).
    if not bags[colour]:
        return 1
    else:
        return sum([int(v)*search_num(k) for k, v in bags[colour].items()]) + 1


part_1 = sum([search(colour) for colour, _ in bags.items()])
print(f"Part 1: {part_1}")

# Don't want to include the outer bag in the count.
part_2 = search_num("shiny gold") - 1
print(f"Part 2: {part_2}")
