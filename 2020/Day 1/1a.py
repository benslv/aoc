from itertools import combinations
import fileinput

import timeit

nums = [int(x) for x in fileinput.input()]

# Part 1
combs = combinations(nums, 2)
for a, b in combs:
    if a+b == 2020:
        print(a*b)

# Part 2
combs3 = combinations(nums, 3)
for a, b, c in combs3:
    if a+b+c == 2020:
        print(a*b*c)
