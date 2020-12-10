import fileinput

# Parse the input file, sort the joltages and add the starting (0) joltage.
adaptors = [0] + sorted([int(x) for x in fileinput.input()])

# Calculate a list store the differences between successive joltages.
diffs = [adaptors[i+1] - adaptors[i] for i in range(len(adaptors)-1)]

# Add a final joltage equal to the max of the current list + 3 (as specified by the question).
adaptors.append(adaptors[-1] + 3)

# Add this joltage to the list of differences, too; we know it will be +3 from the previous.
diffs.append(3)

# Part 1: Print the number of 1-jolt differences multiplied by the number of 3-jolt differences.
print(f"Part 1: {diffs.count(1) * diffs.count(3)}")

# Create a dictionary to store the number of possible routes "to each joltage".
routes = {}

# Initialise with 1 route to the starting joltage.
routes[0] = 1

# Begin iterating through adaptors (ignoring the first value because we already set it above).
for j in adaptors[1:]:
    # Each joltage route is equal to the sum of the number of routes to the previous three joltages.
    # However, some of the joltages won't be present in the list of adaptors.
    # So the number of routes to them will be 0.
    routes[j] = routes.get(j-1, 0) + routes.get(j-2, 0) + routes.get(j-3, 0)

# Print the number of possible routes to get to the final adaptor.
print(f"Part 2: {routes[max(routes.keys())]}")
