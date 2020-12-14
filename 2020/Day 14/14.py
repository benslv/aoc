import sys
import re
# from collections import defaultdict

lines = list(sys.stdin)


def proc_mask(val, mask):
    val |= int(mask.replace("X", "0"), 2)
    val &= int(mask.replace("X", "1"), 2)

    return val


def gen_masks(mask):
    """
    Recursively generate Part 1 masks to be solved with our proc_mask() function.
    """
    if not mask:
        yield ""
        return
    else:
        for m in gen_masks(mask[1:]):
            if mask[0] == "X":  # floating bit, so yield both possible values
                yield "0" + m
                yield "1" + m
            elif mask[0] == "0":  # leave unchanged
                yield "0" + m
            elif mask[0] == "1":  # convert bit to a 1
                yield "1" + m


def solve(lines, part_1=True):
    mem = {}
    mask = ""

    for line in lines:
        key, value = line.strip().split(" = ")

        if key == "mask":
            mask = line.split()[2]
        else:
            pos = int(key[4:-1])
            if part_1:
                mem[pos] = proc_mask(int(value), mask)
            else:
                for m in gen_masks(mask):
                    print(proc_mask(pos, m))
    return mem


print(f"Part 1: {sum(solve(lines).values())}")
print(f"Part 2: {sum(solve(lines, part_1=False).values())}")
