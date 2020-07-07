def intcode(tape):
    t = tape
    i = 0

    while True:
        # Allows the instruction tape to loop continuously even if it reaches the end
        i %= len(t)

        # These check to see if the current op needs direct or immediate addressing
        try:
            a = t[i+1] if (t[i] // 100) % 10 == 1 else t[t[i+1]]
        except IndexError:
            a = None  # 1 is immediate
        try:
            b = t[i+2] if (t[i] // 1000) % 10 == 1 else t[t[i+2]]
        except IndexError:
            b = None
        try:
            c = t[i+3] if (t[i] // 10000) % 10 == 1 else t[t[i+3]]
        except IndexError:
            c = None

        op = t[i] % 100
        if t[i] == 99:  # Halt on opcode 99
            break
        elif op == 1:
            t[t[i+3]] = a + b
            i += 4
        elif op == 2:
            t[t[i+3]] = a * b
            i += 4
        elif op == 3:
            t[t[i+1]] = int(input("Input: "))
            i += 2
        elif op == 4:
            print("Output:", a)
            i += 2
        elif op == 5:
            i = b if a != 0 else i + 3
        elif op == 6:
            i = b if a == 0 else i + 3
        elif op == 7:
            t[t[i+3]] = 1 if a < b else 0
            i += 4
        elif op == 8:
            t[t[i+3]] = 1 if a == b else 0
            i += 4
        else:
            print("bruh")


with open("5.in", "r") as f:
    lines = list(map(int, f.read().split(",")))

intcode(lines)
