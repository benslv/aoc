import sys
from collections import Counter

template, rules = sys.stdin.read().split("\n\n")

rules = [rule.split(" -> ") for rule in rules.split("\n")]
rules = {k: v for k, v in rules}


def solve(n):
    pairs = Counter(template[i:i+2] for i in range(len(template)-1))
    chars = Counter(template)

    STEPS = n

    while STEPS > 0:
        for pair, n in pairs.copy().items():
            c = rules[pair]
            x, y = pair[0], pair[1]

            pairs[pair] -= n
            pairs[x+c] += n
            pairs[c+y] += n

            chars[c] += n

        STEPS -= 1

    return chars


part_1 = solve(10)
print(f"Part 1: {part_1.most_common()[0][1] - part_1.most_common()[-1][1]}")

part_2 = solve(40)
print(f"Part 2: {part_2.most_common()[0][1] - part_2.most_common()[-1][1]}")
