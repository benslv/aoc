import re


def has_ABBA(string):
    return (match := re.search(r"(.)(.)\2\1", string)) is not None and (match[0][0] != match[0][1])


with open("7.in", "r") as f:
    ips = [re.split(r"[\[\]]", ip) for ip in f.read().splitlines()]


# Part 1
total = 0
for ip in ips:
    abba = any(has_ABBA(x) for x in ip[::2])
    no_abba = all(not has_ABBA(y) for y in ip[1::2])

    if abba and no_abba:
        total += 1

print(total)


def is_ABA(string):
    return string[0] != string[1] and string[0] == string[2]


def flip(string):
    return string[1]+string[0]+string[1]


total = 0
for ip in ips:

    supernet = ip[::2]
    hypernet = ip[1::2]

    abas = set()
    babs = set()
    
    for sub in supernet:
        for i in range(len(sub)-2):
            if is_ABA(aba := sub[i:i+3]):
                abas.add(aba)
                babs.add(flip(aba))

    for sub in hypernet:
        ssl = False
        for bab in babs:
            if bab in sub:
                ssl = True
                total += 1
                print("|".join(ip), bab)
                break
        if ssl: break


print(total)
