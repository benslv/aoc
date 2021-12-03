import sys
from collections import Counter

inp = [list(x.strip()) for x in sys.stdin.readlines()]

zipped = list(zip(*inp))

gamma = ""
epsilon = ""

for col in zipped:
    zero = col.count("0")
    one = col.count("1")

    gamma += "0" if zero > one else "1"
    epsilon += "0" if zero < one else "1"

print(f"Part 1: {int(gamma, 2)* int(epsilon, 2)}")

oxygen = inp
co2 = inp

o = ""
c = ""

for i in range(len(inp[0])+1):

    if len(oxygen) > 1:
        count_o = Counter(list(zip(*oxygen))[i])

        if count_o["0"] > count_o["1"]:
            oxygen = [line for line in oxygen if line[i] == "0"]
        else:
            oxygen = [line for line in oxygen if line[i] == "1"]

    else:
        o = "".join(oxygen[0])

    if len(co2) > 1:
        count_c = Counter(list(zip(*co2))[i])

        if count_c["0"] <= count_c["1"]:
            co2 = [line for line in co2 if line[i] == "0"]
        else:
            co2 = [line for line in co2 if line[i] == "1"]
    else:
        c = "".join(co2[0])

print(f"Part 2: {int(o, 2) * int(c, 2)}")
