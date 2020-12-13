import sys
import math
from sympy.ntheory.modular import crt

inp = sys.stdin

timestamp, ids = inp

ids_ = [int(i) for i in ids.split(",") if i != "x"]

divided = sorted({k: int(timestamp) / k for k in ids_}.items(),
                 key=lambda x: math.ceil(x[1])-x[1], reverse=False)

earliest = (divided[0][0], divided[0][0]*round(divided[0][1]))

part_1 = earliest[0] * (earliest[1] - int(timestamp))

print(f"Part 1: {part_1}")


a = []
b = []

for i, j in enumerate(ids.split(",")):
    if j == "x":
        continue
    j = int(j)
    a.append(j)
    b.append(j-i)

part_2 = crt(a, b)[0]

print(f"Part 2: {part_2}")