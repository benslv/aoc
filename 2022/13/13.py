import sys
from ast import literal_eval
from functools import cmp_to_key

inp = sys.stdin.read()


def compare(a, b):
    match a, b:
        case int(), int():
            if a < b:
                return -1
            elif a > b:
                return 1
            return 0
        case int(), list():
            return compare([a], b)
        case list(), int():
            return compare(a, [b])
        case list(), list():
            # < 0 = a is shorter
            # = 0  = equal length
            # > 0 = b is shorter
            length_diff = len(a) - len(b)

            for (x, y) in zip(a, b):
                result = compare(x, y)

                if result != 0:
                    return result

            if length_diff < 0:
                return -1
            elif length_diff > 0:
                return 1

            return 0


inp_p1 = inp.split("\n\n")

part_1 = 0
for i, pair in enumerate(inp_p1, start=1):
    p1, p2 = list(map(literal_eval, pair.split("\n")))

    in_correct_order = compare(p1, p2)

    if in_correct_order == -1:
        part_1 += i

print(f"{part_1=}")


inp_p2 = list(map(literal_eval, inp.replace(
    "\n\n", "\n").splitlines()))
inp_p2.extend([[[2]], [[6]]])

sorted_inp_p2 = sorted(inp_p2, key=cmp_to_key(compare))

index_1 = sorted_inp_p2.index([[2]]) + 1
index_2 = sorted_inp_p2.index([[6]]) + 1

part_2 = index_1*index_2
print(f"{part_2=}")
