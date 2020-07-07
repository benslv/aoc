with open("3.in", "r") as f:
    directions = f.read()


def visited_houses(directions):
    dX = {"^": 0, "v": 0, ">": 1, "<": -1}
    dY = {"^": 1, "v": -1, ">": 0, "<": 0}

    x, y = 0, 0

    # Any santa will *always* drop a present off at (0, 0). How nice!
    visited = {(0, 0)}

    for d in directions:
        x += dX[d]
        y += dY[d]
        visited.add((x, y))

    return visited


part_1 = print(len(visited_houses(directions)))

santa = visited_houses(directions[::2])
robo_santa = visited_houses(directions[1::2])

part_2 = print(len(santa | robo_santa))
