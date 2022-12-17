from collections import deque
import sys

inp = [list(line) for line in sys.stdin.read().splitlines()]


def process_input(inp):
    S = None
    E = None

    for y in range(len(inp)):
        for x in range(len(inp[y])):
            match inp[y][x]:
                case "S":
                    S = (y, x)
                    inp[y][x] = "a"
                case "E":
                    E = (y, x)
                    inp[y][x] = "z"

    return S, E


def height(y: int, x: int) -> int:
    letter = inp[y][x]
    return ord(letter)-96


def get_valid_moves(point: tuple[int, int]) -> set[tuple[int, int]]:
    moves = set()

    for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dy = point[0] + y
        dx = point[1] + x

        if dy < 0 or dy >= len(inp) or dx < 0 or dx >= len(inp[dy]):
            continue

        if height(dy, dx) <= height(*point) + 1:
            moves.add((dy, dx))

    return moves


S, E = process_input(inp)


def BFS(start: tuple[int, int]):
    queue = [[start]]
    seen = {start}

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == E:
            return path

        for move in get_valid_moves(node):
            if move not in seen:
                queue.append(path + [move])
                seen.add(move)


part_1 = len(BFS(S)) - 1
print(f"{part_1=}")

starts = [(y, x) for y in range(len(inp))
          for x in range(len(inp[y])) if inp[y][x] == "a"]

paths = list(filter(lambda x: x is not None, [BFS(s) for s in starts]))

part_2 = len(min(paths, key=len))-1
print(f"{part_2=}")
