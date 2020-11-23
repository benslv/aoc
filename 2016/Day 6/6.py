from collections import Counter

with open("6.in", "r") as f:
    cols = list(zip(*f.read().splitlines()))


# Part 1
output = ""
for col in cols:
    output += Counter(col).most_common()[0][0]

print(f"Part 1: {output}")

# Part 2
output = ""
for col in cols:
    output += Counter(col).most_common()[-1][0]

print(f"Part 2: {output}")
