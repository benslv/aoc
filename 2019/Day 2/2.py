def intcode(noun, verb):
    '''
    Takes two inputs at positions 1 and 2, and returns an output at position 0.
    '''

    lines = [int(x) for x in open("Day 2/input", "r").read().split(",")]

    lines[1], lines[2] = noun, verb

    i = 0
    while True:
        if lines[i] == 1:
            # Hmmm...yes...is this direct memory addressing?
            lines[lines[i+3]] = lines[lines[i+1]] + lines[lines[i+2]]
        elif lines[i] == 2:
            lines[lines[i+3]] = lines[lines[i+1]] * lines[lines[i+2]]
        elif lines[i] == 99:
            break
        else:
            print("Unknown operand:", lines[i])
        i += 4

    return lines[0]


part_1 = print(intcode(12, 2))  # 3706713

for i in range(100):
    for j in range(100):
        if intcode(i, j) == 19690720:
            print(i, j)
            break

part_2 = print(intcode(86, 9))  # 19690720
