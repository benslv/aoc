import sys

points, folds = sys.stdin.read().split("\n\n")

points = [tuple(map(int, point.split(","))) for point in points.split("\n")]

paper = {(x, y): True for x, y in points}
paper2 = {(x, y): True for x, y in points}

part_1 = None

folds = folds.split("\n")

for fold in folds:

    d, v = fold.split(" ")[2].split("=")

    v = int(v)

    if d == "x":
        for x, y in paper:
            if x > v:
                paper2[(v - (x-v), y)] = True
                paper2.pop((x, y), None)
    elif d == "y":
        for x, y in paper:
            if y > v:
                paper2[(x, v - (y-v))] = True
                paper2.pop((x, y), None)

    paper = paper2.copy()

    if part_1 == None:
        part_1 = sum(point for point in paper.values())

print("Part 1:", part_1)

X = max(x for x, _ in paper.keys())
Y = max(y for _, y in paper.keys())

print("Part 2:")

for y in range(Y+1):
    for x in range(X+1):
        print("X" if paper2.get((x, y), False) else " ", end="")
    print("")
