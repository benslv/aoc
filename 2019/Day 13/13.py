import intcode

with open("13.in") as f:
    tape = list(map(int, f.read().split(",")))
    tape += [0]*10000

machine = intcode.Machine(mem=tape)
out = []

x, y, blockType = machine.run(), machine.run(), machine.run()
while x is not None:
    x, y, blockType = machine.run(), machine.run(), machine.run()
    out.append(blockType)

print(out.count(2))
