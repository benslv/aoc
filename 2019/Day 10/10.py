"""
I can't ever delete this code.
It's so bad. It must serve as a reminder to how rushing through a problem
and not laying your thoughts out clearly can lead to a huge amount of pain
and suffering that no man should have to endure.
"""

import math

with open("10.test", "r") as f:
    lines = f.readlines()

locs = []
for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == "#":
            locs.append((y, x))

# Dict to store the number of asteroids in line of sight of each asteroid.
points = {}


def angle(x: tuple, y: tuple) -> float:
    """
    Returns the angle between the current asteroid
    and a given point.
    """
    ans = math.atan2(x[1] - y[1], x[0] - y[0])
    # ensures the angles stay positive and between (0, 2PI)
    return ans % (math.pi*2)


for point in locs:
    # For storing the angles between each asteroid and the point. Will automatically remove duplicate points.
    angles = set()
    for target in locs:
        if point == target:
            continue
        angles.add(angle(point, target))

    points[point] = angles

# for p in points.keys():
#     print(len(points[p]))

part_1 = max([[p, len(points[p])] for p in points.keys()], key=lambda x: x[1])
print(part_1)


def dist(x, y):
    return abs(x[0]+y[0]) + abs(x[1]+y[1])


base = part_1[0]  # coords of the monitoring station

points = {}  # dictionary to store a list of all points at a particular angle

print("Base:", base)
for ast in locs:
    # Add half pi to move start point to top of circle, then modulus with 2pi to make negative angles positive
    a = (angle(base, ast) + math.pi/2) % (2*math.pi)
    if a not in points:
        points[a] = [ast]
    else:
        points[a].append(ast)

angles = [[k, v] for k, v in points.items()]

# Sorting angles by reverse allows us to iterate through them clockwise rather than anticlockwise.
angles.sort(reverse=True)

# Sort the asteroids in each angle in descending order of disctance from the base (to work out which should be destroyed first).
for angle in angles:
    angle[1].sort(reverse=True, key=lambda asteroid: dist(base, asteroid))

print(angles)

i = 0
bet = None
# Begin "rotating" clockwise from the top of the screen.
for a in angles:
    last_destroyed = a[1][-1]
    print(last_destroyed)
    del a[1][-1]  # Delete the closest asteroid from the current angle.
    i += 1
    if i == 200:
        bet = last_destroyed
        break
print(bet)
print(100*bet[0] + bet[1])

destroyed = []

# 1. Distance function to sort points by
# 2. Only destroy one per angle each rotation
# Why did you get this far? Please...I'm sorry.
