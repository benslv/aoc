import sys
import numpy as np

# increase all octopi by 1
# check for >9 energy levels
#   - increment flash count
#   - store flashed coordinate
# increment surrounding octopi (inc. adjacent)
# check for new flashes

octopi = np.array(list(list(map(int, line.strip()))
                       for line in sys.stdin.readlines()))

STEPS = 1


def process_flashes(y, x, octopi, will_flash):
    adjacent = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1),
                (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]

    # Increment adjacent octopi.
    for j, i in adjacent:
        if j in range(len(octopi)) and i in range(len(octopi[j])):
            octopi[j][i] += 1

            # If an incremented octopus now has enough energy to flash
            # add it to the set and process its neighbours
            if (octopi[j][i] > 9) and (j, i) not in will_flash:
                # will_flash.add((y, x))
                return process_flashes(j, i, octopi, will_flash | {(j, i)})

    return will_flash


while STEPS > 0:
    # Increment all octopus energies by 1.
    octopi += 1
    # print(octopi)

    # Keep track of the coordinates will flash at the end of the step.
    will_flash = set()

    # Check for >9 energy levels
    for (y, x), oct in np.ndenumerate(octopi):
        print(y, x)
        if oct > 9:
            # Process adjacent cells to a flashing cell
            will_flash |= process_flashes(y, x, octopi, will_flash | {(y, x)})

    # Set all flashing cells to 0
    for (y, x) in will_flash:
        octopi[y][x] = 0

    print(octopi)

    STEPS -= 1
