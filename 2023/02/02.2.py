import re
import sys

inp = sys.stdin.read().splitlines()

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

part_1 = 0
part_2 = 0

for game in inp:
    game_id = int(game.split(":")[0].split(" ")[1])

    reds = list(map(int, re.findall(r"(\d+) red", game)))
    greens = list(map(int, re.findall(r"(\d+) green", game)))
    blues = list(map(int, re.findall(r"(\d+) blue", game)))

    game_is_valid = all(max(v) <= bag[k] for k, v in {
                        "red": reds, "green": greens, "blue": blues}.items())

    if game_is_valid:
        part_1 += game_id

    power = max(reds) * max(greens) * max(blues)

    part_2 += power


print(f"{part_1=}")
print(f"{part_2=}")
