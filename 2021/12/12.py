import sys
from collections import defaultdict

inp = [line.strip().split("-") for line in sys.stdin.readlines()]

neighbours = defaultdict(list)


for a, b in inp:
    neighbours[a].append(b)
    neighbours[b].append(a)


def search(current, seen=set(), part=1):
    if current == "end":
        return 1

    if current in seen:
        if current == "start":
            return 0

        if current.islower():
            if part == 1:
                return 0
            else:
                part = 1

    return sum(search(cave, seen | {current}, part) for cave in neighbours[current])


print(search("start", part=1))
print(search("start", part=2))
