floors = open("1.in").read()

d = {"(": 1, ")": -1}

# Part 1
ans = sum([d[f] for f in floors])
print(ans)

# Part 2
ans = 0
for i in range(len(floors)):
    ans += d[floors[i]]
    if ans == -1:
        print(i)
        break
