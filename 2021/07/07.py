import sys

inp = list(map(int, sys.stdin.read().split(",")))


def dist(d):
    return d*(d+1)/2


part1 = min(sum(abs(val-x) for x in inp) for val in inp)

part2 = min(sum(dist(abs(val-x)) for x in inp)
            for val in range(min(inp), max(inp)+1))

print("Part 1:", int(part1))

print("Part 2:", int(part2))
