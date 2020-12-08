import fileinput

inst = [line.split() for line in fileinput.input()]


def run(prog):
    acc = 0
    pc = 0

    seen = set()

    loop = False

    prev_pc = 0

    while pc < len(prog) and not loop:
        if pc in seen:
            loop = True
            break

        seen.add(pc)

        prev_pc = pc

        op, val = inst[pc]

        if op == "acc":
            acc += int(val)
            pc += 1
        elif op == "jmp":
            pc += int(val)
        elif op == "nop":
            pc += 1
        else:
            print("Unrecognised instruction")

    return (acc, loop, prev_pc)


part_1 = run(inst)
print(f"Part 1: {part_1[0]}")


def run2(pc, acc, seen, can_mutate):
    if pc == len(inst):
        return acc
    elif pc in seen:
        return None

    op, val = inst[pc]

    if op == "acc":
        return run2(pc + 1, acc + int(val), seen + [pc], can_mutate)
    elif op == "jmp":
        potential = run2(pc + int(val), acc, seen + [pc], can_mutate)
        if potential is None and can_mutate:
            potential = run2(pc + 1, acc, seen + [pc], False)
        return potential
    elif op == "nop":
        potential = run2(pc + 1, acc, seen + [pc], can_mutate)
        if potential is None and can_mutate:
            potential = run2(pc + int(val), acc, seen + [pc], False)
        return potential


part_2 = run2(0, 0, [], True)
print(f"Part 2: {part_2}")
