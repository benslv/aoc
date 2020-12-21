import sys

part_1 = 0

inp = [sorted(list(map(int, line.split())), reverse=True)
       for line in sys.stdin]

for line in inp:
    part_1 += max(line) - min(line)

print(f"Part 1: {part_1}")

part_2 = 0

for line in inp:
    for i in range(len(line) - 1):
        for j in range(i+1, len(line)):
            if line[i] % line[j] == 0:
                part_2 += line[i] // line[j]


print(f"Part 2: {part_2}")
