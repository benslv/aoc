import sys

seeds, *mappings = sys.stdin.read().split("\n\n")

seeds = [int(x) for x in seeds.split()[1:]]
mappings = [[[int(x) for x in _map.split()] for _map in mapping.split("\n")[1:]]
            for mapping in mappings]


def solve(seeds, mappings):
    locations = []

    for seed in seeds:
        for mapping in mappings:
            for dest, src, length in mapping:
                if src <= seed < src+length:
                    diff = seed - src
                    seed = dest + diff
                    break

        locations.append(seed)

    return locations


part_1 = min(solve(seeds, mappings))
print(f"{part_1=}")
