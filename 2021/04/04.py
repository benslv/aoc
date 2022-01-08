import sys

inp = sys.stdin.readlines()

numbers = list(map(int, inp[0].split(",")))

boards = [[list(map(int, line.split())) for line in board.split("\n")]
          for board in "".join(inp[2:]).split("\n\n")]

winners = []
called_numbers = []


def has_row(board):
    for row in board:
        if sum(row) == -5:
            return True
    return False


def has_col(board):
    for col in map(list, zip(*board)):
        if sum(col) == -5:
            return True
    return False


def calculate_score(n, board):
    return n * sum(num for line in board for num in line if num != -1)


while len(numbers) > 0:
    num = numbers.pop(0)
    called_numbers.append(num)

    for b, board in enumerate(boards):

        if b in [x[0] for x in winners]:
            continue

        for y, line in enumerate(board):
            if num in line:
                board[y][line.index(num)] = -1

                if has_row(board) or has_col(board):
                    winners.append((b, num))

print("Part 1:", calculate_score(winners[0][1], boards[winners[0][0]]))
print("Part 2:", calculate_score(winners[-1][1], boards[winners[-1][0]]))
    