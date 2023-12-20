import sys
import re
from collections import defaultdict

strings = sys.stdin.read().split(",")


def hash(string: str) -> int:
    curr = 0

    for c in string:
        curr += ord(c)
        curr *= 17
        curr %= 256

    return curr


part_1 = sum(map(hash, strings))

print(f"{part_1=}")

boxes = defaultdict(list)

LENS_REGEX = re.compile(r"(\w+)([=-])(\d+)*")


def find_index(arr, callback):
    for index, element in enumerate(arr):
        if callback(element):
            return index

    return -1


for string in strings:
    label, action, focal_length = LENS_REGEX.findall(string)[0]

    box = hash(label)
    lens_index = find_index(boxes[box], lambda l: l[0] == label)

    match(action):
        case "-":
            if lens_index != -1:
                boxes[box].pop(lens_index)
        case "=":
            if lens_index != -1:
                boxes[box][lens_index][1] = focal_length
            else:
                boxes[box].append([label, focal_length])

part_2 = 0

for box in boxes.items():
    index = int(box[0]) + 1

    for i, lens in enumerate(box[1], start=1):
        part_2 += index * i * int(lens[1])


print(f"{part_2=}")
