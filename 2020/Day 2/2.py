import fileinput

passwords = list(fileinput.input())


def get_valid_passwords(passwords):
    valid = 0
    for password in passwords:
        parts = password.split()

        low, high = [int(x) for x in parts[0].split("-")]

        char = parts[1].rstrip(":")

        password = parts[2]

        if part_2:
            if (password[low-1] == char or password[high-1] == char) and password[low-1] != password[high-1]:
                valid += 1
        else:
            if password.count(char) in range(low, high+1):
                valid += 1

    return valid


part_2 = False
print("Part 1:", get_valid_passwords(passwords))

part_2 = True
print("Part 2:", get_valid_passwords(passwords))
