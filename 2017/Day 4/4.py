import sys
from itertools import combinations
from collections import Counter

inp = sys.stdin.readlines()

part_1 = sum(len(line.split()) == len(set(line.split())) for line in inp)

print(part_1)

def is_anagram(a, b):
    return Counter(a) == Counter(b)

part_2 = sum(not any([is_anagram(a,b) for (a,b) in combinations(line.split(), 2)]) for line in inp)

print(part_2)
