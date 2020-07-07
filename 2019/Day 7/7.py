from intcode import Intcode
from itertools import permutations


def get_lines():
    with open("Day 7/7.in", "r") as f:
        return list(map(int, f.read().split(",")))


def run(phase_perms):
    result = 0
    for perm in phase_perms:
        amplifiers = [Intcode(phase=phase, tape=get_lines())for phase in perm]

        inp = 0
        current = 0

        while True:

            # The entire program should halt when it encounters any of the amplifiers in a halt state.
            if amplifiers[current].halted():
                break

            # Run the machine with input (initialised at 0 for first machine).
            amplifiers[current].run(inp)

            # Grabs the output from the machine to be used as next input.
            inp = amplifiers[current].getOutput()

            # Move to the next amplifier in the chain.
            current += 1

            # Allows us to loop through the list of amplifiers an feed the result from the last back into the first.
            current %= len(amplifiers)

        result = amplifiers[4].getOutput(
        ) if amplifiers[4].getOutput() > result else result

    return result


# Part 1
phase_perms_1 = list(permutations([0, 1, 2, 3, 4]))
print(run(phase_perms_1))

# Part 2
phase_perms_2 = list(permutations([5, 6, 7, 8, 9]))
print(run(phase_perms_2))
