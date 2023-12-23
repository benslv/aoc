import sys

inp = sys.stdin.read().splitlines()

# obstacle = edge of board or square rock
# calculate distance to nearest obstacle in rolling direction
# count number of round rocks between obstacle and current position
# new position (roughly) = distance to obstacle - number of round rocks?

round_rocks = [(y, x) for y in range(len(inp))
               for x in range(len(inp[y])) if inp[y][x] == "O"]

square_rocks = [(y, x) for y in range(len(inp))
                for x in range(len(inp[y])) if inp[y][x] == "#"]

print(round_rocks)
print(square_rocks)
