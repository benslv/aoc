import sys

inp = list(map(int, sys.stdin.read().split(",")))


def solve(days):
    fishes = [x for x in inp]

    DAYS = days

    while DAYS > 0:
        for _ in range(fishes.count(0)):
            fishes.append(9)

        fishes = [x - 1 if x > 0 else 6 for x in fishes]

        # print(fishes.count(0), fishes)

        DAYS -= 1

    return len(fishes)

print("Part 1:", solve(80))
print("Part 2:", solve(256))