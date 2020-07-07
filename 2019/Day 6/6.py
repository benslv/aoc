inp = [o.split(")") for o in open("Day 6/6.in", "r").read().splitlines()]

orbits = {}
for i in inp:
    a, b = i[0], i[1]
    print(a, b)

    if a not in orbits:
        orbits[a] = []
    orbits[a].append(b)

print(orbits)


def recurse_orbits(x):
    ans = 0
    for v in orbits.get(x, []):
        ans += recurse_orbits(v) + 1
    return ans


ans = 0
for k in orbits:
    ans += recurse_orbits(k)

print(ans)
