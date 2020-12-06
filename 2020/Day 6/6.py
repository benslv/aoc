from functools import reduce

lines = open("6.in").read().split("\n\n")

part_1 = sum([len(set("".join(group.replace("\n", "")))) for group in lines])

print(f"Part 1: {part_1}")

part_2 = sum([(len(reduce(lambda a, b: set(a) & set(b), group.split("\n")))) for group in lines])

print(f"Part 2: {part_2}")

