import fileinput

passwords = list(fileinput.input())

part_1 = 0
part_2 = 0

for line in passwords:
    parts = line.split()

    low, high = [int(x) for x in parts[0].split("-")]

    char = parts[1][0]

    password = parts[2]

    part_1 += password.count(char) in range(low, high+1)

    part_2 += (password[low-1] == char) != (password[high-1] == char)

print("Part 1:", part_1)
print("Part 2:", part_2)
