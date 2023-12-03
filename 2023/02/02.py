import sys

inp = sys.stdin.read().splitlines()

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

part_1 = 0

for game in inp:
    is_game_valid = True

    id, rest = game.split(": ")

    sets = rest.split("; ")

    for set_ in sets:
        colors = set_.split(", ")

        for color in colors:
            num, c = color.split(" ")

            if (bag[c] < int(num)):
                is_game_valid = False
                break

        if not is_game_valid:
            break

    if is_game_valid:
        part_1 += int(id.split(" ")[1])

print(f"{part_1=}")
