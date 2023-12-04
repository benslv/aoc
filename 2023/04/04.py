import sys
import re
import math

inp = sys.stdin.read().splitlines()

part_1 = 0

card_wins = dict()

NUMBER_REGEX = re.compile(
    r"Card\s+(\d+):\s+((?:\d+\s+)+\d+)\s+\|\s+((?:\d+\s+)+\d+)")

for line in inp:
    [id, winners, numbers] = NUMBER_REGEX.findall(line)[0]

    winners = {int(x) for x in winners.split()}
    numbers = {int(x) for x in numbers.split()}

    win_count = len(winners & numbers)
    card_wins[int(id)] = win_count  # Prep for Part 2 ;)

    points = math.floor(2 ** (win_count - 1))

    part_1 += points

print(f"{part_1=}")


queue = {k: 1 for k in range(1, len(inp) + 1)}

for i in range(1, len(queue.keys())+1):
    num_card = queue[i]

    wins = card_wins[i]

    for j in range(i+1, i+wins+1):
        queue[j] += num_card

print(f"part_2={sum(queue.values())}")
