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
# Work out the guard with the most minutes slept total.
max_id = max(times, key=lambda x: len(x[1]))
# Work out the minute most frequently slept by this guard.
max_minute = max(times[max_id], key=times[max_id].count)
print(max_id, max_minute)
answer = int(max_id) * max_minute
print(answer)

# Part 2
guards = []
for id_, _ in times.items():
    # Retrieves the most common minute for a give guard.
    max_min = max(times[id_], key=times[id_].count)
    guards.append((id_, max_min, times[id_].count(max_min)))

ans = max(guards, key=lambda x: x[2])[0:2]
print(int(ans[0])*ans[1])
