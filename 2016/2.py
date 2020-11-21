with open("2.in", "r") as f:
    instructions = f.read().splitlines()

# Initialised at (1, 1) because we start on button 5.
x = 1
y = 1

dX = {"U": 0, "R": 1, "D": 0, "L": -1}
dY = {"U": -1, "R": 0, "D": 1, "L": 0}

# keypad = [["1", "2", "3"],
#           ["4", "5", "6"],
#           ["7", "8", "9"]]

keypad = [["X", "X", "1", "X", "X"],
          ["X", "2", "3", "4", "X"],
          ["5", "6", "7", "8", "9"],
          ["X", "X", "2", "X", "X"],
          ["X", "X", "2", "X", "X"]]

code = ""

for instr in instructions:
    for d in instr:
        x += dX[d]
        y += dY[d]

        # Prevent going out of range.
        if x < 0:
            x = 0
        elif x > 2:
            x = 2
        elif y < 0:
            y = 0
        elif y > 2:
            y = 2

    code += keypad[y][x]

print(code)
