import sys

inp = sys.stdin.read().splitlines()

part_1 = 0
for pair in inp:
    e1, e2 = pair.split(",")

    e1_lower, e1_upper = map(int, e1.split("-"))
    e2_lower, e2_upper = map(int, e2.split("-"))

    if (e1_lower >= e2_lower and e1_upper <= e2_upper) or (e2_lower >= e1_lower and e2_upper <= e1_upper):
        part_1 += 1

print(f"{part_1=}")

part_2 = 0
for pair in inp:
    e1, e2 = pair.split(",")

    e1_lower, e1_upper = map(int, e1.split("-"))
    e2_lower, e2_upper = map(int, e2.split("-"))

    if (e1_lower >= e2_lower and e1_lower <= e2_upper) or (e2_lower >= e1_lower and e2_lower <= e1_upper):
        part_2 += 1

print(f"{part_2=}")
