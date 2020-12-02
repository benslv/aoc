import fileinput

passwords = list(fileinput.input())


def get_valid_passwords(passwords):
    valid = 0
    for line in passwords:
        parts = line.split()

        low, high = [int(x) for x in parts[0].split("-")]

        char = parts[1][0]

        password = parts[2]

        if part_2:
            if (password[low-1] == char) ^ (password[high-1] == char):
                valid += 1
        else:
            if password.count(char) in range(low, high+1):
                valid += 1

    return valid


part_2 = False
print("Part 1:", get_valid_passwords(passwords))

part_2 = True
print("Part 2:", get_valid_passwords(passwords))
