import intcode

with open("jamie.in") as f:
    tape = list(map(int, f.read().split(",")))

tape += [0]*10000

machine = intcode.Machine(mem=tape)

# Initialise 50x50 grid of black squares.
grid = [[0 for _ in range(100)] for _ in range(100)]
x, y = 50, 50  # Starting coord for robot
visited = set()
heading = 0  # 0=up, 1=right, 2=down, 3=left

dX = [0, 1, 0, -1]
dY = [1, 0, -1, 0]

colour = machine.run(1)
direction = machine.run()
while colour is not None:
    visited.add((x, y))
    grid[x][y] = colour

    # maps 0 to -1 and 1 to 1, which means we can increment heading by +/- 1 and turn left or right!
    direction = (direction * 2) - 1
    # keep it within our range of dX and dY
    heading = (heading + direction) % 4

    x += dX[heading]
    y += dY[heading]

    colour = machine.run(grid[x][y])
    direction = machine.run()

print(len(visited))

# This prints it but not very well.
# Vary the width of your command line window and the letters should line up.
# ...
# But they'll be upside down and back to front. Hope you have a mirror!
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[x][y] == 1:
            print("X", end="")
        else:
            print(" ", end="")
