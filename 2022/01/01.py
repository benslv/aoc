import sys

inp = [sum(map(int, elf.split("\n")))
       for elf in sys.stdin.read().split("\n\n")]

part_1 = max(inp)

print(f"{part_1=}")

part_2 = sum(sorted(inp)[-3:])

print(f"{part_2}")
