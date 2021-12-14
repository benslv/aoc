import sys

inp = sys.stdin.readlines()

registers = {line.split()[0]: 0 for line in inp}

operations = {
    "<": lambda a, b: a < b,
    ">": lambda a, b: a > b,
    "<=": lambda a, b: a <= b,
    ">=": lambda a, b: a >= b,
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b
}

highest = 0

for line in inp:
    reg_a, op, val_a, _, reg_b, cond, val_b = line.split()

    if operations[cond](registers[reg_b], int(val_b)):
        if op == "inc":
            registers[reg_a] += int(val_a)
        elif op == "dec":
            registers[reg_a] -= int(val_a)
        else:
            raise ValueError(f"Unexpected operation {op}")

    highest = max(highest, max(registers.values()))

print(f"Part 1: {max(registers.values())}")
print(f"Part 2: {highest}")
