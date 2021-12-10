import sys
from collections import deque

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

illegal = []

scores = []

def calculate_autocomplete_score(closing):
    score = 0

    AUTOCOMPLETE_SCORES = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    while closing:
        char = closing.pop()
        score = (score * 5) + AUTOCOMPLETE_SCORES[char]

    return score

for line in inp:
    closing = deque()
    for char in line.strip():
        if char in "([{<":
            closing.append(PAIRS[char])
        elif char != closing[-1]:
            illegal.append(char)
            # print("Incorrect char:", char)
            # print("Broken string:", line)
            break
        else:
            closing.pop()
    else:
        print(closing)
        scores.append(calculate_autocomplete_score(closing))

part_1 = sum(map(SYNTAX_SCORES.get, illegal))
print("Part 1:", part_1)

print(scores)

part_2 = sorted(scores)[len(scores)//2]
print("Part 2:", part_2)
