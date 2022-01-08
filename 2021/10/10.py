import sys
from functools import reduce

inp = sys.stdin.readlines()

PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

SYNTAX_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

AUTOCOMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

illegal = []
scores = []


def calculate_autocomplete_score(closing):
    closing.reverse()
    return reduce(lambda acc, val: (acc * 5) + AUTOCOMPLETE_SCORES[val], closing, 0)


for line in inp:
    closing = []

    for char in line.strip():
        if char in "([{<":
            closing.append(PAIRS[char])
        elif char != closing[-1]:
            illegal.append(char)
            break
        else:
            closing.pop()
    else:
        scores.append(calculate_autocomplete_score(closing))

part_1 = sum(map(SYNTAX_SCORES.get, illegal))
print("Part 1:", part_1)

part_2 = sorted(scores)[len(scores)//2]
print("Part 2:", part_2)
