import sys
import re

inp = sys.stdin.read()

diagram, instructions = inp.split("\n\n")

num_stacks = int(diagram.splitlines()[-1].split()[-1])


def get_stacks():
    stacks = [[] for _ in range(num_stacks)]

    for line in diagram.splitlines()[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ":
                stacks[i].append(box)

    return stacks


stacks = get_stacks()

# CrateMover 9000
for line in instructions.splitlines():
    quantity, b1, b2 = map(int, re.findall(
        r"move (\d+) from (\d+) to (\d+)", line)[0])

    for _ in range(quantity):
        val = stacks[b1-1].pop(0)
        stacks[b2-1].insert(0, val)

part_1 = "".join(stack[0] for stack in stacks)
print(f"{part_1=}")

stacks = get_stacks()

# CrateMover 9001
for line in instructions.splitlines():
    quantity, b1, b2 = map(int, re.findall(
        r"move (\d+) from (\d+) to (\d+)", line)[0])

    for i in range(quantity):
        val = stacks[b1-1].pop(0)
        stacks[b2-1].insert(i, val)


part_2 = "".join(stack[0] for stack in stacks)
print(f"{part_2=}")
