import sys
from typing import Generator, List, Dict

lines = list(sys.stdin)


def proc_mask(val: int, mask: str) -> int:
    """
    Applies a binary mask to a provided binary value.
    Any non-"X" bits in the mask are applied over the bit in the same position of the value.

    value:  0001011  (decimal 11)
    mask:   1XXXX0X
    result: 1001001  (decimal 73)
    """
    val |= int(mask.replace("X", "0"), 2)
    val &= int(mask.replace("X", "1"), 2)

    return val


def gen_masks(mask: str) -> Generator[str, None, None]:
    """
    Recursively generates masks in the style of Part 1.

    Bit cases:
        0 -> address bit is unchanged (this is an "X" in Part 1 syntax)
        1 -> address bit is overwritten with a 1
        X -> address bit is "floating" so two versions are created, one each with a "0" and a "1"
    """
    if not mask:
        yield ""
        return

    for m in gen_masks(mask[1:]):
        if mask[0] == "0":
            yield "X" + m
        elif mask[0] == "1":
            yield "1" + m
        elif mask[0] == "X":
            yield "0" + m
            yield "1" + m


def solve(lines: List[str], part_1: bool) -> Dict[int, int]:
    mem = {}  # Initialise empty memory (key: address, value: value)
    mask = None  # Initialise empty mask

    for line in lines:
        key, value = line.strip().split(" = ")

        if key == "mask":
            mask = value
        else:
            addr = int(key[4:-1])  # Retrieve the memory address to use.
            if part_1:
                # Apply the bitmask to the value, and write the output to the memory address.
                mem[addr] = proc_mask(int(value), mask)
            else:
                # From the mask provided, generate a list of masks in the style of Part 1.
                for m in gen_masks(mask):
                    # Apply each mask to the address to calculate the new address
                    # and write the value to this address.
                    mem[proc_mask(addr, m)] = int(value)

    return mem


print(f"Part 1: {sum(solve(lines, True).values())}")
print(f"Part 2: {sum(solve(lines, False).values())}")
