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