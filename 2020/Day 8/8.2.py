import fileinput
from copy import deepcopy

lines = [line.split() for line in fileinput.input()]

def compute(tape, part):
    acc = 0
    pc = 0
    seen = set()

    while pc < len(tape):
        if pc in seen:
            if part == 1:
                return acc
            else:
                return None

        seen.add(pc)
        
        op, val = tape[pc]

        if op == "acc":
            acc += int(val)
            pc += 1
        elif op == "jmp":
            pc += int(val)
        elif op == "nop":
            pc += 1
        else:
            print("Unrecognised instruction.")

    return acc

part_1 = compute(lines, 1)
print(f"Part 1: {part_1 }")


part_2 = None
for i in range(len(lines)):

    # Didn't really want to have to use deepcopy but doing [:] 
    # doesn't seem to make a fresh copy every iteration.
    tape = deepcopy(lines)

    if tape[i][0] == "jmp":
        tape[i][0] = "nop"
    elif tape[i][0] == "nop":
        tape[i][0] = "jmp"

    output = compute(tape, 2)

    if output is not None: # doesn't return None
        part_2 = output
        break

print(f"Part 2: {part_2}")