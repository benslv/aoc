import sys
import re

inp = sys.stdin.read().splitlines()

[times, best] = [[int(x) for x in re.findall(r"\d+", line)]
                 for line in inp]


part_1 = 1

for i, time in enumerate(times):
    better_ways = 0

    for hold_ms in range(0, time+1):
        distance = hold_ms * (time-hold_ms)
        if distance > best[i]:
            better_ways += 1

    part_1 *= better_ways

print(f"{part_1=}")

[time, distance] = [int("".join(re.findall(r"\d+", line))) for line in inp]

print(time, distance)

part_2 = 0


for hold_ms in range(0, time+1):
    d = hold_ms * (time-hold_ms)
    if d > distance:
        part_2 += 1

print(f"{part_2=}")
