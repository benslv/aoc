poly = list(open("day5.txt", "r").read())

reacted = None
while reacted or reacted is None:
    reacted = False
    i = 0
    while i < len(poly) - 1:
        if poly[i] == poly[i+1].swapcase():
            del poly[i]
            del poly[i]

            reacted = True
        i += 1

    if not reacted:
        break

print(len(poly))
