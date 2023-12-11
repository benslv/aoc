import sys
from itertools import combinations

inp = sys.stdin.read().splitlines()

stars = [(y, x) for y in range(len(inp))
         for x in range(len(inp[y])) if inp[y][x] == "#"]

empty_cols = [x for x in range(len(inp[0])) if all(
    inp[y][x] == "." for y in range(len(inp)))]

empty_rows = [y for y in range(len(inp)) if all(
    inp[y][x] == "." for x in range(len(inp[y])))]

star_pairs = list(combinations(stars, 2))


def solve(expansion: int) -> int:
    ans = 0
    for (y1, x1), (y2, x2) in star_pairs:
        for y in range(min(y1, y2), max(y1, y2)):
            ans += expansion if y in empty_rows else 1

        for x in range(min(x1, x2), max(x1, x2)):
            ans += expansion if x in empty_cols else 1

    return ans


part_1 = solve(2)
print(f"{part_1=}")

part_2 = solve(1000000)
print(f"{part_2=}")
