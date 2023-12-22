import sys

patterns = [p.split() for p in sys.stdin.read().replace(
    ".", "0").replace("#", "1").split("\n\n")]


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
    rows = [int(row, 2) for row in pattern]
    cols = [int("".join(col), 2) for col in transpose(pattern)]

    num_rows += find_reflection(rows)
    num_cols += find_reflection(cols)

part_1 = num_cols + 100*num_rows

print(f"{part_1=}")
