import sys

inp = list(map(int, sys.stdin.read().split(",")))


class LanternFish:
    def __init__(self, timer=9):
        self.timer = timer

    def tick(self):
        if self.timer == 0:
            self.timer = 6
        else:
            self.timer -= 1

        return self

    def get_timer(self):
        return self.timer


def solve(days):
    fishes = [LanternFish(timer=x) for x in inp]

    DAYS = days

    while DAYS > 0:
        for fish in fishes:
            if fish.get_timer() == 0:
                fishes.append(LanternFish())

        fishes = [fish.tick() for fish in fishes]

        # print([fish.get_timer() for fish in fishes])

        DAYS -= 1

    return len(fishes)


print("Part 1:", solve(80))
print("Part 2:", solve(256))
