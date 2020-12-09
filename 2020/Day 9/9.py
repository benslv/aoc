import fileinput
from itertools import combinations

lines = [int(x) for x in fileinput.input()]

N = 25


def get_preamble(lines, n, m):
    """
    Take the previous n numbers before index m and calculate all the possible sums they can equal,
    returning a set of those values. 
    """
    portion = lines[m-n:m]

    return set(map(sum, combinations(portion, 2)))


part_1 = 0
for i in range(N+1, len(lines)+1):
    if lines[i] not in get_preamble(lines, N, i):
        part_1 = lines[i]
        print(f"Part 1: {part_1}")
        break

for i in range(len(lines)):
    for j in range(i+2, len(lines)+1):
        contig = lines[i:j]
        if sum(contig) == part_1:
            part_2 = min(contig)+max(contig)
            print(f"Part 2: {part_2}")
            break
        elif sum(contig) > part_1:
            break
