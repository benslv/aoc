import fileinput
from collections import deque

instructions = [line.rstrip("\n") for line in fileinput.input()]


def create_matrix(n, m):
    """
    Create a matrix of n rows and m columns.
    """
    return [[False for _ in range(m)] for _ in range(n)]


def rect(col, row, matrix):
    for i in range(col):
        for j in range(row):
            matrix[j][i] = True


def print_matrix(matrix):
    output = "\n".join(
        [" ".join(["X" if col == True else "." for col in row]) for row in matrix])
    print(output)


def rotate_row(row, rot, matrix):
    target_row = deque(matrix[row])
    target_row.rotate(rot)
    matrix[row] = target_row


def rotate_col(col, rot, matrix):
    target_col = deque([row[col] for row in matrix])
    target_col.rotate(rot)

    for i in range(len(matrix)):
        matrix[i][col] = target_col[i]


matrix = create_matrix(6, 50)

for ins in instructions:
    parts = ins.split()

    if parts[0] == "rect":
        a, b = parts[1].split("x")
        rect(int(a), int(b), matrix)
    elif parts[0] == "rotate":
        amount = int(parts[2].split("=")[1])
        if parts[1] == "column":
            rotate_col(amount, int(parts[4]), matrix)
        if parts[1] == "row":
            rotate_row(amount, int(parts[4]), matrix)

print_matrix(matrix)

part_1 = [light for sublist in matrix for light in sublist]
print(part_1.count(True))
