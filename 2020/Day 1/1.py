import fileinput

nums = [int(x) for x in fileinput.input()]
n = len(nums)

part_1 = 0

for i in range(n):
    for j in range(i, n):
        if nums[i]+nums[j] == 2020:
            part_1 = nums[i]*nums[j]

print(f"Part 1: {part_1}")

part_2 = 0

for x in range(n):
    for y in range(x+1, n):
        for z in range(y + 1, n):
            if nums[x]+nums[y]+nums[z] == 2020:
                part_2 = nums[x]*nums[y]*nums[z]

print(f"Part 2: {part_2}")
