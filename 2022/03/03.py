import sys

inp = sys.stdin.read().splitlines()

part_1 = 0

for bag in inp:
    l = len(bag)

    p1, p2 = bag[:l//2], bag[l//2:]

    common = list(set(p1) & set(p2))[0]

    if common.isupper():
        part_1 += ord(common) - 38
    else:
        part_1 += ord(common) - 96

print(f"{part_1=}")

part_2 = 0

for i in range(0, len(inp), 3):
    elf1, elf2, elf3 = inp[i:i+3]

    common = list(set(elf1) & set(elf2) & set(elf3))[0]

    if common.isupper():
        part_2 += ord(common) - 38
    else:
        part_2 += ord(common) - 96

print(f"{part_2=}")
