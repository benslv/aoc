import sys

lines = sys.stdin.read().splitlines()


class Clock:
    def __init__(self):
        self.X = 1
        self.tick = 0
        self.values = []
        self.screen = ""

    def __repr__(self):
        return f"{self.tick=} {self.X=}"

    def cycle(self):
        if self.tick > 0 and (self.tick % 40) == 0:
            self.screen += "\n"

        if abs((self.tick % 40) - self.X) <= 1:
            self.screen += "#"
        else:
            self.screen += " "

        self.tick += 1

        if (self.tick + 20) % 40 == 0:
            self.values.append(self.X*self.tick)

    def addx(self, val: int):
        self.X += val

    def get_total(self):
        return sum(self.values)

    def get_screen(self):
        return self.screen


clock = Clock()

for line in lines:
    match line.split(" "):
        case ["noop"]:
            clock.cycle()

        case ["addx", val]:
            clock.cycle()
            clock.cycle()

            clock.addx(int(val))

print(f"Part 1: {clock.get_total()=}")

print(f"Part 2:\n{clock.get_screen()}")
