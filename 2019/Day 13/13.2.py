import intcode

with open("13.in") as f:
    tape = list(map(int, f.read().split(",")))
    tape += [0]*1000000

tape[0] = 2
machine = intcode.Machine(mem=tape)

score = 0
paddle_x = None
ball_x = None
inp = []

while True:
    x = machine.run(inp)
    y = machine.run(inp)
    tile = machine.run(inp)

    # print("x:", x)
    # print("y:", y)
    # print("tile:", tile)

    if x is None or y is None or tile is None:
        break

    inp = [0]

    if (x, y) == (-1, 0):
        score = tile
        print(score)
        continue

    if tile == 3:  # Paddle
        paddle_x = x
    elif tile == 4:  # Ball
        ball_x = x

    if not (paddle_x is None or ball_x is None):
        if paddle_x < ball_x:    # If paddle is to the left of the ball, input RIGHT movement
            inp = [1]
        elif paddle_x > ball_x:  # If paddle is to the right of the ball, input LEFT movement
            inp = [-1]


print("Score:", score)
