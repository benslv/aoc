import fileinput

passes = [line.strip() for line in fileinput.input()]


def partition_row(letters, lo, hi):
    print(lo, hi, letters)
    # If the range is only one apart, we can work out which value it should be.
    if hi-lo == 1:
        return lo if letters[0] == "F" else hi

    # Otherwise, calculate the midpoint and return
    mid = (lo + hi) // 2

    if letters[0] == "F":
        return partition_row(letters[1:], lo, mid)
    else:
        return partition_row(letters[1:], mid+1, hi)


def partition_col(letters, lo, hi):
    print(lo, hi, letters)
    # If the range is only one apart, we can work out which value it should be.
    if hi-lo == 1:
        return lo if letters[0] == "L" else hi

    # Otherwise, calculate the midpoint and return
    mid = (lo + hi) // 2

    if letters[0] == "L":
        return partition_col(letters[1:], lo, mid)
    else:
        return partition_col(letters[1:], mid+1, hi)


ids = []

for pass_ in passes:
    row = partition_row(pass_[:7], 0, 127)
    print(f"row: {row}")

    col = partition_col(pass_[7:], 0, 7)
    print(f"col: {col}")

    ids.append(row*8+col)

print(f"Part 1: {max(ids)}")

ids.sort()


for i in range(len(ids) - 1):
    if ids[i+1] - ids[i] == 2:
        print(f"Part 2: {ids[i]+1}")
        break
