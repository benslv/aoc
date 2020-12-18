import sys
import re

lines = [line.strip() for line in sys.stdin]

# Create a new custom class to redefine operator precedences!


class Int():
    def __init__(self, s):
        self.val = int(s)

    def __add__(self, other):
        return Int(self.val+other.val)

    # Part 1: Multiplcation is assigned to the subtraction operation, so it has the same LTR evaluation as addition.
    def __sub__(self, other):
        return Int(self.val*other.val)

    def __mul__(self, other):
        return Int(self.val*other.val)

    # Part 2: Addition is assigned to the exponentiation operator, so it has a higher precedence than multiplication.
    def __pow__(self, other):
        return Int(self.val+other.val)


part_1 = 0

for line in lines:
    # Replace every number with a custom Int version.
    line = re.sub(r"(\d+)", r"Int(\1)", line)
    # Replace every instance of multiplication with a subtraction.
    line = re.sub(r"\*", r"-", line)
    # Use Python's eval() to parse the parentheses and calculate the result.
    part_1 += eval(line).val

print(f"Part 1: {part_1}")

part_2 = 0

for line in lines:
    # Replace every number with a custom Int version.
    line = re.sub(r"(\d+)", r"Int(\1)", line)
    # Replace every instance of addition with an exponentiation.
    line = re.sub(r"\+", r"**", line)
    # Use Python's eval() to parse the parentheses and calculate the result.
    part_2 += eval(line).val

print(f"Part 2: {part_2}")
