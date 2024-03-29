import sys
from collections import Counter
from functools import cmp_to_key


inp = [line.split() for line in sys.stdin.read().splitlines()]


def score(hand: str, j_val: str = "0"):
    match sorted(Counter(hand.replace("0", j_val)).values(), reverse=True):
        case [5]:
            return 10
        case [4, 1]:
            return 9
        case [3, 2]:
            return 8
        case [3, 1, 1]:
            return 7
        case [2, 2, 1]:
            return 6
        case [2, 1, 1, 1]:
            return 5
        case [1, 1, 1, 1, 1]:
            return 4


def strength(hand: str, p2=False):
    if p2:
        hand = hand.translate(str.maketrans("TJQKA", "A0CDE"))
        return max((score(hand, j_val), hand) for j_val in "ABCDE98765432")
    else:
        hand = hand.translate(str.maketrans("TJQKA", "ABCDE"))
        return (score(hand), hand)


def cmp(a: str, b: str, p2=False):
    a_strength = strength(a, p2)
    b_strength = strength(b, p2)

    if a_strength[0] > b_strength[0]:
        return 1
    elif a_strength[0] < b_strength[0]:
        return -1
    elif a_strength[1] > b_strength[1]:
        return 1
    elif a_strength[1] < b_strength[1]:
        return -1

    return 0


part_1 = sum([rank*bid for [rank, [_, bid]] in enumerate(sorted([[hand, int(bid)] for [hand, bid] in inp],
                                                                key=cmp_to_key(lambda x, y: cmp(x[0], y[0]))), start=1)])

print(f"{part_1=}")

part_2 = sum([rank*bid for [rank, [_, bid]] in enumerate(sorted([[hand, int(bid)] for [hand, bid] in inp],
                                                                key=cmp_to_key(lambda x, y: cmp(x[0], y[0], p2=True))), start=1)])

print(f"{part_2=}")
