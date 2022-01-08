import sys

inp = sys.stdin.read().splitlines()

part1 = 0
part2 = 0

for line in inp:
    sequences, digits = line.split(" | ")

    sequences = [frozenset(letters) for letters in sequences.split()]
    digits = [frozenset(letters) for letters in digits.split()]

    one, seven, four, *unmatched, eight = sorted(set(sequences), key=len)

    three = [x for x in unmatched if len(x - one) == 3][0]
    six = [x for x in unmatched if len(eight - x) == 1 and len(x & one) == 1][0]
    five = [x for x in unmatched if x <= six and len(six - x) == 1][0]
    zero = [x for x in unmatched if x == (eight - four) | one | (eight - three)][0]
    two = [x for x in unmatched if len(x - five) == 2 and len(x & five) == 3][0]
    nine = [x for x in unmatched if x == eight - (six - five)][0]

    part1 += sum(x in {one, four, seven, eight} for x in digits)

    mapping = {x: str(i) for i, x in enumerate([zero, one, two, three, four, five, six, seven, eight, nine])}

    part2 += int("".join(mapping[d] for d in digits))

print("Part 1:", part1)
print("Part 2:", part2)