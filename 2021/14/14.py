import sys
from collections import Counter

template, rules = sys.stdin.read().split("\n\n")

rules = [rule.split(" -> ") for rule in rules.split("\n")]
insertions = {k: v for k, v in rules}

# Slow for Part 2 (n=40)
for _ in range(10):
    next_template = ""
    for i in range(len(template)-1):
        next_template += template[i]
        next_template += insertions[template[i:i+2]]
    next_template += template[-1]
    template = next_template

c = Counter(template)

print(f"Part 1: {c.most_common()[0][1] - c.most_common()[-1][1]}")
