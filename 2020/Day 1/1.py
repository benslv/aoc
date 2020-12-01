with open("1.in", "r") as f:
    nums = list(map(int, f.readlines()))

# part_1 = 0

# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         if nums[i]+nums[j] == 2020:
#             # print(nums[i]*nums[j])
#             part_1 = nums[i]*nums[j]

# print(part_1)

part_2 = 0

for x in range(len(nums)):
    for y in range(x+1, len(nums)):
        for z in range(y + 1, len(nums)):
            if nums[x]+nums[y]+nums[z] == 2020:
                part_2 = nums[x]*nums[y]*nums[z]

print(part_2)
