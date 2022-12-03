import sys

inp = sys.stdin.read().splitlines()

SHAPE_SCORE = {
    "A": 1,
    "B": 2,
    "C": 3
}

OUTCOME = {
    "A": {
        "A": 3,
        "B": 0,
        "C": 6
    },
    "B": {
        "A": 6,
        "B": 3,
        "C": 0
    },
    "C": {
        "A": 0,
        "B": 6,
        "C": 3
    }
}

STRATEGY = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B"
    },
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    }
}


def play_round(opp: str, you: str) -> int:
    score = 0
    score += SHAPE_SCORE[you]
    score += OUTCOME[you][opp]

    return score


part_1 = 0

for round in inp:
    opp, you = round.split(" ")

    trans = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    you = trans[you]

    score = play_round(opp, you)

    part_1 += score


print(f"{part_1=}")

part_2 = 0

for round in inp:
    opp, strat = round.split(" ")

    you = STRATEGY[opp][strat]

    score = play_round(opp, you)

    part_2 += score

print(f"{part_2=}")
