from collections import defaultdict


times = defaultdict(list)

with open("day4.txt", "r") as f:
    lines = sorted(f.read().splitlines())

for line in lines:
    time, action = line.split("] ")

    # Grab the minutes portion of the time, since nothing else is needed.
    time = int(time.split()[1].split(":")[1])

    if action.startswith("Guard"):
        id_ = action.split()[1][1:]
    elif action == "falls asleep":
        start = time
    elif action == "wakes up":
        end = time

        # Append every minute the guard is asleep to a tracker corresponding to each id.
        for minute in range(start, end):
            times[id_].append(minute)

# print(times.items())

# Part 1
# Work out the guard with the most minutes slept total. Used to use max() for this but it didn't seem to work...
max_id = sorted(times.items(), reverse=True, key=lambda x: len(x[1]))[0]
# Work out the minute most frequently slept by this guard.
max_minute = max(max_id[1], key=max_id[1].count)
answer = int(max_id[0]) * max_minute
print(f"Part 1: {answer}")

# Part 2
guards = []
for id_, _ in times.items():
    # Retrieves the most common minute for a give guard.
    max_min = max(times[id_], key=times[id_].count)
    guards.append((id_, max_min, times[id_].count(max_min)))

ans = max(guards, key=lambda x: x[2])[0:2]
print(f"Part 2: {int(ans[0])*ans[1]}")
