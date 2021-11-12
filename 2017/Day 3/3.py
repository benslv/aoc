import sys
import math

inp = int(sys.stdin.read())

i = 1

while i*i < inp:
    i += 2

pivots = [i*i - k*(i-1) for k in range(4)]

print(pivots)

for p in pivots:
    dist = abs(p - inp)
    if dist <= (i-1)//2:
        print(i-1-dist)
        break

# Part 2 i on the OEIS
# https://oeis.org/A141481