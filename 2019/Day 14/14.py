# 10 ORE => 10 A
# 1 ORE => 1 B
# 7 A, 1 B => 1 C
# 7 A, 1 C => 1 D
# 7 A, 1 D => 1 E
# 7 A, 1 E => 1 FUEL

from math import ceil
from collections import defaultdict


def parse_chem(c):
    units, name = c.split(" ")
    return int(units), name


reactions = {}  # Stores the reactions required for each product.
waste = {}  # Keeps track of any waste chemicals we could use in a reaction.

# Parse input and return chemical names and quantities in pairs.
for line in open("14.in").readlines():
    line = line.strip()
    inp, out = line.split(" => ")
    inputs = []

    for chem in inp.split(", "):
        inputs.append(parse_chem(chem))

    out_units, out_chem = parse_chem(out)
    reactions[out_chem] = (out_units, inputs)
print(reactions)


def min_ore(reactions, chem="FUEL", units=1, waste=None):
    """
    Depth First Search to calculate the units of ore required to produce a given chemical.
    """
    if waste is None:
        waste = defaultdict(int)

    if chem == "ORE":
        return units

    # 1. Reuse any waste chemicals we have.
    reuse = min(units, waste[chem])
    units -= reuse
    waste[chem] -= reuse

    # 2. Work out how many of the reaction to perform.
    produced, inputs = reactions[chem]
    n = ceil(units/produced)

    # 3. Calcuate the minimum ore required to produce every input.
    ore = 0

    for req, inp in inputs:
        ore += min_ore(reactions, inp, n*req, waste)

    waste[chem] += n*produced - units

    return ore


part_1 = min_ore(reactions)
print(part_1)


def max_fuel(reactions):
    """
    Calculates the upper bound on the amount of fuel you can make with 1 trillion ore, then performs a binary search to work out the max value.
    """
    trillion = 1000000000000
    lower = 0
    upper = 1

    # Upper bound
    while min_ore(reactions, units=upper) < trillion:
        lower = upper
        upper *= 2

    # Binary search to find max fuel
    while lower + 1 < upper:
        mid = (lower + upper) // 2
        ore = min_ore(reactions, units=mid)
        if ore > trillion:
            upper = mid
        elif ore < trillion:
            lower = mid

    return lower


part_2 = max_fuel(reactions)
print(part_2)
