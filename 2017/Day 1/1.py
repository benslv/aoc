import sys

inp = sys.stdin.read()

part_1 = sum([int(inp[i]) for i in range(len(inp)-1, -1, -1) if inp[i] == inp[i-1]])

print(f"Part 1: {part_1}")

part_2 = sum([int(inp[i]) for i in range(len(inp)-1, -1, -1) if inp[i] == inp[i-(len(inp)//2)]])

print(f"Part 2: {part_2}")