import sys
from typing import List, Set, Tuple


def score(c: List[int]) -> int:
    return sum([x*(i+1) for i, x in enumerate(reversed(c))])


p1d, p2d = sys.stdin.read().split("\n\n")

p1 = [int(x) for x in p1d.split("\n")[1:]]
p2 = [int(x) for x in p2d.split("\n")[1:]]


def rec_combat(p1: List[int], p2: List[int]) -> Tuple[int, int]:
    seen: Set[Tuple[int]] = set()

    while p1 and p2:
        key = str(p1) + "|" + str(p2)

        # Before either player deals a card, if there was a previous round in this game that had
        # exactly the same cards in the same order in the same players' decks, the game instantly
        # ends in a win for player 1.
        if key in seen:
            return 1, p1

        # Otherwise, this round's cards must be in a new configuration; the players begin the
        # round by each drawing the top card of their deck as normal.
        seen.add(key)

        p1c = p1.pop(0)
        p2c = p2.pop(0)

        # If both players have at least as many cards remaining in their deck as the
        # value of the card they just drew, the winner of the round is determined by
        # playing a new game of Recursive Combat.
        if len(p1) >= p1c and len(p2) >= p2c:
            winner, _ = rec_combat(p1[:p1c], p2[:p2c])

            if winner == 1:
                p1.extend([p1c, p2c])
            else:
                p2.extend([p2c, p1c])
        else:
            # Otherwise, at least one player must not have enough cards left in their deck
            # to recurse; the winner of the round is the player with the higher-value card.
            if p1c > p2c:
                p1.extend([p1c, p2c])
            else:
                p2.extend([p2c, p1c])

    if len(p1) > 0:
        return 1, p1
    else:
        return 2, p2


winner, part_2 = rec_combat(p1, p2)

print(f"Part 2: {score(part_2)}")
