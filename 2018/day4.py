from collections import defaultdict

guards = defaultdict(list)

# with open("day4.txt", "r") as f:
#     for line in f.read().splitlines():
#         times, action = line.split("] ")

#         if action.startswith("Guard"):
#             id_ = action.split(" ")[1]
#             guards[id_].append("bruh")

# print(guards)

with open("day4.txt", "r") as f:
    lines = sorted(f.read().splitlines())

for line in lines:
    time, action = line.split("] ")

    time = int(time.split()[1].split(":")[1])

    if action.startswith("Guard"):
        id_ = action.split()[1][1:]
    elif action == "falls asleep":
        start = time
    elif action == "wakes up":
        end = time
        time_asleep = end-start
        guards[id_].append((start, end))

    # print(f"{id_}: {time_asleep}")
    print(guards.items())
