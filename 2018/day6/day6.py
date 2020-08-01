data = [list(map(int, i.split(", ")))
        for i in open("day6.test", "r").readlines()]


def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


max_x = max(list(zip(*data))[0])
max_y = max(list(zip(*data))[1])

grid = {}

for x in range(max_x):
    for y in range(max_y):
        min_dist = min(manhattan([x, y], [i, j])for i, j in data)
        for n, (i, j) in enumerate(data):
            if manhattan([x, y], [i, j]) == min_dist:
                if grid.get((x, y), -1) != -1:
                    grid[(x, y)] = -1
                    break
                grid[(x, y)] = n

print(grid)
