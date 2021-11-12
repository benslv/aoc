import sys
import re
from collections import Counter

inp = sys.stdin

weights = {}
children = {}

for line in inp:
    info = line.strip().split(" -> ")

    name, weight, *subtowers = re.findall(r"\w+", line)

    weights[name] = int(weight)
    children[name] = list(subtowers)

# Flatten the list of children to find all towers which are supported by some other.
supported = {c for child in children.values() for c in child}

# Figure out which towers aren't supported by another.
unsupported = [child for child in children if child not in supported]

part_1 = unsupported[0]

print("Part 1:", part_1)

def total_weight(label):
    if not children[label]:
        return weights[label]

    child_weights = [total_weight(child) for child in children[label]]

    if len(set(child_weights)) > 1:
        (correct, _), (incorrect, _) = Counter(child_weights).most_common()

        return(correct - incorrect + weights[children[label][child_weights.index(incorrect)]])

    return weights[label] + sum(child_weights)

print("Part 2:", total_weight(part_1))