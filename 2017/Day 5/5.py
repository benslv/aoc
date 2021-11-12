import sys

inp = [int(x) for x in sys.stdin]

steps = 0
pointer = 0

while True:

    try:
        next_p = pointer + inp[pointer]

        if inp[pointer] >= 3:
            inp[pointer] -= 1
        else:
            inp[pointer] += 1

        pointer = next_p
        steps += 1
    except IndexError:
        print(f"Part 1: {steps}")
        break