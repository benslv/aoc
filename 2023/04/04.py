import sys
import re
import math
from collections import defaultdict

inp = sys.stdin.read().splitlines()

part_1 = 0

card_wins = defaultdict(int)

NUMBER_REGEX = re.compile(
    r"Card\s+(\d+):\s+((?:\d+\s+)+\d+)\s+\|\s+((?:\d+\s+)+\d+)")

for line in inp:
    [id, winners, numbers] = NUMBER_REGEX.findall(line)[0]

    winners = {int(x) for x in winners.split()}
    numbers = {int(x) for x in numbers.split()}

    win_count = len(winners & numbers)
    card_wins[int(id)] = win_count

    points = math.floor(2 ** (win_count - 1))

    part_1 += points

print(f"{part_1=}")

# print(card_wins)

# cards = defaultdict(int)

queue = {k: 1 for k in range(1, len(inp) + 1)}

# print(queue)

for i in range(1, len(queue.keys())+1):
    num_card = queue[i]

    wins = card_wins[i]

    for j in range(i+1, i+wins+1):
        queue[j] += num_card

# print(queue)

print(f"part_2={sum(queue.values())}")

# queue = [x for x in range(1, len(inp) + 1)]

# while len(queue) > 0:
#     # print(queue)
#     id = queue.pop(0)
#     cards[id] += 1
#     win_count = card_wins[id]

#     queue.extend([x for x in range(id+1, id + win_count+1)])


# card_queue = inp[:]
# cards = defaultdict(int)
# card_wins = defaultdict(int)

# while len(card_queue) > 0:
#     card = card_queue.pop(0)

#     [id, winners, numbers] = NUMBER_REGEX.findall(card)[0]

#     winners = {int(x) for x in winners.split()}
#     numbers = {int(x) for x in numbers.split()}

#     win_count = len(winners & numbers)
#     card_wins[id] = win_count

#     cards[id] += 1

#     card_queue.extend(inp[int(id): int(id)+win_count])


# print(f"part_2={sum(cards.values())}")
