import sys
from typing import List

def score(c: List[int]) -> int:
    return sum([x*(i+1) for i, x in enumerate(reversed(c))])

p1d, p2d = sys.stdin.read().split("\n\n")

p1 = [int(x) for x in p1d.split("\n")[1:]]
p2 = [int(x) for x in p2d.split("\n")[1:]]

while len(p1) > 0 and len(p2) > 0:
    p1c = p1.pop(0)
    p2c = p2.pop(0)

    if p1c > p2c:
        p1.extend([p1c, p2c])
    elif p2c > p1c:
        p2.extend([p2c, p1c])
    else:
        print("Equal cards found. Halting because this shouldn't happen...")
        break


print(score(p1), score(p2))
