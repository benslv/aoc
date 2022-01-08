import sys

inp = list(map(int, sys.stdin.read().split(",")))


def solve(inp, days):
    DAYS = days

    fishes = {x: inp.count(x) for x in range(9)}

    while DAYS > 0:
        next_fishes = {x: 0 for x in range(9)}

        for time, num in fishes.items():

            if time == 0:
                next_fishes[6] += num
                next_fishes[8] += num
            else:
                next_fishes[time-1] += num

        fishes = next_fishes

        DAYS -= 1

    return sum(fishes.values())


print("Part 1:", solve(inp, 80))
print("Part 2:", solve(inp, 256))
