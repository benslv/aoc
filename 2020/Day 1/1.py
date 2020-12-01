import fileinput

nums = [int(x) for x in fileinput.input()]

part_1 = 0

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i]+nums[j] == 2020:
            part_1 = nums[i]*nums[j]

print(f"Part 1: {part_1}")

part_2 = 0

for x in range(len(nums)):
    for y in range(x+1, len(nums)):
        for z in range(y + 1, len(nums)):
            if nums[x]+nums[y]+nums[z] == 2020:
                part_2 = nums[x]*nums[y]*nums[z]

print(f"Part 2: {part_2}")
