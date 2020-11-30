import re

def has_ABBA(string):
    return (match := re.search(r"(.)(.)\2\1", string)) is not None and (match[0][0] != match[0][1])

with open("7.in", "r") as f:
    ips = [re.split(r"[\[\]]", ip) for ip in f.read().splitlines()]

total = 0

for ip in ips:
    abba = any(has_ABBA(x) for x in ip[::2])
    no_abba = all(not has_ABBA(y) for y in ip[1::2])

    if abba and no_abba:
        total += 1

print(total)