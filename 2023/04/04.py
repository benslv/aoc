import sys
import re
import math

inp = sys.stdin.read().splitlines()

part_1 = 0

NUMBER_REGEX = re.compile(
    r"Card\s+\d+:\s+((?:\d+\s+)+\d+)\s+\|\s+((?:\d+\s+)+\d+)")

for line in inp:
    [[winners, numbers]] = NUMBER_REGEX.findall(line)

    winners = {int(x) for x in winners.split()}
    numbers = {int(x) for x in numbers.split()}

    points = math.floor(2 ** (len(winners & numbers) - 1))

    part_1 += points

print(f"{part_1=}")
