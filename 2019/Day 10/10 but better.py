import math


def getVisible(base, asteroids):
    visible = set()
    for asteroid in asteroids:
        if asteroid != base:
            dx = asteroid[0] - base[0]
            dy = asteroid[1] - base[1]
            gcd = abs(math.gcd(dx, dy))
            visible.add((dx//gcd, dy//gcd))

    return visible


with open("10.in", "r") as f:
    lines = f.readlines()

asteroids = set()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            asteroids.add((i, j))

baseCount = []
for base in asteroids:
    visible = getVisible(base, asteroids)
    baseCount.append((base, len(visible), visible))

# Sort all the bases into descending order based on the number of asteroids they can see.
bestBases = sorted(baseCount, reverse=True, key=lambda x: x[1])

# Highest number of asteroids any single base can see.
part_1 = bestBases[0]

destroyed = [(math.atan2(dy, dx), (dx, dy)) for dx, dy in part_1[2]]
destroyed.sort(reverse=True)
dx, dy = destroyed[200-1][1]

x, y = part_1[0][0]+dx, part_1[0][1]+dy
while (x, y) not in asteroids:
    x, y = x+dx, y+dy

part_2 = y*100 + x
print(part_2)
