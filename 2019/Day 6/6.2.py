inp = [o.split(")") for o in open("Day 6/6.in", "r").read().splitlines()]

orbits = {"COM": []}
for i in inp:
    a, b = i[0], i[1]
    # print(a, b)

    if b not in orbits:
        orbits[b] = []
    orbits[b].append(a)

# print(orbits)


def path_to_com(x) -> list:
    cur_p = x
    travel = []
    while cur_p[0] != "COM":
        travel.append(cur_p)
        cur_p = orbits[cur_p[0]]
        # print(travel)
    return travel


san_path = path_to_com(["SAN"])
you_path = path_to_com(["YOU"])

# print(san_path)
# print(you_path)

both = [x for x in san_path if x in you_path]
print(both)

for i in both:
    you_path.remove(i)
    san_path.remove(i)

# print(san_path)
# print(you_path)

combined = san_path + you_path
print(len(combined) - 2)
