import sys
import re
from math import lcm

[instructions, network_text] = sys.stdin.read().split("\n\n")
# [instructions, network_text] = open(
#     "/Users/ben.silverman/Development/aoc/2023/08/08.test2").read().split("\n\n")

NETWORK_REGEX = re.compile(r"\w{3}")

network = {}
for line in network_text.splitlines():
    [start, l, r] = NETWORK_REGEX.findall(line)

    network[start] = (l, r)

loc = "AAA"
steps = 0
i = 0
while loc != "ZZZ":
    dir = instructions[i]
    i = (i + 1) % len(instructions)

    match dir:
        case "L":
            loc = network[loc][0]
        case "R":
            loc = network[loc][1]

    steps += 1

print(f"part_1={steps}")


starts = [[k, 0] for k in network.keys() if k.endswith("A")]


for start in starts:
    i = 0
    while not start[0].endswith("Z"):
        dir = instructions[i]
        i = (i + 1) % len(instructions)

        match dir:
            case "L":
                start[0] = network[start[0]][0]
            case "R":
                start[0] = network[start[0]][1]

        start[1] += 1

part_1 = lcm(*[start[1] for start in starts])

print(f"{part_1=}")
