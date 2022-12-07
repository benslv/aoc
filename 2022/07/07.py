import sys


# lines = sys.stdin.read().splitlines()
lines = open("/home/ben/Development/aoc/2022/07/07.test",
             "r").read().splitlines()

directory = [{}]
index = 0

while index < len(lines):
    print(lines[index])

    line = lines[index].split()

    match line[0]:
        case "$":
            command = line[1:]
            print(command)

            match command:
                case ["cd", ".."]:
                    pass
                case ["cd", subdir]:
                    if subdir not in directory[-1]:
                        directory[-1][subdir] = {}
                        print(directory)

    index += 1
