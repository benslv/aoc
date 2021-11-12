import sys

mem = list(map(int, sys.stdin.read().split()))

def get_max_block(mem: list[int]) -> int:
    return (max(mem), mem.index(max(mem)))

def redistribute(mem: list[int]) -> list[int]:
    val, i = get_max_block(mem)

    mem[i] = 0

    quotient = val // len(mem)
    remainder = val % len(mem)

    for j in range(len(mem)):
        mem[j] += quotient

    for j in range(remainder):
        mem[(i + 1 + j) % len(mem)] += 1
    
    return mem


seen = set()
cycles = 1

while (allocation := tuple(redistribute(mem))) not in seen:
    seen.add(allocation)
    cycles += 1

print(cycles, allocation, len(seen))

# Run with 6.in for Part 1
# RUn with 6.2.in for Part 2