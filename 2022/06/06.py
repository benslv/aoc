import sys

inp = sys.stdin.read().strip()


def solve(length):
    for i in range(length, len(inp)):
        if len(set(inp[i-length:i])) == length:
            return i


part_1 = solve(4)
print(f"{part_1=}")

part_2 = solve(14)
print(f"{part_2=}")
