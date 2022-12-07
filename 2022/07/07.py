import sys
from itertools import accumulate
from collections import defaultdict

lines = sys.stdin.read().splitlines()

directories = defaultdict(int)         

for line in lines:
    match line.split():
        case ["$", "cd", "/"]: 
            path = [""]
        case ["$", "cd", ".."]: 
            path.pop()
        case ["$", "cd", dir]:
            path.append(f"{dir}/")
        case ["$", "ls"]: 
            pass
        case ["dir", _]: 
            pass
        case [size, _]: 
            for p in accumulate(path):
                directories[p] += int(size)

print(directories)

part_1 = sum(s for s in directories.values() if s <= 100000)
print(f"{part_1=}")

part_2 = min([s for s in directories.values() if directories[""] - s <= 40000000])
print(f"{part_2=}")