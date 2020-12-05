import fileinput

passes = [line.strip() for line in fileinput.input()]

ids = []

for pass_ in passes:
    seat = pass_.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")

    ids.append(int(seat, 2))

print(f"Part 1: {max(ids)}")

ids.sort()

for i in range(len(ids) - 1):
    if ids[i+1] - ids[i] == 2:
        print(f"Part 2: {ids[i]+1}")
        break
