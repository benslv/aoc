import sys

patterns = [p.split() for p in sys.stdin.read().split("\n\n")]


def transpose(pattern):
    return list(map(list, zip(*pattern)))


def find_reflection(pattern, errors_allowed=0):

    for start in range(len(pattern)):
        comparisons = []

        for i in range(start, -1, -1):
            j = start + (start - i) + 1

            if j > len(pattern) - 1:
                break

            for x in range(len(pattern[i])):
                comparisons.append(pattern[i][x] != pattern[j][x])

        if len(comparisons) > 0 and sum(comparisons) == errors_allowed:
            return start + 1

    return 0


num_cols = 0
num_rows = 0

for pattern in patterns:
    num_rows += find_reflection(pattern)
    num_cols += find_reflection(transpose(pattern))

part_1 = num_cols + 100*num_rows

print(f"{part_1=}")


num_cols = 0
num_rows = 0

for pattern in patterns:
    num_rows += find_reflection(pattern, 1)
    num_cols += find_reflection(transpose(pattern), 1)

part_2 = num_cols + 100*num_rows

print(f"{part_2=}")
