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
    if not bags[colour].keys():  # If the bag contains no bags inside it.
        return False
    elif any("shiny gold" in colour for colour in bags[colour].keys()):
        return True
    else:
        return any([search(inner) for inner in bags[colour]])


part_1 = sum([search(colour) for colour, _ in bags.items()])

print(part_1)
