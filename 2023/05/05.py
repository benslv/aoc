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

seed_ranges = ([seeds[i], seeds[i] + seeds[i+1]]
               for i in range(0, len(seeds), 2))

locations = (solve([x for x in range(src, dest)], mappings)
             for src, dest in seed_ranges)

# This will take about 22 minutes :)
part_2 = min(min(location) for location in locations)

print(f"{part_2=}")
