A, B = open("Day 3/3.in", "r").read().split("\n")
A = A.split(",")
B = B.split(",")


def get_points(line):
    points = {}
    dX = {"L": -1, "R": 1, "U": 0, "D": 0}
    dY = {"L": 0, "R": 0, "U": 1, "D": -1}
    x, y = 0, 0
    length = 0

    # Iterate through each command in the line, keeping track of every point that we pass through.
    for cmd in line:
        d = cmd[0]
        n = int(cmd[1:])
        for _ in range(n):
            x += dX[d]
            y += dY[d]
            # We're also keeping track of the current length travelled, and storing that in each point.
            length += 1

            # Don't update the length of the point if we pass through it a second time. We want the shortest length there.
            if (x, y) not in points:
                points[(x, y)] = length
    return(points)


A_points = get_points(A)
B_points = get_points(B)

# Intersection of the two sets of points finds us the common points that the lines pass through.
both = set(A_points.keys()) & set(B_points.keys())
print(both)

# Calculate the Manhattan Distance for each common point and return the smallest.
part1 = min([abs(x)+abs(y) for x, y in both])
print(part1)

# Sum the distance travelled for each common point and return the smallest.
part2 = min([A_points[p]+B_points[p] for p in both])
print(part2)
