def solve(inp: str, n: int) -> int:
    nums = [int(x) for x in inp.split(",")]

    # Stores each number and the number of the turn it was last spoken.
    vals = {x: i+1 for i, x in enumerate(nums)}

    # Offset the turn counter by the number of turns taken to speak each number in the input.
    i = len(nums)

    prev = nums[-1]  # Initialise the most recently spoken number.

    while i < n:
        next = i - vals.get(prev, i)
        vals[prev] = i
        prev = next
        i += 1

    return prev


print(f"Part 1: {solve('16,12,1,0,15,7,11', 2020)}")
print(f"Part 2: {solve('16,12,1,0,15,7,11', 30000000)}")
