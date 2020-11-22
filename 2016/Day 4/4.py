from collections import Counter

with open("4.in", "r") as f:
    rooms = [room.split("-") for room in f.read().splitlines()]

sector_total = 0

for room in rooms:
    letters = sorted("".join(room[:-1]))
    letters = Counter(letters).most_common(5)
    letters = "".join(list(zip(*letters))[0])

    sector, checksum = room[-1].rstrip("]").split("[")

    if checksum == letters:
        sector_total += int(sector)

# Part 1
print(sector_total)

from string import ascii_lowercase as ALPHABET

def shift(message, offset):
    encoded = ""
    for ch in message:
        index = ord(ch) - 97
        next_index = (index + offset) % 26
        encoded += ALPHABET[next_index]
    return encoded

for room in rooms:
    letters = "".join(room[:-1])
    sector = room[-1].rstrip("]").split("[")[0]

    print(sector, shift(letters, int(sector)))

"""
Part 2:
Solved by running `python 4.py | grep north` to find the line containing the word "north"
"""