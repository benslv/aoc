with open("6.in", "r") as f:
    lines = f.readlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]


def perform_instruction(line):
    command = line[-4]  # Will either be "toggle", "on", or "off";
    lights = line[-3:]
    start = list(map(int, lights[0].split(",")))
    end = list(map(int, lights[2].split(",")))
    r = list(zip(start, end))

    for i in range(r[0][0], r[0][1]+1):
        for j in range(r[1][0], r[1][1]+1):
            if command == "on":
                grid[i][j] += 1
            elif command == "off":
                grid[i][j] = 0 if grid[i][j] == 0 else grid[i][j] - 1
            elif command == "toggle":
                grid[i][j] += 2
            else:
                print("Something has gone terribly wrong...")


for line in lines:
    line = line.split()
    perform_instruction(line)

ans = sum([sum(row) for row in grid])
print(ans)
