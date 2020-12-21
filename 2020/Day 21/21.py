import sys
from collections import Counter

all_foods = set()
counts = Counter()

als = {}

for line in sys.stdin:
    a, b = line.strip().split(" (contains ")
    foods = set(a.split())
    allergens = set(b.rstrip(")").split(", "))

    all_foods |= foods
    counts.update(foods)

    for allergen in allergens:
        if allergen not in als:
            als[allergen] = foods.copy()
        else:
            als[allergen] &= foods

bad_foods = {food for foods in als.values() for food in foods}

part_1 = sum([counts[food] for food in (all_foods - bad_foods)])
print(f"Part 1: {part_1}")

seen = set()
dangerous = []

while True:
    for allergen, food in als.items():
        if len(food - seen) == 1:
            item = min(food-seen)
            dangerous.append((allergen, item))
            seen.add(item)
            break
    else:
        break

part_2 = ",".join([x[1] for x in sorted(dangerous, key=lambda x: x[0])])

print(f"Part 2: {part_2}")
