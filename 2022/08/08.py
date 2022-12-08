import sys

lines = [[int(x) for x in list(line)] for line in sys.stdin.read().splitlines()]

def is_visible(y: int, x: int, tree: int):
    left = (n for n in lines[y][:x])
    right = (n for n in lines[y][x+1:])
    up = (row[x] for row in lines[:y])
    down = (row[x] for row in lines[y+1:])

    return any(max(trees) < tree for trees in [left, right, up, down])

def calc_distance(tree, trees):
    dist = 0

    for val in trees:
        if val < tree:
            dist += 1
        
        if val >= tree:
            dist += 1
            break

    return dist

def calc_scenic_score(y: int, x: int, tree: int):
    left = [n for n in lines[y][:x]][::-1]
    right = [n for n in lines[y][x+1:]]
    up = [row[x] for row in lines[:y]][::-1]
    down = [row[x] for row in lines[y+1:]]

    l_dist = calc_distance(tree, left)
    r_dist = calc_distance(tree, right)
    u_dist = calc_distance(tree, up)
    d_dist = calc_distance(tree, down)
   
    return l_dist * r_dist * u_dist * d_dist

part_1 = (len(lines) * len(lines[0])) - ((len(lines) - 2) * (len(lines[0]) - 2))
part_2 = 0

for y, row in enumerate(lines[1:-1], start=1):
    for x, tree in enumerate(row[1:-1], start=1):
        part_1 += is_visible(y, x, tree)
        part_2 = max(part_2, calc_scenic_score(y, x, tree))

print(f"{part_1=}")
print(f"{part_2=}")