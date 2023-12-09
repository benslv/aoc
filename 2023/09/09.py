import sys

inp = [[int(x) for x in line.split()]
       for line in sys.stdin.read().splitlines()]


def solve(arr: list[int]):
    differences = [arr[x] - arr[x-1] for x in range(1, len(arr))]

    if all(x == differences[0] for x in differences):
        return arr[-1] + differences[0]

    return arr[-1] + solve(differences)


part_1 = sum(solve(line) for line in inp)
print(f"{part_1=}")

part_2 = sum(solve(line[::-1]) for line in inp)
print(f"{part_2=}")
