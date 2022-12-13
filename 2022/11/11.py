import sys
import re
import operator
import math

inp = sys.stdin.read()

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


class Monkey:
    def __init__(self, items: list[int], operation, test_val: int, t: int, f: int):
        self.items = items
        self.operation = operation
        self.test_val = test_val
        self.t = t
        self.f = f
        self.inspections = 0

    def __repr__(self):
        return f"{self.items=}, {self.inspections=}"

    def test(self, worry: int):
        return self.t if worry % self.test_val == 0 else self.f

    def take_turn(self, modulo=None):
        for item in self.items:
            self.inspections += 1

            item = self.operation(item)

            if not modulo:
                item = math.floor(item / 3)
            else:
                item %= modulo

            throw_to = self.test(item)

            monkeys[throw_to].items.append(item)

        self.items = []


def get_operation(expr: str):
    left, op, right = expr.split(" ")

    op = OPERATORS[op]

    match [left, right]:
        case "old", "old":
            return lambda old: op(old, old)
        case a, "old":
            return lambda old: op(int(a), old)
        case "old", b:
            return lambda old: op(old, int(b))
        case a, b:
            return lambda: op(a, b)
        case _:
            raise ValueError("Unhandled expression found:", expr)


def get_monkeys():
    monkeys: dict[int, Monkey] = {}

    for monkey in inp.split("\n\n"):
        monkey_lines = monkey.splitlines()

        num = int(re.findall(r"(\d+)", monkey_lines[0])[0])
        items = [int(item)
                 for item in monkey_lines[1].split(": ")[1].split(", ")]
        operation = get_operation(monkey_lines[2].split("= ")[1])
        test_val = int(re.findall(r"(\d+)", monkey_lines[3])[0])
        t = int(re.findall(r"(\d+)", monkey_lines[4])[0])
        f = int(re.findall(r"(\d+)", monkey_lines[5])[0])

        monkeys[num] = Monkey(items, operation, test_val, t, f)

    return monkeys


# Part 1
monkeys = get_monkeys()

for _ in range(20):
    for monkey in monkeys.values():
        monkey.take_turn()

part_1 = operator.mul(
    *sorted((monkey.inspections for monkey in monkeys.values()), reverse=True)[:2])

print(f"{part_1=}")

# Part 2
monkeys = get_monkeys()
modulo = math.lcm(*[monkey.test_val for monkey in monkeys.values()])

for _ in range(10_000):
    for monkey in monkeys.values():
        monkey.take_turn(modulo=modulo)

part_2 = operator.mul(
    *sorted((monkey.inspections for monkey in monkeys.values()), reverse=True)[:2])

print(f"{part_2=}")
