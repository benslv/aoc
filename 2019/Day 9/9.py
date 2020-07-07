import intcode

with open("9.in", "r") as f:
    tape = list(map(int, f.read().split(",")))
    tape += [0]*80000

machine = intcode.Machine(mem=tape)
ans = machine.run()
print(ans)
