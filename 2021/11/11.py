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
                will_flash |= process_flashes(
                    j, i, octopi, will_flash | {(j, i)})

    return will_flash


total_flashes = 0
STEPS = 0

part_1 = 0
part_2 = 0

while not (part_1 and part_2):
    # Increment all octopus energies by 1.
    octopi += 1

    # Keep track of the coordinates will flash at the end of the step.
    will_flash = set()

    # Check for >9 energy levels
    for (y, x), oct in np.ndenumerate(octopi):
        if oct > 9 and (y, x) not in will_flash:
            # Process adjacent cells to a flashing cell
            will_flash |= process_flashes(y, x, octopi, will_flash | {(y, x)})

    total_flashes += len(will_flash)

    # Set all flashing cells to 0
    for (y, x) in will_flash:
        octopi[y][x] = 0

    STEPS += 1

    if np.all(octopi == 0):
        part_2 = STEPS

    if STEPS == 100:
        part_1 = total_flashes

print("Part 1:", part_1)
print("Part 2:", part_2)
