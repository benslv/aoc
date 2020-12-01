import fileinput
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


instructions = sorted([line.rstrip()
                       for line in fileinput.input()], reverse=True)

print(instructions)


store = {
    "bot": defaultdict(list),
    "input": defaultdict(list),
    "output": defaultdict(list)
}


for ins in instructions:
    parts = ins.split()

    if ins.startswith("value"):
        val = parts[1]  # Value to be added.
        bid = parts[5]  # Bot ID to be used.

        store["bot"][bid].append(val)  # Add the value to the bot's storage.
        # Sort the storage to persist "high" and "low" functionality.
        store["bot"][bid].sort()
    elif ins.startswith("bot"):
        give_id = parts[1]

        val_1 = parts[3]
        type_1 = parts[5]
        id_1 = parts[6]

        val_2 = parts[8]
        type_2 = parts[10]
        id_2 = parts[11]

        # TODO: Add ternary to type_1 and type_2 to check whether "high" or "low"