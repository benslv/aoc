import fileinput
import re
from collections import defaultdict


class Bot:
    def __init__(self, id):
        self.id = id
        self.bin = []

    def give(self, val):
        """
        Add the new value to the bot's bin.
        Sort it in ascending order (to preserve "low" and "high" positions).
        """
        self.bin.append(val)
        self.bin.sort()

    def take(self, val):
        """
        Remove a value from the bot's bin.
        "val" will either be "high" or "low".
        """
        if val == "high":
            return self.bin.pop(1)
        else:
            return self.bin.pop(0)

    def get_bin(self):
        return self.bin


lines = [line.rstrip() for line in fileinput.input()]

values = list(filter(lambda x: x.startswith("value"), lines))
instructions = list(filter(lambda x: x.startswith("bot"), lines))

store = {
    "bot": defaultdict(list),
    "output": defaultdict(list)
}

# Populate all the bots with their values.
for line in values:
    parts = line.split()

    val = int(parts[1])  # Value to be added.
    bid = parts[5]  # Bot ID to be used.

    store["bot"][bid].append(val)  # Add the value to the bot's storage.

routes = {}

# For each of the non-"value" instructions, record where each both sends
# its chips to once it has 2 of them.
for ins in instructions:
    give, n1, n2 = re.findall(r"\d+", ins)
    type1, type2 = re.findall(r" (bot|output) ", ins)

    # Store the number of each chip and the type of store it should go to.
    routes[give] = (n1, type1), (n2, type2)

# Continue processing all the bots until they've all run out of chips.
while store["bot"]:
    for k, v in dict(store["bot"]).items():
        if len(v) == 2:
            v1, v2 = sorted(store["bot"].pop(k))

            if v1 == 17 and v2 == 61:
                print(f"Part 1: {k}")

            (n1, type1), (n2, type2) = routes[k]
            store[type1][n1].append(v1)
            store[type2][n2].append(v2)


a, b, c = [store["output"][str(i)][0] for i in range(3)]

print(f"Part 2: {a*b*c}")
