import sys

patterns = [p.split() for p in sys.stdin.read().split("\n\n")]


def transpose(pattern):
    return list(map(list, zip(*pattern)))


def find_reflection(pattern):
    for start in range(len(pattern)):
        is_reflecting = False

        for i in range(start-1, -1, -1):
            j = start + (start - i) - 1

            if j > len(pattern) - 1:
                break

            if pattern[i] == pattern[j]:
                is_reflecting = True

            if pattern[i] != pattern[j]:
                is_reflecting = False
                break

        if is_reflecting:
            return start

    return 0


num_cols = 0
num_rows = 0

for pattern in patterns:
    num_rows += find_reflection(pattern)
    num_cols += find_reflection(transpose(pattern))

part_1 = num_cols + 100*num_rows

print(f"{part_1=}")
