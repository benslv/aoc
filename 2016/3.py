def is_valid_triangle(a, b, c):
    return (a+b > c and b+c > a and a+c > b)

with open("3.in", "r") as f:
    triangles = [list(map(int, triangle.split())) for triangle in f.readlines()]

part_1 = 0

for triangle in triangles:
    a, b, c = triangle

    if is_valid_triangle(a, b, c):
        part_1 += 1

# Part 1
print(part_1)

columns = [[], [], []]

for i in range(len(columns)):
    for triangle in triangles:
        columns[i].append(triangle[i])

values = [x for sub in columns for x in sub]

triangles = []

for i in range(0, len(values), 3):
    triangles.append(values[i:i+3])

part_2 = 0

for triangle in triangles:
    a, b, c = triangle

    if is_valid_triangle(a, b, c):
        part_2 += 1

# Part 2
print(part_2)